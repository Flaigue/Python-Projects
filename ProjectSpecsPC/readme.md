# SystemSpecs-PY: Linux Hardware & OS Info

**SystemSpecs-PY** is a lightweight Python utility designed to extract and display detailed hardware and software specifications directly from the terminal. Originally developed on a **Linux Mint XFCE** environment, this project prioritizes direct system file interrogation over heavy third-party libraries, providing a fast and "bare-metal" feel to system monitoring.

---

## Architecture & Extraction Logic

The core philosophy of this script is **native data harvesting**. Instead of relying solely on high-level APIs, it parses raw system files to ensure maximum accuracy on Linux distributions.

### 1. Direct Kernel Interrogation
The script reads directly from the Linux virtual file system:
*   **/etc/os-release:** Parsed to retrieve the "Pretty Name" of the distribution and its specific version codename.
*   **/proc/cpuinfo:** Scanned line-by-line to extract the exact CPU model, L3 cache size, and physical core count.
*   **Environment Variables:** Uses `os.environ` to detect the active **Desktop Environment (DE)** (e.g., XFCE, Cinnamon, KDE) without executing external probes.

### 2. Intelligent String Cleaning
Raw data from Linux system files is often cluttered with technical prefixes. This script implements custom string manipulation logic:
*   Uses `.split()`, `.replace()`, and `.strip()` to remove redundant tags like `(R)`, `CPU`, or `model name:`.
*   Applies `.capitalize()` and `.join()` methods to ensure the output is formatted elegantly for the user.

### 3. Hardware Bus Probing
For GPU detection, the script utilizes the `subprocess` module to run the `lspci` command. The raw byte output is captured, decoded to UTF-8, and filtered using a refined "right-split" logic to isolate the specific Graphics Card model, stripping away revision codes and bus addresses.

---

## Key Features

*   **OS Insight:** Displays Generic Kernel info, Pretty Distro Name, and Version Codename.
*   **Deep CPU Analytics:** Real-time frequency monitoring, architecture detection, cache size, and physical core counting.
*   **GPU Identification:** Extracts the specific Graphics Card model via PCI bus filtering.
*   **Advanced RAM Metrics:** Provides a comprehensive breakdown of **Total, Used, Available, and Free Memory** converted into Gigabytes (GB) with two-decimal precision.
*   **Live Performance Tracking:** Utilizes `psutil` to calculate CPU and RAM usage percentages in real-time.

---

## How to Run

### Prerequisites
*   **System:** Linux (Optimized for Debian/Ubuntu-based distros).
*   **Python:** 3.1.
*   **Dependencies:** `psutil` (for memory and usage metrics).

### Installation
1. **Install the required library:**
   ```bash
   pip install psutil
   ```

2. **Clone the repository:**
   
```bash
   git clone https://github.com/Flaigue/Python-Projects.git
   ```

3. **Run the script:**
   ```bash
   python3 Specs.py
   ```

---

## Development Context

This project was built and optimized on a modest **Linux Mint XFCE** machine. The goal was to prove that efficient Python logic can replace heavy system monitor tools. By reading directly from `/proc` and `/etc`, **SystemSpecs-PY** maintains a tiny memory footprint, making it ideal for older hardware or minimal server environments.

---

## Roadmap

- [ ] **Storage Analytics:** Add a section for Disk partitions and Health (SSD/HDD).
- [ ] **Battery Status:** Implementation of power level tracking for laptops.
- [ ] **Network Info:** Display local IP and Interface speeds.

---

## About the Author

Developed by **Leandro dos Reis**. A developer focused on Linux optimization and creating high-transparency system tools.

**Hardware Focus:** Linux Mint XFCE Edition.

---

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.
