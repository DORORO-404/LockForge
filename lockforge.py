# ========= LockForge - Advanced File Encryptor =========

# === Safe Import Modules ===
try:
    import os
    import sys
    import getpass
    import pyAesCrypt
    import pyfiglet
    from colorama import Fore, Style, init
except ImportError as e:
    missing = str(e).split("'")[1]
    print(f"\n[!] Missing module: '{missing}'")
    print("[-] Please install all dependencies before running LockForge.")
    print("[*] Required: pyAesCrypt, pyfiglet, colorama")
    print("[+] You can install them using:")
    print("[i] pip install pyAesCrypt pyfiglet colorama\n")
    sys.exit(1)

# === Initialize Colorama ===
init(autoreset=True, strip=False, convert=True)

# === Version Info ===
VERSION = "1.4"

# === Color Shortcuts ===
RED, GREEN, YELLOW = Fore.RED, Fore.GREEN, Fore.YELLOW
BLUE, MAGENTA, CYAN = Fore.BLUE, Fore.MAGENTA, Fore.CYAN
WHITE, RESET = Fore.WHITE, Style.RESET_ALL

# === Display ASCII banner ===
def display_banner():
    banner = pyfiglet.figlet_format("LockForge")
    print(f"{MAGENTA}{banner}{RESET}")
    print(f"""{CYAN}
╔════════════════════════════════════════════╗
║   {MAGENTA}LockForge - AES File Encryptor{CYAN}           ║
║   {MAGENTA}By: DORORO__404   |  Version: v{VERSION}  {CYAN}     ║
╚════════════════════════════════════════════╝{RESET}
""")

# === Display welcome message ===
def display_welcome():
    print(f"\n{MAGENTA}[+] {GREEN}Welcome to {MAGENTA}LockForge{GREEN} — Secure. Encrypt. Protect.{RESET}")
    print(f"{YELLOW}[i] {CYAN}AES-256 encryption ensures top-level security for your files.{RESET}")
    print(f"{YELLOW}[i] {CYAN}LockForge is ready to safeguard your data!{RESET}")
    print(f"{YELLOW}[i] Type '{CYAN}exit{YELLOW}', '{CYAN}quit{YELLOW}', '{CYAN}close{YELLOW}', or {CYAN}CTRL + C{YELLOW} at any time to exit.{RESET}")
    print(f"{CYAN}{'-' * 75}{RESET}")

# === Exit gracefully ===
def exit_lockforge():
    print(f"\n{GREEN}[*] Exiting LockForge...{RESET}")
    print(f"{MAGENTA}[!] Thank you for trusting LockForge!{RESET}")
    print(f"{YELLOW}[i] Session ended successfully.\n{RESET}")
    sys.exit()

# === Input handler with exit keywords ===
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

# === Get and validate file path ===
def input_file(message):
    file_path = input_handler(message).strip()
    if not file_path:
        print(f"{RED}[!] No file path provided.{RESET}")
        return None
    return os.path.abspath(os.path.normpath(file_path))

# === Confirm file deletion ===
def confirm_deletion(file):
    if not os.path.isfile(file):
        print(f"{RED}[!] File '{WHITE}{file}{RED}' not found or invalid.{RESET}")
        return False
    confirm = input_handler(f"{YELLOW}[?] Delete the original file? [Y/n]: {RESET}").lower()
    if confirm in ['y', 'yes', '']:
        try:
            os.remove(file)
            print(f"{GREEN}[✓] Original file deleted.{RESET}")
            return True
        except Exception as e:
            print(f"{RED}[!] Error while deleting the file: {e}{RESET}")
            return False
    else:
        print(f"{YELLOW}[i] Original file was kept.{RESET}")
        return False

# === Encrypt file ===
def encryption():
    file = input_file(f"\n{CYAN}[>] Enter the full path or filename to encrypt: {RESET}")
    if not file or not os.path.isfile(file):
        print(f"{RED}[!] File '{WHITE}{file}{RED}' not found or invalid.{RESET}")
        return

    while True:
        password = input_handler(f"{CYAN}[>] Enter password to encrypt: {RESET}", is_password=True)
        if len(password) < 8:
            print(f"{RED}[!] Password must be at least 8 characters.{RESET}")
            continue
        print(f"{YELLOW}[i] Password accepted.{RESET}")
        confirm_password = input_handler(f"{CYAN}[>] Confirm password: {RESET}", is_password=True)
        if password == confirm_password:
            break
        else:
            print(f"{RED}[!] Passwords do not match. Try again.{RESET}")

    try:
        print(f"\n{YELLOW}[i] Encrypting... Please wait.{RESET}")
        pyAesCrypt.encryptFile(file, file + ".aes", password, 64 * 1024)
        print(f"{GREEN}[✓] File encrypted as '{WHITE}{file}.aes{GREEN}'{RESET}\n")
        confirm_deletion(file)
    except Exception as e:
        print(f"{RED}[!] Encryption failed: {e}{RESET}")

# === Decrypt file ===
def decryption():
    file = input_file(f"\n{CYAN}[>] Enter the full path or filename to decrypt: {RESET}")
    if not file.endswith(".aes"):
        file += ".aes"
    if not os.path.isfile(file):
        print(f"{RED}[!] File '{WHITE}{file}{RED}' not found or invalid.{RESET}")
        return

    password = input_handler(f"{CYAN}[>] Enter password to decrypt: {RESET}", is_password=True)
    new_file = file.replace(".aes", "")

    try:
        print(f"\n{YELLOW}[i] Decrypting... Please wait.{RESET}")
        pyAesCrypt.decryptFile(file, new_file, password, 64 * 1024)
        print(f"{GREEN}[✓] File decrypted as '{WHITE}{new_file}{GREEN}'{RESET}\n")
        confirm_deletion(file)
    except Exception as e:
        print(f"{RED}[!] Decryption failed: {e}{RESET}")

# === Menu options ===
def choose_option():
    while True:
        print(f"\n{MAGENTA}[+] {GREEN}What would you like to do?{RESET}")
        print(f"{GREEN}[1] 🔒 {WHITE}Encrypt a file{RESET}")
        print(f"{GREEN}[2] 🔓 {WHITE}Decrypt a file{RESET}")
        print(f"{GREEN}[3] 🚪 {WHITE}Exit LockForge{RESET}")
        choice = input_handler(f"{CYAN}[>] Enter your choice: {RESET}")

        if choice == '1':
            encryption()
        elif choice == '2':
            decryption()
        elif choice == '3':
            print(f"\n{YELLOW}[i] Exit command received.{RESET}")
            exit_lockforge()
        else:
            print(f"{RED}[!] Invalid option '{WHITE}{choice}{RED}'. Choose 1, 2, or 3.{RESET}")

# === Show version and exit if requested ===
def show_version():
    if "--version" in sys.argv:
        print(f"{CYAN}[•] LockForge Version: {VERSION}{RESET}")
        sys.exit()

# === Main function ===
def main():
    show_version()
    try:
        display_banner()
        display_welcome()
        choose_option()
    except Exception as e:
        print(f"{RED}[!] An unexpected error occurred: {e}{RESET}")
        exit_lockforge()

# === Entry Point ===
if __name__ == "__main__":
    main()
