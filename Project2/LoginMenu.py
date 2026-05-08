import os
from time import sleep
import subprocess

# --- PATH CONFIGURATION (Platform Independent) ---
# os.path.expanduser("~") finds the current user's home directory across Linux, macOS, and Windows
home_dir = os.path.expanduser("~")
# Join paths using os.path.join to handle different slash directions (/ vs \) automatically
data_folder = os.path.join(home_dir, "Documents", "User_Data")
user_file = os.path.join(data_folder, "users.txt")

# Create the data folder if it doesn't already exist to prevent FileNotFoundError
if not os.path.exists(data_folder):
    os.mkdir(data_folder)

# --- HELPER FUNCTIONS ---

def get_credentials():
    """Prompts user for name and password, removing accidental leading/trailing spaces."""
    print("\n" + "="*30)
    name = input("Name: ").strip()
    password = input("Password: ").strip()
    print("="*31)
    return name, password

def wait_animation(text):
    """Creates a simple visual loading effect with dots."""
    print(text, end="")
    for _ in range(3):
        sleep(0.5)
        # flush=True ensures the dots appear immediately in the terminal
        print(".", end="", flush=True)
    print("\n")

def clean_screen():
    """Detects OS and executes the appropriate terminal clearing command."""
    # 'nt' refers to Windows; others (posix) use 'clear'
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True)

# --- MAIN APPLICATION LOOP ---

while True:
    clean_screen()
    print("="*10, "HOME PAGE", "="*10)
    print("1 - Register User\n2 - Login User\n3 - Forgot Password\n4 - Exit Program")
    print("="*31)

    option = input(": ").strip()

    # 1. REGISTRATION LOGIC
    if option == "1":
        wait_animation("Initializing Registration")
        name, password = get_credentials()
        
        # Validation: Do not allow empty strings to be saved
        if not name or not password:
            print("Error: Fields cannot be empty!")
            sleep(1.5)
            continue

        # Duplicate Check: Search for existing username
        user_exists = False
        if os.path.exists(user_file):
            with open(user_file, "r") as f:
                for line in f:
                    # Using startswith + comma ensures "Ana" doesn't match "Anabela"
                    if line.startswith(f"{name},"):
                        user_exists = True
                        break
        
        if user_exists:
            print(f"Error: User '{name}' already exists! Try logging in.")
            sleep(2)
            continue
        else:
            # Mode "a" (Append) adds new data to the end without deleting existing content
            with open(user_file, "a") as f:
                f.write(f"{name},{password}\n")
            print("Registration successful!")
        sleep(2)

    # 2. LOGIN LOGIC
    elif option == "2":
        wait_animation("Initializing Login")
        l_name, l_password = get_credentials()
        login_success = False

        if os.path.exists(user_file):
            with open(user_file, "r") as f:
                for line in f:
                    # split(",") separates the name from the password saved in the text file
                    stored_name, stored_pass = line.strip().split(",")
                    if l_name == stored_name and l_password == stored_pass:
                        login_success = True
                        break
        
        if login_success:
            print(f"Welcome back, {l_name}!")
            # Prevents immediate screen clearing so the user can see the welcome message
            input("\nPress Enter to logout and return to menu...")
        else:
            print("Invalid credentials. Please try again.")
            sleep(2)

    # 3. PASSWORD RECOVERY LOGIC
    elif option == "3":
        print("\n" + "="*10, "RECOVERY", "="*10)
        target_name = input("Enter your username: ").strip()
        
        found = False
        all_users = []

        if os.path.exists(user_file):
            # Load all users into RAM list to allow in-memory editing
            with open(user_file, "r") as f:
                for line in f:
                    all_users.append(line.strip().split(","))

            # Locate the target user and update their password in the list
            for user_data in all_users:
                if user_data[0] == target_name:
                    found = True
                    print(f"User '{target_name}' found.")
                    new_password = input("Enter your NEW password: ").strip()
                    user_data[1] = new_password 
                    break
            
            if found:
                # Mode "w" (Write) overwrites the entire file with the updated RAM list
                with open(user_file, "w") as f:
                    for user in all_users:
                        f.write(f"{user[0]},{user[1]}\n")
                print("Password updated successfully!")
            else:
                print("User not found in our database.")
        else:
            print("Database is empty. Register first.")
        sleep(2)

    # 4. EXIT APPLICATION
    elif option == "4":
        wait_animation("Closing program")
        break

    # FALLBACK FOR INVALID INPUTS
    else:
        print("Invalid input! Please choose 1, 2, 3, or 4.")
        sleep(2)
