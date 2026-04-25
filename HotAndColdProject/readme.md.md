# Hot and Cold: A Logic-Based Guessing Game

**Hot and Cold** is a terminal-based intuition game developed in Python 3. The project demonstrates core programming concepts such as input sanitization, cross-platform system integration, and dynamic feedback loops based on mathematical proximity.

---

## Architecture & Development Logic

The software follows a **modular functional design**, prioritizing a clean user experience (UX) and robust error handling. The core pillars include:

### 1. Advanced Input Sanitization
The `filter_input()` function acts as a security layer, ensuring that only integers within the $[0, 100]$ range are processed. It prevents crashes from "garbage input" (strings or symbols) by using recursion-like loop validation.

### 2. Proximity-Based Feedback Algorithm
Instead of simple "Higher/Lower" hints, the game implements a **thermal distance logic**. Using the `abs()` (absolute value) function, the system calculates the mathematical distance ($|chosen\_num - guess|$) to provide granular feedback:
* **Very Hot:** Within 5 units.
* **Warm/Cold:** Intermediate ranges.
* **Frozen:** Beyond 25 units of distance.

### 3. Cross-Platform UI Management
To ensure a professional look, the project includes a `clear_screen()` function that detects the host Operating System (`os.name`). It executes `cls` for Windows and `clear` for Unix-based systems (Linux/macOS) via the `subprocess` module, maintaining a clutter-free terminal.

---

## Key Features

* **User-Centric UX:** Uses `time.sleep` and visual "loading dots" to create transitions between game states.
* **State Persistence:** Manages global variables for attempts and target numbers, allowing seamless resets without restarting the script.
* **Defensive Programming:** Implements a catch-all `else` in the hint logic to ensure the program never enters an undefined state.
* **Clean Feedback:** A clear distinction between "First Try" victories and multi-attempt wins for a more rewarding player experience.

---

## How to Run

1. **Prerequisites:**
   The project uses native Python libraries (**Random**, **OS**, **Subprocess**, **Time**). No external installations are required.

2. **Clone the repository:**
   ```bash
   git clone https://github.com/Flaigue/Python-Projects.git
   ```

3. **Navigate to the project folder:**
   ```bash
   cd HotAndCold
   ```

4. **Run the application:**
   ```bash
   python3 HotAndCold.py
   ```

---

## Roadmap (Future Iterations)

* [ ] **Difficulty Modes:** Implement "Hard Mode" with a dynamic range (0-500) or fewer attempts.
* [ ] **Session Statistics:** Track the average number of attempts per win during a single session.
* [ ] **Colorized Output:** Integrate `colorama` to display "Hot" hints in red and "Cold" in blue.

---

## About the Author

Developed by **Leandro dos Reis**. Passionate about software development and logic, focused on building clean, efficient, and well-documented code.

**Connect with me:**
[LinkedIn Profile](https://www.linkedin.com/in/leandro-alves-nunes)

---

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.