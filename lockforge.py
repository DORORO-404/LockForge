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
╔═══════════════════════════════════════╗
║     {MAGENTA}LockForge - File Encryptor{CYAN}        ║
║     {MAGENTA}Developer   : DORORO__404{CYAN}         ║
║     {MAGENTA}GitHub      : DORORO-404{CYAN}          ║
║     {MAGENTA}Version     : {VERSION}{CYAN}                 ║
╚═══════════════════════════════════════╝{RESET}
""")

# === Display Welcome Message ===
def display_welcome():
    print(f"{BLUE}[+] ===== {CYAN}Welcome to LockForge - Secure Your Files with Ease!{BLUE} ===== [+]{RESET}\n")

# === Safe Exit ===
def exit_lockforge():
    print(f"\n{GREEN}Exiting LockForge... Thank you for using LockForge!{RESET}")
    sys.exit()

# === File Encryption ===
def encryption():
    file_name = input(f"{GREEN}Enter the name of the file you want to encrypt: {RESET}")
    if not os.path.isfile(file_name):
        print(f"{RED}Error: File '{file_name}' not found.{RESET}")
        return

    password = input(f"{GREEN}Enter a password to encrypt the file: {RESET}")
    buffer_size = 64 * 1024

    try:
        pyAesCrypt.encryptFile(file_name, file_name + ".aes", password, buffer_size)
        os.remove(file_name)
        print(f"{GREEN}Success: File '{file_name}' has been encrypted successfully as '{file_name}.aes'.{RESET}")
    except Exception as e:
        print(f"{RED}Encryption failed: {e}{RESET}")

# === File Decryption ===
def decryption():
    file_name = input(f"{GREEN}Enter the name of the encrypted file (.aes): {RESET}")
    if not os.path.isfile(file_name):
        print(f"{RED}Error: File '{file_name}' not found.{RESET}")
        return

    password = input(f"{GREEN}Enter the password to decrypt the file: {RESET}")
    buffer_size = 64 * 1024
    output_file = file_name.replace(".aes", "")

    try:
        pyAesCrypt.decryptFile(file_name, output_file, password, buffer_size)
        os.remove(file_name)
        print(f"{GREEN}Success: File '{file_name}' has been decrypted successfully as '{output_file}'.{RESET}")
    except Exception as e:
        print(f"{RED}Decryption failed: {e}{RESET}")

# === Choose Option ===
def choose_option():
    while True:
        print(f"{YELLOW}[1] Encrypt a File{RESET}")
        print(f"{YELLOW}[2] Decrypt a File{RESET}")
        print(f"{YELLOW}[3] Exit LockForge{RESET}")
        choice = input(f"{CYAN}>> Choose an option: {RESET}")

        if choice == '1':
            encryption()
        elif choice == '2':
            decryption()
        elif choice == '3':
            exit_lockforge()
        else:
            print(f"{RED}Invalid option. Please select 1, 2, or 3.{RESET}\n")

# === Main Function ===
def main():
    display_banner()
    display_welcome()
    choose_option()

# === Entry Point ===
if __name__ == "__main__":
    main()
