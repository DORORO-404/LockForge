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
- `colorama` – for colorful terminal output
- `pyfiglet` – for banner ASCII art
- `os`, `sys` – for file operations and system exit

---

## 📦 Installation

```bash
git clone https://github.com/DORORO-404/LockForge.git
cd LockForge
pip install -r requirements.txt
python lockforge.py
```

## 🖥️ Example Usage

```bash
[+] ===== Welcome to LockForge - Secure Your Files with Ease! ===== [+]

[1] Encrypt a File
[2] Decrypt a File
[3] Exit LockForge
>> Choose an option: 1
Enter the name of the file you want to encrypt: File.txt
Enter a password to encrypt the file: dororo
Success: File 'File.txt' has been encrypted successfully as 'File.txt.aes'.
[1] Encrypt a File
[2] Decrypt a File
[3] Exit LockForge
>> Choose an option: 2
Enter the name of the encrypted file (.aes): File.txt.aes
Enter the password to decrypt the file: dororo
Success: File 'File.txt.aes' has been decrypted successfully as 'File.txt'.
[1] Encrypt a File
[2] Decrypt a File
[3] Exit LockForge
>> Choose an option: 3

Exiting LockForge... Thank you for using LockForge!
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