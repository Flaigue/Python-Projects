# PyAuth-Manager: Terminal-Based User Authentication

**PyAuth-Manager** is a lightweight, platform-independent Python utility designed to manage user credentials. It serves as a practical demonstration of advanced file handling, in-memory data manipulation, and cross-platform system integration without the need for external database engines.

---

## Technical Architecture & Data Logic

The system is built on the principle of **persistent text-based storage**, utilizing the Python Standard Library to ensure zero-dependency deployment.

### 1. Cross-Platform Path Resilience

The application utilizes `os.path.expanduser("~")` and `os.path.join()` to dynamically generate file paths. This ensures the script functions perfectly on **Linux**, **macOS**, and **Windows** by adapting to the specific directory separators and home folder structures of the host OS.

### 2. Intelligent Data Harvesting (Registration)

To prevent data corruption and redundancy, the registration logic implements:

* **Duplicate Detection:** Before saving, the system performs a "Read-Pass" using `.startswith(f"{name},")`. This specific string slicing prevents partial matches (e.g., stopping "Ana" from being flagged as a duplicate of "Anabela").
* **Append Mode (`"a"`):** New users are added to the end of the `users.txt` file, preserving existing data while minimizing memory overhead during the registration phase.

### 3. The "Memory-Bridge" Update Strategy (Recovery)

Since standard text files do not allow for the direct editing of specific lines, PyAuth-Manager implements a **RAM-to-Disk rewrite strategy** for password recovery:

1. **Ingestion:** The entire database is loaded into a nested list (`all_users`) in RAM.
2. **Manipulation:** The target user's password index is located and updated in memory.
3. **Overwrite (`"w"`):** The physical file is cleared and entirely rewritten with the updated list, ensuring data consistency.

---

## Core Features

* **Secure Registration:** Validates inputs to prevent empty credentials and checks for existing usernames to maintain a unique user base.
* **Robust Login:** Implements line-by-line parsing and string splitting to verify credentials against stored records.
* **Password Recovery:** Allows users to reset their passwords through a verified username search and file-rewrite logic.
* **Dynamic UI:** Uses `subprocess` to manage terminal states (`clear` vs `cls`) and `time.sleep` for realistic UX feedback.

---

## How to Use

### Prerequisites

* **Python:** 3.x
* **OS:** Windows, Linux, or macOS.

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Flaigue/Python-Projects.git

```


2. **Navigate to the directory:**
```bash
cd Python-Projects

```


3. **Run the application:**
```bash
python3 AuthSystem.py

```



---

## Technical Implementation Details

| Feature | Logic Used | Mode |
| --- | --- | --- |
| **Storage** | Plain Text (`.txt`) | N/A |
| **Separation** | Comma-Separated Values (CSV style) | N/A |
| **Pathing** | `os.path` | Dynamic |
| **Registration** | `open(file, "a")` | Append |
| **Login** | `open(file, "r")` | Read |
| **Recovery** | `open(file, "w")` | Overwrite |

---

## Development Context

This project was developed as an exploration of **local data persistence**. By avoiding complex database drivers (like SQLite or PostgreSQL), the project highlights the power of Python's built-in string manipulation and file I/O capabilities.

---

## Author

**Leandro dos Reis** *Focused on Linux optimization and transparent software architecture.*

---

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

---
