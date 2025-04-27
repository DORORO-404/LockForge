# ========= LockForge - Advanced File Encryptor =========

# === Import Modules ===
import os
import sys
import getpass
import pyAesCrypt
import pyfiglet
from colorama import Fore, Style as ColoramaStyle, init as colorama_init

# === Initialize Colorama ===
colorama_init(autoreset=True, strip=False, convert=True)

# === Program Info ===
VERSION = "1.2"

# === Color Shortcuts ===
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE
RESET = ColoramaStyle.RESET_ALL

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
    print(f"{YELLOW}[i] AES-256 encryption ensures top-level security for your files.{RESET}")
    print(f"{YELLOW}[i] LockForge is ready to safeguard your data!{RESET}")

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
            user_input = getpass.getpass(message).strip() if is_password else input(message).strip()

            if user_input.lower() in ["exit", "quit", "close"]:
                print(f"\n{YELLOW}[i] Exit command received.{RESET}")
                exit_lockforge()
            elif not user_input:
                print(f"{RED}[!] Input cannot be empty. Please try again.{RESET}")
            else:
                return user_input
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}[i] Keyboard interrupt detected.{RESET}")
        exit_lockforge()

# === Ask for a file path and validate it ===
def input_file(message):
    file_path = input_handler(message).strip()
    
    if not file_path:
        print(f"{RED}[!] No file path provided.{RESET}")
        return None

    file_path = os.path.abspath(os.path.normpath(file_path))
    return file_path

# === Confirm deletion of a file after successful operation ===
def confirm_deletion(file):
    if os.path.isfile(file):
        confirm = input_handler(f"{YELLOW}[?] {CYAN}Delete the original file? [Y/n]: {RESET}").lower()
        return confirm in ['y', 'yes', '']
    else:
        print(f"{RED}[!] File {WHITE}'{file}'{RED} not found or invalid.{RESET}")
        return False

# === Encrypts a specified file ===
def encryption():
    user_file = input_file(f"\n{CYAN}[>] {WHITE}Enter the full path or filename of the file you want to encrypt: {RESET}")
    if not user_file or not os.path.isfile(user_file):
        print(f"{RED}[!] File {WHITE}'{user_file}'{RED} not found or invalid.{RESET}")
        return

    password = input_handler(f"{CYAN}[>] {WHITE}Please enter a password to encrypt the file: {RESET}", is_password=True)
    buffer_size = 64 * 1024

    try:
        print(f"\n{YELLOW}[i] Encrypting... Please wait.{RESET}")
        pyAesCrypt.encryptFile(user_file, user_file + ".aes", password, buffer_size)
        print(f"{GREEN}[✓] File encrypted successfully as {CYAN}'{user_file}.aes'{RESET}\n")

        if confirm_deletion(user_file):
            os.remove(user_file)
            print(f"{GREEN}[✓] Original file deleted.{RESET}")
        else:
            print(f"{YELLOW}[i] Original file was kept.{RESET}")

    except Exception as e:
        print(f"{RED}[!] Encryption failed: {e}{RESET}")

# === Decrypts an encrypted file ===
def decryption():
    user_file = input_file(f"\n{CYAN}[>] {WHITE}Enter the full path or filename of the encrypted file: {RESET}")
    if not user_file.endswith(".aes"):
        user_file += ".aes"
    
    if not os.path.isfile(user_file):
        print(f"{RED}[!] File {WHITE}'{user_file}'{RED} not found or invalid.{RESET}")
        return

    password = input_handler(f"{CYAN}[>] {WHITE}Please enter the password to decrypt the file: {RESET}", is_password=True)
    buffer_size = 64 * 1024
    new_file = user_file.replace(".aes", "")

    try:
        print(f"\n{YELLOW}[i] Decrypting... Please wait.{RESET}")
        pyAesCrypt.decryptFile(user_file, new_file, password, buffer_size)
        print(f"{GREEN}[✓] File decrypted successfully as {CYAN}'{new_file}'{RESET}\n")

        if confirm_deletion(user_file):
            os.remove(user_file)
            print(f"{GREEN}[✓] Encrypted file deleted.{RESET}")
        else:
            print(f"{YELLOW}[i] Encrypted file was kept.{RESET}")

    except Exception as e:
        print(f"{RED}[!] Decryption failed: {e}{RESET}")

# === Displays options menu and processes user selection ===
def choose_option():
    while True:
        print(f"\n{MAGENTA}[★] {CYAN}What would you like to do?{RESET}")
        print(f"{BLUE}[1] 📁🔒 {WHITE}Encrypt a file{RESET}")
        print(f"{BLUE}[2] 📂🔓 {WHITE}Decrypt a file{RESET}")
        print(f"{BLUE}[3] 🚪👋 {WHITE}Exit LockForge{RESET}")
        choice = input_handler(f"{CYAN}[>] {YELLOW}Enter your choice: {RESET}")

        if choice == '1':
            encryption()
        elif choice == '2':
            decryption()
        elif choice == '3':
            exit_lockforge()
        else:
            print(f"{RED}[!] Invalid option '{choice}'. Please choose 1, 2, or 3.{RESET}")

# === Main entry point: initializes the tool ===
def main():
    try:
        display_banner()
        display_welcome()
        print(f"\n{CYAN}{'-' * 75}{RESET}")
        choose_option()

    except Exception as e:
        print(f"{RED}[!] An unexpected error occurred: {e}{RESET}")
        exit_lockforge()

# === Execute LockForge ===
if __name__ == "__main__":
    main()
