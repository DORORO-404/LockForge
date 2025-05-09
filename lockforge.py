# ========= LockForge - Advanced File Encryptor =========
# Developed by dororo__404 | Version: 1.5.1

# === [IMPORT] Import required modules ===
try:
    import os
    import sys
    import getpass
    import pyAesCrypt
    import pyfiglet
except ImportError as e:
    missing = str(e).split("'")[1]
    print(f"\n[ERROR] Missing module: '{missing}'")
    print("\033[93m[WARNING] Please install all required dependencies before running this script.\033[0m")
    print("\033[94m[INFO] Required module: pyAesCrypt, pyfiglet\033[0m")
    print("\033[92m[SUGGESTION] You can install it directly using:\033[0m")
    print("\033[96m  → pip install pyAesCrypt, pyfiglet\033[0m\n")

    print("\033[95m[RECOMMENDED] Set up a virtual environment:\033[0m")
    print("\033[97mFor Linux / macOS:\033[0m")
    print("\033[96m    python3 -m venv venv && source venv/bin/activate\033[0m")
    print("\033[97mFor Windows:\033[0m")
    print("\033[96m    python -m venv venv && venv\\Scripts\\activate\033[0m\n")

    print("\033[92m[THEN] Install all requirements from file (if available):\033[0m")
    print("\033[96m  → pip install -r requirements.txt\033[0m\n")

    sys.exit(1)

# === [CONFIG] Configure ANSI colors for output ===
RESET   = "\033[0m"
BOLD    = "\033[1m"
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"

# === [INFO] Current version number ===
VERSION = "1.5.1"

# === [UI] Display ASCII banner for the program ===
def display_banner():
    banner = pyfiglet.figlet_format("LockForge")
    print(f"{MAGENTA}{banner}{RESET}")
    print(f"""{CYAN}
╔════════════════════════════════════════════╗
║   {MAGENTA}LockForge - AES File Encryptor{CYAN}           ║
║   {MAGENTA}By: DORORO__404   |  Version: v{VERSION}  {CYAN}   ║
╚════════════════════════════════════════════╝{RESET}
""")

# === [UI] Display welcome message for the user ===
def display_welcome():
    print(f"\n{MAGENTA}[+] Welcome to {GREEN}LockForge{MAGENTA} — Secure. Encrypt. Protect.{RESET}")
    print(f"{YELLOW}[INFO] AES-256 encryption ensures top-level security for your files.{RESET}")
    print(f"{YELLOW}[INFO] LockForge is ready to safeguard your data!{RESET}")
    print(f"{YELLOW}[INFO] Type '{CYAN}exit{YELLOW}', '{CYAN}quit{YELLOW}', '{CYAN}close{YELLOW}', or {CYAN}CTRL + C{YELLOW} at any time to exit.{RESET}")
    print(f"{CYAN}{'-' * 75}{RESET}")

# === [EXIT] Gracefully exit the program ===
def exit_lockforge():
    print(f"\n{GREEN}[INFO] Exiting LockForge...{RESET}")
    print(f"{MAGENTA}[THANK YOU] Thank you for trusting LockForge!{RESET}")
    print(f"{YELLOW}[INFO] Session ended successfully.\n{RESET}")
    sys.exit()

# === [INPUT] Handle user input with exit keywords support ===
def input_handler(message, is_password=False):
    try:
        while True:
            user_input = getpass.getpass(message).strip() if is_password else input(message).strip()
            if user_input.lower() in ["exit", "quit", "close"]:
                print(f"\n{YELLOW}[INFO] Exit command received.{RESET}")
                exit_lockforge()
            elif not user_input:
                print(f"{RED}[ERROR] Input cannot be empty. Please try again.{RESET}")
            else:
                return user_input
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}[INFO] Keyboard interrupt detected.{RESET}")
        exit_lockforge()

# === [INPUT] Get and validate the file path ===
def input_file(message):
    file_path = input_handler(message).strip()
    if not file_path:
        print(f"{RED}[ERROR] No file path provided.{RESET}")
        return None
    return os.path.abspath(os.path.normpath(file_path))

# === [ACTION] Confirm deletion of original file after encryption/decryption ===
def confirm_deletion(file):
    if not os.path.isfile(file):
        print(f"{RED}[ERROR] File '{WHITE}{file}{RED}' not found or invalid.{RESET}")
        return False
    confirm = input_handler(f"{YELLOW}[INPUT] Delete the original file? [Y/n]: {RESET}").lower()
    if confirm in ['y', 'yes', '']:
        try:
            os.remove(file)
            print(f"{GREEN}[SUCCESS] Original file deleted.{RESET}")
            return True
        except Exception as e:
            print(f"{RED}[ERROR] Error while deleting the file: {e}{RESET}")
            return False
    else:
        print(f"{YELLOW}[INFO] Original file was kept.{RESET}")
        return False

# === [ENCRYPT] Perform file encryption using AES ===
def encryption():
    file = input_file(f"\n{CYAN}[INPUT] Enter the full path or filename to encrypt: {RESET}")
    if not file or not os.path.isfile(file):
        print(f"{RED}[ERROR] File '{WHITE}{file}{RED}' not found or invalid.{RESET}")
        return

    while True:
        password = input_handler(f"{CYAN}[INPUT] Enter password to encrypt: {RESET}", is_password=True)
        if len(password) < 8:
            print(f"{RED}[ERROR] Password must be at least 8 characters.{RESET}")
            continue
        print(f"{YELLOW}[INFO] Password accepted.{RESET}")
        confirm_password = input_handler(f"{CYAN}[INPUT] Confirm password: {RESET}", is_password=True)
        if password == confirm_password:
            break
        else:
            print(f"{RED}[ERROR] Passwords do not match. Try again.{RESET}")

    try:
        print(f"\n{YELLOW}[INFO] Encrypting... Please wait.{RESET}")
        pyAesCrypt.encryptFile(file, file + ".aes", password, 64 * 1024)
        print(f"{GREEN}[SUCCESS] File encrypted as '{WHITE}{file}.aes{GREEN}'{RESET}\n")
        confirm_deletion(file)
    except Exception as e:
        print(f"{RED}[ERROR] Encryption failed: {e}{RESET}")

# === [DECRYPT] Perform file decryption and restore original ===
def decryption():
    file = input_file(f"\n{CYAN}[INPUT] Enter the full path or filename to decrypt: {RESET}")
    if not file.endswith(".aes"):
        file += ".aes"
    if not os.path.isfile(file):
        print(f"{RED}[ERROR] File '{WHITE}{file}{RED}' not found or invalid.{RESET}")
        return

    password = input_handler(f"{CYAN}[INPUT] Enter password to decrypt: {RESET}", is_password=True)
    new_file = file.replace(".aes", "")

    try:
        print(f"\n{YELLOW}[INFO] Decrypting... Please wait.{RESET}")
        pyAesCrypt.decryptFile(file, new_file, password, 64 * 1024)
        print(f"{GREEN}[SUCCESS] File decrypted as '{WHITE}{new_file}{GREEN}'{RESET}\n")
        confirm_deletion(file)
    except Exception as e:
        print(f"{RED}[ERROR] Decryption failed: {e}{RESET}")

# === [MENU] Display options menu and handle user selection ===
def choose_option():
    while True:
        print(f"\n{MAGENTA}[+] What would you like to do?{RESET}")
        print(f"{GREEN}[1] Encrypt a file{RESET}")
        print(f"{GREEN}[2] Decrypt a file{RESET}")
        print(f"{GREEN}[3] Exit LockForge{RESET}")
        choice = input_handler(f"{CYAN}[INPUT] Enter your choice: {RESET}")

        if choice == '1':
            encryption()
        elif choice == '2':
            decryption()
        elif choice == '3':
            print(f"\n{YELLOW}[INFO] Exit command received.{RESET}")
            exit_lockforge()
        else:
            print(f"{RED}[ERROR] Invalid option '{WHITE}{choice}{RED}'. Choose 1, 2, or 3.{RESET}")

# === [ARGS] Show version info if --version flag is passed ===
def show_version():
    if "--version" in sys.argv:
        print(f"{CYAN}[INFO] LockForge Version: {VERSION}{RESET}")
        sys.exit()

# === [MAIN] Main function to run the program ===
def main():
    show_version()
    try:
        display_banner()
        display_welcome()
        choose_option()
    except Exception as e:
        print(f"{RED}[ERROR] An unexpected error occurred: {e}{RESET}")
        exit_lockforge()

# === [ENTRY] Entry point for running script directly ===
if __name__ == "__main__":
    main()
