# Rock, Paper, Scissors: Advanced Terminal Logic

**Rock, Paper, Scissors** is a polished Python 3 terminal game that goes beyond basic conditional statements. The project showcases a focus on **defensive programming**, **data-driven logic**, and **cross-platform compatibility**, providing a seamless and "unbreakable" user experience.

---

## Architecture & Development Logic

The project's architecture was designed to be modular and resilient. Instead of a linear script, it utilizes structured loops and functions to manage the game flow.

### 1. Data-Driven Win Conditions
Unlike standard implementations that rely on massive nested `if/else` chains, this project uses a **Tuple-based Comparison** system. 
* A `win_conditions` list stores winning pairs as `(Winner, Loser)`. 
* The system performs a membership check (`in`) to determine the outcome, making the code highly scalable and readable.

### 2. Defensive Programming (Input Validation)
To prevent runtime crashes, the game implements a **Try-Except** block within a validation loop. This ensures that:
* Non-integer inputs (like letters or symbols) are caught without breaking the program.
* Inputs outside the valid range ($1-3$) are rejected, forcing a clean retry until a correct choice is made.

### 3. Cross-Platform UI Management
The software utilizes the `subprocess` module and `os.name` detection to execute system-level commands. This allows the `clear_screen()` function to work natively on both **Windows (NT)** and **Unix-based (Linux/macOS)** systems, maintaining a professional and clutter-free interface.

---

## Key Features

* **Modular Restart System:** A dedicated `exit_menu()` function with an internal `while` loop that guarantees valid user feedback before proceeding or closing.
* **Visual Polish:** Uses `time.sleep` and `flush=True` buffers to create a dramatic countdown and a smooth "closing" animation with visual dots.
* **Smart Mapping:** Utilizes Python Dictionaries to map integer choices to their string representations, separating internal logic from the user-facing display.
* **Zero-Crash Design:** Built to handle "garbage input" at every stage of the game.

---

## How to Run

1. **Prerequisites:**
   This project uses only native Python 3 libraries (**Random**, **Time**, **OS**, **Subprocess**).

2. **Clone the repository:**
   ```bash
   git clone https://github.com/Flaigue/Python-Projects.git
   ```

3. **Navigate to the folder:**
   ```bash
   cd RockPaperScissors
   ```

4. **Run the application:**
   ```bash
   python3 RockPaperScissors.py
   ```

---

## Roadmap (Future Iterations)

* [ ] **Extended Rules:** Implementation of *Rock Paper Scissors Lizard Spock* by expanding the tuple list.
* [ ] **Score Persistence:** Add a session-based leaderboard or save wins to a `.txt` file.
* [ ] **Color Integration:** Use ANSI escape codes to colorize "Victory" in green and "Defeat" in red for better terminal feedback.

---

## About the Author

Developed by **Leandro dos Reis**. A developer focused on turning simple logic into robust, professional-grade software.

**Connect with me:**
[LinkedIn Profile](https://www.linkedin.com/in/leandro-alves-nunes)

---

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.