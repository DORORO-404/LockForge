# ========= LockForge - Advanced File Encryptor =========

# === Import Modules ===
import os
import sys
import getpass
import pyAesCrypt
import pyfiglet
from colorama import Fore, Style, init

# === Initialize Colorama ===
init(autoreset=True)

# === Program Info ===
VERSION = "1.1"

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
    print(f"{CYAN}{banner}{RESET}")
    print(f"""{CYAN}
╔════════════════════════════════════════════╗
║   {MAGENTA}LockForge - AES File Encryptor{CYAN}           ║
║   {MAGENTA}By: DORORO__404   |  Version: v{VERSION}  {CYAN}     ║
╚════════════════════════════════════════════╝{RESET}
""")

# === Display a welcome message to the user ===
def display_welcome():
    print(f"\n{GREEN}[★] Welcome to {MAGENTA}LockForge{GREEN} — Secure. Encrypt. Protect.{RESET}")
    print(f"{YELLOW}[i] AES-256 encryption ensures top-level security for your files.{RESET}")
    print(f"{YELLOW}[i] LockForge is now ready to protect your data!{RESET}")

# === Gracefully exit the program ===
def exit_lockforge():
    print(f"\n{GREEN}[*] Exiting LockForge...{RESET}")
    print(f"{MAGENTA}[!] Thank you for using LockForge!{RESET}")
    print(f"{YELLOW}[i] Your session has been successfully closed.\n{RESET}")
    sys.exit()

# === Handle general input with exit support and password masking ===
def input_handler(prompt, is_password=False):
    try:
        while True:
            user_input = getpass.getpass(prompt).strip() if is_password else input(prompt).strip()

            if user_input.lower() in ["exit", "quit", "q", "x", "close"]:
                print(f"\n{YELLOW}[i] Exit command detected...{RESET}")
                exit_lockforge()
            elif user_input == "":
                print(f"{RED}[!] Input cannot be empty. Please try again.{RESET}")
            else:
                return user_input
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}[i] Keyboard interrupt detected.{RESET}")
        exit_lockforge()

# === Prompt for file path and return absolute, normalized path ===
def input_file(prompt):
    file_path = input_handler(prompt).strip()

    if not file_path:
        print(f"{RED}[!] No file path provided.{RESET}")
        return None

    file_path = os.path.normpath(file_path)

    if not os.path.isabs(file_path):
        file_path = os.path.abspath(file_path)

    return file_path

# === Encrypt a file with AES and remove the original ===
def encryption():
    file = input_file(f"\n{CYAN}[>] {YELLOW}Enter the full path or name of the file to encrypt: {RESET}")
    if not file or not os.path.isfile(file):
        print(f"{RED}[!] File {WHITE}'{file}'{RED} was not found or is invalid.{RESET}")
        return

    password = input_handler(f"{CYAN}[>] {YELLOW}Enter a password to encrypt the file: {RESET}", is_password=True)
    buffer_size = 64 * 1024

    try:
        pyAesCrypt.encryptFile(file, file + ".aes", password, buffer_size)
        os.remove(file)
        print(f"\n{GREEN}[✓] File {WHITE}'{file}'{GREEN} has been successfully encrypted as {WHITE}'{file}.aes'{GREEN}.{RESET}")
    except Exception as e:
        print(f"{RED}[!] Encryption failed: {e}{RESET}")

# === Decrypt a .aes file using the provided password ===
def decryption():
    file = input_file(f"\n{CYAN}[>] {YELLOW}Enter the full path or name of the encrypted file: {RESET}")
    if not file.endswith(".aes"):
        file += ".aes"
    if not os.path.isfile(file):
        print(f"{RED}[!] File {WHITE}'{file}'{RED} was not found or is invalid.{RESET}")
        return

    password = input_handler(f"{CYAN}[>] {YELLOW}Enter the password to decrypt the file: {RESET}", is_password=True)
    buffer_size = 64 * 1024
    new_file = file.replace(".aes", "")

    try:
        pyAesCrypt.decryptFile(file, new_file, password, buffer_size)
        os.remove(file)
        print(f"\n{GREEN}[✓] File {WHITE}'{file}'{GREEN} has been successfully decrypted as {WHITE}'{new_file}'{GREEN}.{RESET}")
    except Exception as e:
        print(f"{RED}[!] Decryption failed: {e}{RESET}")

# === Display main options to the user and process their choice ===
def choose_option():
    while True:
        print(f"\n{MAGENTA}[★] Please choose one of the following options:{RESET}")
        print(f"{GREEN}[1] {WHITE}Encrypt a file{RESET}")
        print(f"{GREEN}[2] {WHITE}Decrypt a file{RESET}")
        print(f"{GREEN}[3] {WHITE}Exit LockForge{RESET}")
        choice = input_handler(f"{CYAN}[>] {YELLOW}Your choice: {RESET}")

        if choice == '1':
            encryption()
        elif choice == '2':
            decryption()
        elif choice == '3':
            exit_lockforge()
        else:
            print(f"{RED}[!] Invalid option {WHITE}'{choice}'{RED}. Please enter 1, 2, or 3.{RESET}")

# === Entry point: Show intro and launch options menu ===
def main():
    try:
        display_banner()
        display_welcome()

        print(f"\n{CYAN}{'-' * 50}{RESET}")
        choose_option()

    except Exception as e:
        print(f"{RED}[!] An error occurred: {e}{RESET}")
        exit_lockforge()

# === Run the program ===
if __name__ == "__main__":
    main()
