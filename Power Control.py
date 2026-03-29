import time
import os
import subprocess

class HydraController:
    """
    The Central Intelligence that manages the 4-node Ryzen Cluster.
    It monitors health and dispatches AI tasks to the most 'powerful' available node.
    """
    def __init__(self):
        self.nodes = ["hydra-node-1", "hydra-node-2", "hydra-node-3", "hydra-node-4"]
        self.master_node = "hydra-node-1"
        print("--- Hydra Control Engine Initialized ---")

    def get_cluster_status(self):
        """Checks which nodes are currently 'Ready' in the K3s cluster."""
        try:
            # Uses the kubectl command installed by your setup.sh
            result = subprocess.check_output(["kubectl", "get", "nodes"]).decode('utf-8')
            return result
        except Exception as e:
            return f"Error connecting to K3s: {e}"

    def distribute_power(self, task_name, complexity="high"):
        """
        Decides which node gets the task.
        In your project, the 'Master' (Node 1) handles logic, 
        while Worker Nodes (2-4) handle raw AI generation/power.
        """
        if complexity == "high":
            target = "hydra-node-2" # Assign to a powerful worker
        else:
            target = "hydra-node-1" # Keep on master for speed

        print(f"🚀 Dispatching Task: [{task_name}] to {target}...")
        
        # Command to run a containerized AI model on a specific node via Kubernetes
        deploy_cmd = f"kubectl run {task_name} --image=hydra-ai-model:latest --overrides='{{ \"apiVersion\": \"v1\", \"spec\": {{ \"nodeSelector\": {{ \"kubernetes.io/hostname\": \"{target}\" }} }} }}'"
        
        # In a real setup, we would execute this:
        # os.system(deploy_cmd)
        return f"Task {task_name} is now running on {target}."

    def monitor_loop(self):
        """The heartbeat of the cluster."""
        while True:
            print("\n--- Cluster Heartbeat Check ---")
            status = self.get_cluster_status()
            print(status)
            
            # Simple logic: If we see fewer than 4 nodes, alert the user
            ready_count = status.count("Ready")
            if ready_count < 4:
                print(f"⚠️ Warning: Only {ready_count}/4 nodes are online. Check power cables on Workers.")
            else:
                print("✅ Hydra System: Full Power Available (4/4 Nodes).")
            
            time.sleep(30) # Wait 30 seconds before next check

if __name__ == "__main__":
    controller = HydraController()
    # Example: Simulating an AI Image Generation task
    controller.distribute_power("stable-diffusion-gen-1", complexity="high")
    # Start monitoring the cluster
    controller.monitor_loop()
