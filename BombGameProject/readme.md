# The Bomb Game: A Refactoring Journey

This project is a terminal-based logic and survival game. More than a simple script, this repository documents the transition from a functional prototype to a **refactored**, modularized, and error-resilient application.

## The Objective

The player must choose numbers between 1 and 5. One of these numbers is "mined." The goal is to survive as long as possible by picking only the safe numbers. If you hit the bomb, the game ends.

---

## Technical Highlights (Developer's Perspective)

During development, the focus shifted from "just making it work" to "making it right." Below are the technical implementations that demonstrate software engineering best practices:

## 1. Modularization & Control Flow

The code was refactored into specific functions (`play()` and `leave()`), eliminating linear logic and enabling an infinite game loop without requiring a manual script restart.

## 2. Exception Handling (Robustness)

Implementation of `try...except` blocks to catch `ValueError`. This ensures the program doesn't crash if the user enters invalid characters, maintaining a stable execution.

## 3. Portability (Cross-Platform)

Added conditional logic for terminal clearing:

```python
os.system("cls" if os.name == "nt" else "clear")

```

This ensures a clean and professional UI whether the game is running on **Windows** or **Linux**.

## 4. Explicit Conversion & Readability

I opted for explicit `str(input(...))` and `int(input(...))` conversions to make the code's intent obvious to other developers, prioritizing clarity over extreme conciseness.

---

## User Experience (UX/UI)

Even as a CLI (Command Line Interface) application, polish concepts were applied to increase immersion:

 **Programmed Suspense:** Use of the `time` module to create visual delays (`...`) when closing or restarting, simulating a real loading process.
 **Clean Interface:** The screen is constantly cleared to keep the player focused on the current action.
 **Immediate Feedback:** Clear messaging that distinguishes between success, input errors, and defeat.

---

## The "Museum Concept": Code Evolution

A key part of this repository is the preservation of the **original version** (`BombGameOldVersion.py`).

 **Why?** To serve as a historical record of technical evolution.
 **What changed?** The project moved away from "logical crutches" and redundancies toward a clean structure with better memory management and controlled recursion.

---

## How to Run

1. Ensure you have Python 3 installed.

2. Clone the repository:
```bash
git clone https://github.com/Flaigue/Python-Projects.git

```

3. Navigate to the folder:
```bash
cd BombGameProject

```

4. Run the game:
```bash
python3 BombGame.py

```


---

## About the Author

Developed by **Leandro Reis**. Passionate about IT and gaming, focused on learning how to transform pure logic into interactive experiences. Currently exploring the depths of Python on Linux Mint.

**Connect with me:**
[LinkedIn Profile](https://www.linkedin.com/in/leandro-alves-nunes)
