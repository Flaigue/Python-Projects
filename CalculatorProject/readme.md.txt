# Professional CLI Calculator: Functional Logic & Input Defense

**Professional CLI Calculator** is a robust Python utility designed for reliable mathematical operations within the terminal. Beyond simple arithmetic, this project focuses on **defensive programming**, **scalable design patterns**, and a polished **user experience** through intelligent flow control.

---

## Architecture & Development Logic

The project is built on the principle of "separation of concerns," dividing the code into logical layers for math, validation, and execution:

### 1. Dictionary Dispatch Pattern
Instead of using fragile `if/else` or `match/case` chains, the application implements a **dispatch table** using a Python dictionary. This maps string operators directly to their respective functions:

* **Scalability:** Adding new operations (like Power or Square Root) requires zero changes to the core loop logic.
* **Performance:** Constant-time $O(1)$ lookup for operations.
* **Clean Code:** Highly readable mapping of `"+": add`, `"-": subtract`, etc.

### 2. Defensive Input Filtering (`getnumber`)
The application implements a "Firewall" function that prevents crashes caused by invalid data types. It uses a **Recursive Validation Loop** with exception handling:

* **Type Safety:** Uses `try-except` blocks to catch `ValueError` before they reach the main logic.
* **Persistence:** The function only returns control to the main program once a valid `float` is provided.

### 3. Nested State Management
The software manages the program lifecycle through nested `while` loops, ensuring that the user’s progress (like the first number) is not lost if they make a mistake during the operator selection phase.

---

## Key Features

* **Crash-Proof Input:** Sophisticated handling of non-numeric characters to ensure the terminal never terminates unexpectedly.
* **Zero-Division Protection:** Embedded logic within the `divide` function to return a graceful error message instead of a system crash.
* **OS-Aware Interface:** Uses `os.name` to detect the host environment (Windows vs. Unix) and clear the terminal screen appropriately.
* **Polished Exit Sequence:** A timed visual feedback loop (`time.sleep`) and string-stripping logic to provide a smooth transition when closing the app.

---

## How to Run

1.  **Check Requirements:**
    Requires **Python 3.1** installed on any standard terminal.

2.  **Clone the repository:**
    ```bash
    git clone https://github.com/Flaigue/Python-Projects.git
    ```

3.  **Navigate to the folder:**
    ```bash
    cd CalculatorProject
    ```

4.  **Run the script:**
    ```bash
    python3 calculator.py
    ```

---

## About the Author

Developed by **Leandro dos Reis**. Focused on building robust software solutions with a focus on clean code, defensive programming, and optimal logic structures.

**Connect with me:**
[LinkedIn Profile](https://www.linkedin.com/in/leandro-alves-nunes)

---

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

**Key Terms:**
* **Attribution:** You must give appropriate credit to **Leandro dos Reis**.
* **Non-Commercial:** You may not use this code or its derivatives for commercial purposes.
* **Educational Use:** Feel free to study and modify the code for learning and professional growth.