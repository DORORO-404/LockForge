# ========= LockForge - Advanced File Encryptor =========

# === Import Modules ===
import os
import sys
import getpass
import pyAesCrypt
import pyfiglet
from colorama import Fore, Style, init

# === Initialize Colorama ===
init(autoreset=True, strip=False, convert=True)

# === Program Info ===
VERSION = "1.3"

# === Color Shortcuts ===
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

# === Display the ASCII banner for LockForge ===
def display_banner():
    banner = pyfiglet.figlet_format("LockForge")
    print(f"{MAGENTA}{banner}{RESET}")
    print(f"""{CYAN}
╔════════════════════════════════════════════╗
║   {MAGENTA}LockForge - AES File Encryptor{CYAN}           ║
║   {MAGENTA}By: DORORO__404   |  Version: v{VERSION}  {CYAN}     ║
╚════════════════════════════════════════════╝{RESET}
""")

# === Display a welcome message to the user ===
def display_welcome():
    print(f"\n{MAGENTA}[★] {GREEN}Welcome to {MAGENTA}LockForge{GREEN} — Secure. Encrypt. Protect.{RESET}")
    print(f"{YELLOW}[i] {CYAN}AES-256 encryption{YELLOW} ensures top-level security for your files.{RESET}")
    print(f"{YELLOW}[i] {CYAN}LockForge{YELLOW} is ready to safeguard your data!{RESET}")
    print(f"{YELLOW}[i] Type '{CYAN}exit{YELLOW}', '{CYAN}quit{YELLOW}', '{CYAN}close{YELLOW}', or {CYAN}CTRL + C{YELLOW} at any time to exit.{RESET}")
    print(f"{CYAN}{'-' * 75}{RESET}")

# === Gracefully exit the program ===
def exit_lockforge():
    print(f"\n{GREEN}[*] Exiting LockForge...{RESET}")
    print(f"{MAGENTA}[!] Thank you for trusting LockForge!{RESET}")
    print(f"{YELLOW}[i] Session ended successfully.\n{RESET}")
    sys.exit()

# === Handle user input with support for exit keywords and password masking ===
def input_handler(message, is_password=False):
    try:
        while True:
            # Use getpass if it's for a password
            user_input = getpass.getpass(message).strip() if is_password else input(message).strip()

            # Check for exit keywords
            if user_input.lower() in ["exit", "quit", "close"]:
                print(f"\n{YELLOW}[i] Exit command received.{RESET}")
                exit_lockforge()

            # If input is empty
            elif not user_input:
                print(f"{RED}[!] Input cannot be empty. Please try again.{RESET}")
            else:
                return user_input
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}[i] Keyboard interrupt detected.{RESET}")
        exit_lockforge()

# === Ask for a file path and validate it ===
def input_file(message):
    # Get the file path using input_handler
    file_path = input_handler(message).strip()
    
    # Validate the file path
    if not file_path:
        print(f"{RED}[!] No file path provided.{RESET}")
        return None

    # Convert to absolute path
    file_path = os.path.abspath(os.path.normpath(file_path))
    return file_path

# === Confirm deletion of a file after successful operation ===
def confirm_deletion(file):
    # Check if the file exists
    if not os.path.isfile(file):
        print(f"{RED}[!] File '{WHITE}{file}{RED}' not found or invalid.{RESET}")
        return False

    # Ask for confirmation to delete the file
    confirm = input_handler(f"{YELLOW}[?] Delete the original file? [Y/n]: {RESET}").lower()
    if confirm in ['y', 'yes', '']:
        try:
            os.remove(file)
            print(f"{GREEN}[✓] Original file deleted.{RESET}")
            return True
        except Exception as e:
            print(f"{RED}[!] Error occurred while deleting the file: {e}{RESET}")
            return False
    else:
        print(f"{YELLOW}[i] Original file was kept.{RESET}")
        return False

# === Encrypts a specified file ===
def encryption():
    # Get the file to be encrypted
    file = input_file(f"\n{CYAN}[>] Enter the full path or filename of the file you want to encrypt: {RESET}")
    if not file or not os.path.isfile(file):
        print(f"{RED}[!] File '{WHITE}{file}{RED}' not found or invalid.{RESET}")
        return

    # Get the password for encryption
    while True:
        password = input_handler(f"{CYAN}[>] Please enter a password to encrypt the file: {RESET}", is_password=True)
        if len(password) < 8:
            print(f"{RED}[!] Password must be at least 8 characters long.{RESET}")
            continue
        else:
            print(f"{YELLOW}[i] Password accepted.{RESET}")
    
        confirm_password = input_handler(f"{CYAN}[>] Confirm the password: {RESET}", is_password=True)
        
        if password == confirm_password:
            break
        else:
            print(f"{RED}[!] Passwords do not match. Please try again.{RESET}")

    # Define the buffer size for encryption
    buffer_size = 64 * 1024

    # Try encrypting the file using pyAesCrypt
    try:
        print(f"\n{YELLOW}[i] Encrypting... Please wait.{RESET}")

        pyAesCrypt.encryptFile(file, file + ".aes", password, buffer_size)

        print(f"{GREEN}[✓] File encrypted successfully as '{WHITE}{file}.aes{GREEN}'{RESET}\n")

        # Confirm deletion of the original file
        confirm_deletion(file)

    except Exception as e:
        print(f"{RED}[!] Encryption failed: {e}{RESET}")

# === Decrypts an encrypted file ===
def decryption():
    # Get the encrypted file path
    file = input_file(f"\n{CYAN}[>] Enter the full path or filename of the encrypted file: {RESET}")
    
    # Ensure the file ends with ".aes" extension
    if not file.endswith(".aes"):
        file += ".aes"
    
    # Check if the file exists
    if not os.path.isfile(file):
        print(f"{RED}[!] File '{WHITE}{file}{RED}' not found or invalid.{RESET}")
        return

    # Get the password for decryption
    password = input_handler(f"{CYAN}[>] Please enter the password to decrypt the file: {RESET}", is_password=True)

    # Define the buffer size for decryption
    buffer_size = 64 * 1024

    # Define the new file name for the decrypted file
    new_file = file.replace(".aes", "")

    try:
        print(f"\n{YELLOW}[i] Decrypting... Please wait.{RESET}")

        pyAesCrypt.decryptFile(file, new_file, password, buffer_size)

        print(f"{GREEN}[✓] File decrypted successfully as '{WHITE}{new_file}{GREEN}'{RESET}\n")

        # Confirm deletion of the encrypted file
        confirm_deletion(file)

    except Exception as e:
        print(f"{RED}[!] Decryption failed: {e}{RESET}")

# === Displays options menu and processes user selection ===
def choose_option():
    while True:
        # Display the menu options
        print(f"\n{MAGENTA}[★] {GREEN}What would you like to do?{RESET}")
        print(f"{GREEN}[1] 📁🔒 {WHITE}Encrypt a file{RESET}")
        print(f"{GREEN}[2] 📂🔓 {WHITE}Decrypt a file{RESET}")
        print(f"{GREEN}[3] 🚪👋 {WHITE}Exit LockForge{RESET}")
        
        # Get the user's choice
        choice = input_handler(f"{CYAN}[>] Enter your choice: {RESET}")

        # Process the choice
        if choice == '1':
            encryption()
        elif choice == '2':
            decryption()
        elif choice == '3':
            print(f"\n{YELLOW}[i] Exit command received.{RESET}")
            exit_lockforge()
        else:
            # Invalid input handling
            print(f"{RED}[!] Invalid option '{WHITE}{choice}{RED}'. Please choose 1, 2, or 3.{RESET}")

# === Main entry point: initializes the tool ===
def main():
    try:
        # Display the banner and welcome message
        display_banner()
        display_welcome()

        # Show the options menu
        choose_option()

    except Exception as e:
        # Catch unexpected errors and exit gracefully
        print(f"{RED}[!] An unexpected error occurred: {e}{RESET}")
        exit_lockforge()

# === Execute LockForge ===
if __name__ == "__main__":
    main()
