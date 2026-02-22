# Dynamic Christmas Tree: Terminal Art & Logic

**Dynamic Christmas Tree** is a Python script that generates a customizable, colored Christmas tree directly in the terminal. More than just a visual exercise, it integrates real-time date checking and advanced terminal styling to create a seasonal interactive experience.

---

## Architecture & Development Logic

The project moves beyond basic loops by implementing professional string manipulation and system integration:

### 1. RGB Terminal Rendering

Instead of standard terminal colors, this project uses **ANSI RGB escape sequences** (`\033[38;2;R;G;Bm`). By storing these in a dictionary, the code remains clean and allows for high-fidelity colors:

* **Star:** Yellow RGB.
* **Leaves:** Vibrant Green RGB.
* **Trunk:** Earthy Brown RGB.
* **Base:** Neutral Grey Background.

### 2. Time-Aware Logic

Using the `datetime` module, the application is "aware" of the current date. It implements a conditional system to deliver context-specific messages based on the calendar:

* **Christmas Eve (Dec 24th)**
* **Christmas Day (Dec 25th)**
* **December Season**
* **Off-Season messages**

### 3. Geometric Alignment Math

The tree's triangular shape is calculated dynamically based on user input. The logic ensures perfect symmetry by calculating spaces and character counts for each level:

* **Spaces:** `altura - andar`
* **Characters:** `2 * andar - 1`

---

## Key Features

* **Customizable Height:** User-defined input to scale the tree to any size.
* **Clean Interface:** Automatic terminal clearing using `os.system` for a focused visual output.
* **Dynamic Feedback:** Contextual messages that change based on the system's date.
* **Graceful Exit:** Controlled program closure to prevent the terminal from snapping shut after execution.

---

## How to Run

1. **Check Requirements:**
Works on any terminal that supports ANSI colors (tested on **Linux Mint/XFCE**).

3. **Clone the repository:**
```bash
git clone https://github.com/Flaigue/Python-Projects.git
```

3. **Navigate to the folder:**
```bash
cd ChristmasProject
```

4. **Run the script:**
```bash
python3 ChristmasTree.py
```

---

## About the Author

Developed by **Leandro dos Reis**. Focused on exploring the intersection between hardware-software interaction and creative coding.

**Connect with me:**
[LinkedIn Profile](https://www.linkedin.com/in/leandro-alves-nunes)

---

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

* **Attribution:** You must give appropriate credit to Leandro dos Reis.
* **Non-Commercial:** You may not use this material for commercial purposes without explicit permission.
