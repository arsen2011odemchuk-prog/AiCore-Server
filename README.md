# Hydra AI Cluster - Phase 1

## 📌 Project Overview
Hydra is a distributed computing cluster built to run AI models locally. Phase 1 establishes the **Control Plane**, responsible for networking and task management.
A high-performance, 4-node distributed computing cluster designed for local AI model inference (LLMs) and neural network orchestration using a headless Linux environment.

## Phase 1 is the development of a Hardware-Secured Control Plane.
This node is designed with a bespoke physical access layer. Using an integrated RFID/NFC sensor bridge, the system firmware is configured to lock the Ethernet Switch and all SSH communication at the hardware level. The server remains in a 'Cold State' until a physical Admin Card is present on the custom-wired sensor. This project involves original wiring between the motherboard's GPIO/Serial headers and a microcontroller (Arduino/Pico) to create a physical-to-digital security handshake."
### How to Use:
"The user must physically tap a registered Admin NFC token to the chassis sensor. The microcontroller verifies the hardware ID and sends an unlock signal to the Linux OS via a custom Python-Serial bridge, enabling the cluster network.
 The user connects to the Master Node via SSH over a local network. Using Docker and K3s (Kubernetes), AI workloads are distributed across the cluster nodes, allowing for parallel data    processing without relying on cloud services.
## How to use it: ##
## Why I made it: ##
I created this project to learn the fundamentals of distributed systems and to run powerful AI models locally. By building a cluster from consumer hardware, I am exploring cost-effective ways to scale compute power for deep learning.

## 🛠 Tech Stack
- **Hardware:** AMD AM4 Platform, NVIDIA CUDA (GT 210 for setup)
- **OS:** Ubuntu Server 24.04 LTS
- **Orchestration:** K3s (Kubernetes)

## 📂 Project Structure
- `/cad` - .STEP file of the system assembly
- `/firmware` - setup.sh for automated server configuration
- `/docs` - Wiring diagrams and network topology
- `BOM.csv` - Full list of components with links

## showing places where components will go
  <img width="565" height="512" alt="image" src="https://github.com/user-attachments/assets/df7e780e-a0fe-4d12-8852-84a4ea5d72b7" />

## System Interconnect & Wiring Strategy:
 Since Node 1 is built using standardized ATX/AM4 components, the wiring follows a strict modular power and data distribution plan:
- Power Delivery: The VIDA 500W PSU provides dedicated 24-pin ATX power to the MSI A520M motherboard and a 4+4 pin EPS connector for the Ryzen 3 4100 CPU.
- Storage Interface: The Integral 256GB SSD is mounted directly via the M.2 PCIe Gen3 x4 slot, eliminating the need for external SATA data and power cables to improve airflow.
- Network Topology: A Cat6 Ethernet cable connects the onboard Realtek GbE LAN to the TP-Link 5-Port Gigabit Switch. This switch serves as the communication backbone for the upcoming 4-node cluster.
- Initial Video Out: The NVIDIA GT 210 is connected via the PCIe x16 slot for the initial OS configuration.
  <img width="651" height="606" alt="image" src="https://github.com/user-attachments/assets/661a371f-92d1-4cc4-8b36-58a3dde44ee0" />

## Detailed Wiring & Interconnect Specifications

|cable type| from where to where|specification|purpose|
|:---|:---|:---|:---|
|ATX 24-Pin|	PSU -> Motherboard| Main Power Cable	|Main power supply for the entire board and chipset.|
|EPS 4+4 Pin|	PSU -> CPU Socket|	CPU Power Cable|	Dedicated power supply for Ryzen 3 4100.|
|SATA Power|	PSU -> Case Fans|	Peripheral Power|	Power supply for the case lights and fans Kolink.|
|PCI x16 Slot|	Motherboard -> GPU|	Bus Connection|	Data transfer and 75W power delivery for GT 210.|
|M.2 Interface|	Motherboard -> SSD|	PCIe Gen3 x4|	Direct connection without cables for Integral SSD.|
|Cat6 Ethernet|	Motherboard -> Switch|	RJ45 Gigabit Cable|Cluster network bridge (blue cable in the diagram).|
|Front Panel|	Case -> Motherboard|	JFP1 Headers	Кнопка |Power switches and indicators (Power/Reset).|

## Phase 1 Connectivity Strategy:
- For Node 1, I have optimized the wiring to ensure maximum airflow for 24/7 server stability.
- Direct Storage: By using an M.2 NVMe SSD, I eliminated the need for SATA data and power cables, reducing clutter.
- Modular Power: The 500W PSU delivers stable 12V rails to the Ryzen 3 4100 via an 8-pin EPS connector, ensuring no voltage drops during heavy AI orchestration tasks.
- Network Backbone: The connection to the TP-Link Gigabit Switch is the most critical link. It uses a shielded Cat6 cable to minimize interference, serving as the gateway for future compute nodes in the cluster.
- Headless Ready: The wiring for the GT 210 GPU is temporary. Once the Linux OS is configured, this card can be physically removed, leaving the PCIe slot empty to further improve cooling.



## 📊 BOM (Bill of Materials)

| Part | Model | Link | Price |
| :--- | :--- | :--- | :--- |
| CPU | Ryzen 3 4100 | [Link](https://www.amazon.co.uk/AMD-Ryzen-4100-processor-8-thread/dp/B09VCRQVWM/ref=sr_1_1?crid=2Y4QZQVLVT2IF&dib=eyJ2IjoiMSJ9.6dhmVMA2bcpC65UqGMUc8heYxtnIAl9I_GSjxGZF6Si1KWAe27YvQu2NrC2Wc_brCoaxr9Qpf5Ukyh1nmTaJ_xU6IV9ww8p9HGckBbx8OO_21IUt1MepfrSouBN_9NE9KvPK1QG-zX_tYDJGxqDUGdab9LjZ_hG_BW4wvv2bQdp8U8VxuV1HrKuFMSYbxBRpSxvdLOdIWVE3eL6_B-1F46pEI2KbAJIRqVHMMkrgWKA.q3slf3wyPvBp7CpuOpp5Nu-Shv-oOHgrLifTiBxMM2g&dib_tag=se&keywords=Ryzen%2B3%2B4100&qid=1774650962&sprefix=ryzen%2B3%2B4100%2B%2Caps%2C301&sr=8-1&th=1) | £49.00 |
| MB | Gigabyte A520M | [Link](https://www.amazon.co.uk/Gigabyte-Motherboard-Bandwidth-Management-Anti-Sulfur/dp/B0BXFBN121/ref=sr_1_4?crid=2DF9ISTZUVLCI&dib=eyJ2IjoiMSJ9.CEo89SXcm_D40jVjhvS9xBTqPMQW5tpZXSd1XonPYn3zyY2MiekLAw4GScfXxWQ8ocPk1Wlmihx3-8VhPleEi8nnWfy7ukRsCzyNWCE6W9mnAv6rdt5RthRGGuad-t36CPYH5zRfVTH6yMAABmp2XXlNz_-7XSUZhfp7CdasLAFM0LE1jqEN5ix0OVCNpsTefVswScMr9aB-wREn2b-WkZMQNx2m4gt_C2C0XLrRu8g.QByg4EcYt6kc11OSpW3AHFJ0jpDYOOmjk150k5uIWWY&dib_tag=se&keywords=MSI%2BA520M-A%2BPRO&qid=1774651125&sprefix=%2Caps%2C294&sr=8-4&th=1) | £43.97 |
| GPU | GT 210 1GB | [Link](https://www.amazon.co.uk/Dpofirs-Graphics-589MHz-Desktop-Computer/dp/B0C6R4HVXG/ref=sr_1_18_sspa?crid=81QTHR9TBHJR&dib=eyJ2IjoiMSJ9.fzr3WQFFAyhC7lrOwTvS3MbbwC8J8qXBNzvAQ8jfl1yBx-tNhTDV94GbMiB_95mlea8KhpLVjriA0DHU4UbfhDfo15vOr8rnodDESnOsdqXbUFnZFBj6INYOeAS1QyhepbA6v9fDIvtNY2lKHv0m1EEIX1IYv_v3hfnxWFUn6kgs3GNnoOlIcMhJwu3sg9SHrCqHzQb6uilaYjBvKMpLNbm4FYQwDwPBJiHw01iPZXQ.Prf9xRq-9jksqkp_0FLVLvYeVCus-69LaX4JVsQn1Vg&dib_tag=se&keywords=NVIDIA+780&qid=1774653595&refinements=p_36%3A-2800&rnid=428432031&sprefix=nvidia+780%2Caps%2C322&sr=8-18-spons&aref=exjaksy3r0&sp_csd=d2lkZ2V0TmFtZT1zcF9idGY&psc=1) | £27.95 |
| RAM | 16GB DDR4 | [Link](https://www.amazon.co.uk/Pesfehhy-Memoria-3200MHz-PC4-25600-PC4-19200/dp/B0F7Y1BWMG/ref=sr_1_2?crid=50X8J56P3MJX&dib=eyJ2IjoiMSJ9.fzsBwsEnwg-M09YIF2Fq-XxYinRWchJEt_Pv2GlQz8SS3-dSsam84dYDksF90CeDVB-61pKsjFCUnu6NG3niozy7XoXu2jvzHrzZ-j6UgAU2U6paeIlBihA9jOg14agKL5HfgPKDYTpMvC4rligoI3WWRjtdweeygoYS93S9qi82VrY44AjStKW9hZjYLis4sID_SeChPawzIycK6DvA381b25QqEJP9a0siLgUykDQ.P7v0JGeYk6ur1BrqbpUvcQiCqHrVqfhMF1GlJ9YwK0s&dib_tag=se&keywords=16GB+DDR4+3200MHz+RAM&qid=1774653810&refinements=p_36%3A-3000&rnid=428432031&sprefix=16gb+ddr4+3200mhz+ram%2Caps%2C320&sr=8-2) | £29.08 |
| SSD | 256GB NVMe | [Link](https://www.amazon.co.uk/Integral-256GB-Gen3x4-R-3350MB-W-1350MB/dp/B09P58BJ2L/ref=sr_1_16?crid=6P52QA6FMURZ&dib=eyJ2IjoiMSJ9.wVBCJw2QrKliTXPFdTVpvnxMCRWZkP2tX9VAt3NITNkuFww_Zs3iSncHyCuH1x-HK3SKex2JWZY7o73NNX396EtGZCh6Tuv1zoZs4WNjjHNBOh_3gbjFchV59-K6OEpaAsablNo35Zm7hFJoo7wlEHpUQGCpSwRWgy2oT-6RO51s2CM8xaZpuJPmSBNvwKxW3eGfYTig_BTKvv8gqD0jdc5Ckh2FgLQoDmd2Mz5NJ-E.CuqkSiAfqItbScDBErjfOKBt9E-jSVodgQkLoxhmuw8&dib_tag=se&keywords=NV2%2BM.2%2BNVMe%2BSSD&qid=1774651658&refinements=p_36%3A-5600&rnid=428432031&sprefix=nv2%2Bm.2%2Bnvme%2Bssd%2Caps%2C372&sr=8-16&th=1) | £39.95 |
| PSU | VIDA 500W | [Link](https://www.amazon.co.uk/VIDA-Bronze-Dynamic-Ultra-Quiet-Included/dp/B0FCYRFW9X/ref=sr_1_4?crid=32R0CKVC67WY1&dib=eyJ2IjoiMSJ9.5p7aulaFskwkUdO2fkgAcgOCl-aT7fvJQDWQetSoyWA_5S6U22M5Wbw6SwQbqQWxcw2FgEcx1QV-UQH7Alr4CZ0s-4CrAPTCieq249h74VwK1dTeOs6O3x85CSkwUxSX_KWtmx3o5PeeE37blFfhw8_wYn7e7Ilo117qyFGNcV7vnRWDiXl7JdOakDGpzyc7pHN8tbNdruQPBv1lwXGiLbfFi4zo8kmg7-WcwJPJDtk.zJyCWjpM8vIqa5QcDwVTL2vhllqb-W0nGde7txPlzhc&dib_tag=se&keywords=Aerocool+Integrator+500W+80%2B+Bronze&qid=1774651771&sprefix=aerocool+integrator+500w+80%2B+bronze%2Caps%2C280&sr=8-4) | £33.31 |
| Case | Kolink VOID | [Link](https://www.amazon.co.uk/Kolink-Void-Medium-Tower-Case-RGB-White/dp/B08VDCWP8V/ref=sr_1_50_sspa?crid=1SUP0ZEBTPGDT&dib=eyJ2IjoiMSJ9.Lcp6PqwRPi0B6BUKoOocn-Q21_GzKNQ9T2wKu91U5yrGjHj071QN20LucGBJIEps.ySzz2BkpXrFA4XsbcD2XmHHt-Btny7CD40L3V8BaoW8&dib_tag=se&keywords=CiT%2BSeven%2BMicro-ATX%2BCase&qid=1774652606&refinements=p_36%3A-3000&rnid=428432031&sprefix=%2Caps%2C455&sr=8-50-spons&xpid=_HXv35Cpptp6q&aref=SjyemuKIlQ&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfbmV4dA&th=1) | £27.98 |
| Switch | TP-Link 5-Port | [Link](https://www.amazon.co.uk/TP-Link-LS1005G-Wallmount-Ethernet-Splitter/dp/B07VWB347G/ref=sr_1_2?crid=3ECLN18I6IH85&dib=eyJ2IjoiMSJ9.jGhszS0jfnZN7qt8kNipT6PWfJDdsqSBNEGKcwsnmIJmQgcDI1fcal7NKLKlsD8wyVJ3o2JI-Tzq4mDZocX7msLOA45MzCEvx9geFTPpTlG9FJ5HpVSDJRPwukytSkGmHGM_uKBx6250X0ZUAkzRUikFmdzcpqB0rYgT5-8pDCurF90zoJHUZ1lxyqo3PkGBIH4kl95mQX4PSsokJdj-fvlkfcLGv4ZpxizXy2SPdBQ.4c4MRyYDBqgnDgxbv1x74Ji8wk647AppoUNYodEzGXw&dib_tag=se&keywords=TP-Link%2BLS1005G%2B6-Port%2BGigabit%2BDesktop%2BSwitch&qid=1774652747&refinements=p_36%3A-1300&rnid=428432031&sprefix=tp-link%2Bls1005g%2B6-port%2Bgigabit%2Bdesktop%2Bswitch%2Caps%2C305&sr=8-2&th=1) | £8.99 |
| **TOTAL** | | | **£260.23/$346,77** |
## future improvements 
currently i am plannign to build 4 nodes join it create my own programing language( that have better efficient) and make better ai.

