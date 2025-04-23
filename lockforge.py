# ========= LockForge - Advanced File Encryptor =========

# === Import Modules ===
import os
import sys
import pyAesCrypt
import pyfiglet
from colorama import Fore, Style, init

# === Initialize Colorama ===
init(autoreset=True)

# === Program Info ===
VERSION = "1.0"

# === Color Shortcuts ===
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

# === Display ASCII Banner ===
def display_banner():
    banner = pyfiglet.figlet_format("LockForge")
    print(f"{CYAN}{banner}{RESET}")
    print(f"""{CYAN}
╔════════════════════════════════════════════╗
║   {MAGENTA}LockForge - AES File Encryptor{CYAN}           ║
║   {MAGENTA}By: DORORO__404   |  Version: v{VERSION}  {CYAN}     ║
╚════════════════════════════════════════════╝{RESET}""")

# === Display Welcome Message ===
def display_welcome():
    print(f"\n{GREEN}[★] Welcome to {MAGENTA}LockForge{GREEN} — Secure. Encrypt. Protect.{RESET}")
    print(f"{YELLOW}[i] AES-256 encryption ensures top-level security for your files.{RESET}")
    print(f"{YELLOW}[i] LockForge is ready to secure your files.{RESET}")

# === Safe Exit ===
def exit_lockforge():
    print(f"\n{GREEN}[*] Exiting LockForge...{RESET}")
    print(f"{MAGENTA}[!] Thank you for using LockForge!{RESET}")
    print(f"{YELLOW}[i] Your session has been successfully closed.\n{RESET}")
    sys.exit()

# === Input Handler with Exit Options ===
def input_with_exit(prompt):
    try:
        while True:
            user_input = input(prompt).strip()
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

# === File Encryption ===
def encryption():
    file_name = input_with_exit(f"\n{CYAN}[>] {YELLOW}Enter the name of the file you want to encrypt: {RESET}")
    if not os.path.isfile(file_name):
        print(f"{RED}[!] File {WHITE}'{file_name}'{RED} not found.{RESET}")
        return

    password = input_with_exit(f"{CYAN}[>] {YELLOW}Enter a password to encrypt the file: {RESET}")
    buffer_size = 64 * 1024

    try:
        pyAesCrypt.encryptFile(file_name, file_name + ".aes", password, buffer_size)
        os.remove(file_name)
        print(f"\n{GREEN}[✓] File {WHITE}'{file_name}'{GREEN} has been encrypted as {WHITE}'{file_name}.aes'{GREEN}.{RESET}")
    except Exception as e:
        print(f"{RED}[!] Encryption failed: {e}{RESET}")

# === File Decryption ===
def decryption():
    file_name = input_with_exit(f"\n{CYAN}[>] {YELLOW}Enter the name of the encrypted file (.aes): {RESET}")
    if not os.path.isfile(file_name):
        print(f"{RED}[!] File {WHITE}'{file_name}'{RED} not found.{RESET}")
        return

    password = input_with_exit(f"{CYAN}[>] {YELLOW}Enter the password to decrypt the file: {RESET}")
    buffer_size = 64 * 1024
    new_file = file_name.replace(".aes", "")

    try:
        pyAesCrypt.decryptFile(file_name, new_file, password, buffer_size)
        os.remove(file_name)
        print(f"\n{GREEN}[✓] File {WHITE}'{file_name}'{GREEN} has been decrypted as {WHITE}'{new_file}'{GREEN}.{RESET}")
    except Exception as e:
        print(f"{RED}[!] Decryption failed: {e}{RESET}")

# === Choose Option ===
def choose_option():
    while True:
        print(f"\n{MAGENTA}[★] Please choose one of the following options:{RESET}")
        print(f"{GREEN}[1] {WHITE}Encrypt a File.{RESET}")
        print(f"{GREEN}[2] {WHITE}Decrypt a File.{RESET}")
        print(f"{GREEN}[3] {WHITE}Exit LockForge.{RESET}")
        choice = input_with_exit(f"{CYAN}[>] {YELLOW}Choose an option: {RESET}")

        if choice == '1':
            encryption()
        elif choice == '2':
            decryption()
        elif choice == '3':
            exit_lockforge()
        else:
            print(f"{RED}[!] Invalid option {WHITE}'{choice}'{RED}. Please choose a valid option (1, 2, or 3).{RESET}")

# === Main Function ===
def main():
    try:
        display_banner()
        display_welcome()

        line = "-" * 50
        print(f"\n{CYAN}{line}{RESET}")

        choose_option()

    except Exception as e:
        print(f"{RED}[!] An error occurred: {e}{RESET}")
        exit_lockforge()

# === Entry Point ===
if __name__ == "__main__":
    main()
