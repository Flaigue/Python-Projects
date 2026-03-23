# Professional CLI Hangman: State Machine & Data-Driven Logic

**Professional CLI Hangman** is a dynamic terminal-based game developed in Python. It utilizes standard library modules to create an interactive session, complete with categorized word banks, visual ASCII rendering, validation firewalls, and historical statistics tracking.

---

## Architecture & Development Logic

The application logic moves beyond basic linear scripts by managing game states and data structures efficiently:

### 1. Multi-Level Dictionary Seeding
Instead of hardcoding single flat lists, the game uses a **Hash Map (Dictionary)** to categorize datasets. 
* **The Logic:** `random.choice(list(categories.keys()))` picks the category first, and then a second `random.choice()` picks the target word.
* **Why this matters:** It decouples the data from the game engine, making it incredibly easy to add new themes without rewriting loop conditions.

### 2. State Memory & Deduplication
To ensure a fair and crash-proof user experience, the system maintains real-time tracking of duplicate actions:
* **List Comprehension Masking:** Dynamic generation of hidden arrays `[" " if char == " " else "_" for char in target]`.
* **Historical Memory:** Separate arrays track `lista_acertos` and `lista_erros` to prevent users from wasting turns on previously guessed letters.

### 3. Graceful Input Validation Flow
The primary game loop implements safety checks before processing game ticks:
* **Length capping:** Rejects attempts longer than 1 character (unless it is the `"dica"` keyword).
* **Single-use flags:** The boolean toggle `dica_usada` guarantees a hint can only be invoked once per session.

---

## Key Features

* **Dynamic ASCII Art Rendering:** Translates mathematical error counts directly into index-based drawing shifts (`stages[erros]`).
* **Session Persistence:** State variables reset per game while allowing infinite session restarts.
* **End-of-Game Analytics:** Prints comprehensive post-mortem metrics (Hit/Miss logs) whether the outcome is a Win or Loss.
* **Cross-Platform OS Clearing:** Smooth visual wipes between turns using `os.name` environment checks.

---

## How to Run

1. **Check Requirements:**
Works on any terminal that supports standard Python 3.

2. **Clone the repository:**
```bash
git clone https://github.com/Flaigue/Python-Projects.git
```

3. **Navigate to the folder:**
```bash
cd HangmanProject
```

4. **Run the script:**
```bash
python3 hangman.py
```

---

## About the Author

Developed by **Leandro dos Reis**. Focused on building reliable Python automation, terminal interfaces, and clean, defensive logic flows.

**Connect with me:**
[LinkedIn Profile](https://www.linkedin.com/in/leandro-alves-nunes)

---

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

**Key Terms:**
* **Attribution:** You must give appropriate credit to **Leandro dos Reis**.
* **Non-Commercial:** You may not use this code or its derivatives for commercial purposes.
* **Educational Use:** Feel free to study and modify the code for learning and professional growth.