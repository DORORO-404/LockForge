# 🔐 LockForge - Advanced File Encryptor for Terminal

![Project Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python Version](https://img.shields.io/badge/python-3.8+-blue)

**LockForge** is a lightweight, powerful, and easy-to-use file encryption and decryption tool for your terminal.  
Developed in Python, it's perfect for developers, ethical hackers, and Kali Linux users who need quick file protection.

---

## 🚀 About The Project

**LockForge** uses AES encryption (via `pyAesCrypt`) to securely encrypt and decrypt files from the terminal.

It allows users to:

- ✅ Encrypt any file using a strong password
- ✅ Decrypt `.aes` encrypted files
- ✅ Automatically remove original files after encryption/decryption
- ✅ Enjoy a colorful and interactive CLI experience

---

## 🛠 Technologies Used

| Language   | Type     | Dependencies       |
|------------|----------|--------------------|
| Python 3.8+| CLI Tool | `pyAesCrypt`, `colorama`, `pyfiglet`

**Python Modules**:
- `pyAesCrypt` – for AES encryption/decryption
- `pyfiglet` – for banner ASCII art
- `os`, `sys` – for file operations and system exit

---

## 📦 Installation
To install **LockForge** version 1.5.1, follow the steps below:

1. Clone the repository:

    ```bash
    git clone https://github.com/DORORO-404/LockForge.git
    cd LockForge
    ```

2. **Set Up a Virtual Environment (Recommended)**

    For **Linux** / **macOS**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    For **Windows**:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python3 lockforge.py
    ```

5. Exit anytime by typing `exit`, `quit`, `close`, or pressing `CTRL + C`.

## 🖥️ Example Usage

```bash
[+] Welcome to LockForge — Secure. Encrypt. Protect.
[INFO] AES-256 encryption ensures top-level security for your files.
[INFO] LockForge is ready to safeguard your data!
[INFO] Type 'exit', 'quit', 'close', or CTRL + C at any time to exit.
---------------------------------------------------------------------------

[+] What would you like to do?
[1] Encrypt a file
[2] Decrypt a file
[3] Exit LockForge
[INPUT] Enter your choice: 1

[INPUT] Enter the full path or filename to encrypt: file.txt
[INPUT] Enter password to encrypt: 12345678
[INFO] Password accepted.
[INPUT] Confirm password: 12345678

[INFO] Encrypting... Please wait.
[SUCCESS] File encrypted as 'file.txt.aes'

[INPUT] Delete the original file? [Y/n]: y
[SUCCESS] Original file deleted.

[+] What would you like to do?
[1] Encrypt a file
[2] Decrypt a file
[3] Exit LockForge
[INPUT] Enter your choice: 3

[INFO] Exit command received.

[INFO] Exiting LockForge...
[THANK YOU] Thank you for trusting LockForge!
[INFO] Session ended successfully.
```

## 🤝 Contributing

Contributions are always welcome! Here’s how you can contribute:

1. Fork the repository.
2. Create your branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Feel free to open issues for any bugs or feature requests.

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

## 📁 Project Structure
```bash
LockForge/
├── lockforge.py           # Main Python script for file encryption
├── README.md              # Project documentation
├── LICENSE                # MIT License file
└── requirements.txt       # Required Python packages
```
