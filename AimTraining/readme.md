# Aim Flow: Precision Training Tool

**Aim Flow** is a precision-training mini-game developed in Python 3. The project focuses on Graphical User Interface (GUI) manipulation and real-time game state management, challenging users to click dynamically generated targets under time pressure.

---

## Architecture & Development Logic

The project was built using a functional approach with a focus on **Event-Driven Programming**. Below are the core technical pillars:

### 1. State Management

The software alternates between three main states:

* **Idle:** The system remains on standby until the first click, preserving resources and user time.
* **Active:** The game loop initiates, triggering the countdown timer and scoring logic.
* **GameOver:** Inputs are deactivated (`state="disabled"`) and the interface is cleared to display results and reset/exit options.

### 2. Non-blocking Timer Logic

Unlike basic approaches that use `time.sleep()` (which would freeze the GUI), this project utilizes Tkinter's `.after()` method. This allows the timer to run asynchronously, keeping the interface fluid and responsive.

### 3. Dynamic Geometry & Responsiveness

Target positioning logic calculates window dimensions (`winfo_width` / `winfo_height`) in real-time. This ensures the button is never generated outside the visible area, regardless of window resizing or maximization.

---

## Key Features

* **Start On Click:** Global variables and timers only trigger after the user's first interaction.
* **Real-time Score System:** Instant precision tracking.
* **Boundary Detection:** A robust algorithm to prevent UI clipping and ensure targets stay within bounds.
* **Soft Reset:** A dedicated function to revert all global variables and UI states to default without restarting the process.

---

## How to Run

1. **Check Dependencies:**
The project uses only native Python libraries (**Tkinter**, **Random**, **OS**).

2. **Clone the repository:**
```bash
git clone https://github.com/Flaigue/Python-Projects.git
```

3. **Navigate to the AimTraining folder:**
```bash
cd AimTraining
```

4. **Run the application:**
```bash
python3 AimFlow.py
```

> **Note:** Ensure the `Python.png` file is in the configured directory for the application icon to load correctly.

---

## Roadmap (Future Iterations)

* [ ] **Data Persistence:** Save High Scores using JSON or SQLite.
* [ ] **Difficulty Levels:** Progressive reduction of target size as the score increases.
* [ ] **OOP Refactoring:** Migrate logic to Classes (Object-Oriented Programming) for better scalability.

---

## About the Author

Developed by **Leandro dos Reis**. Passionate about IT and gaming, focused on transforming logic into interactive experiences.

**Connect with me:**
[LinkedIn Profile](https://www.linkedin.com/in/leandro-alves-nunes)

---

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

**Key Terms:**
 **Attribution:** You must give appropriate credit to **Leandro dos Reis**, providing a link to this repository and indicating if any changes were made.
 **Non-Commercial:** You may not use this code or its derivatives for commercial purposes without explicit permission.
 **Educational Use:** Feel free to download, study, and modify the code for learning and personal growth.
