COMPANY : CODE IT SOLUTIONS

NAME : SANGABATTUNI AAKASH

INTERN ID : CTIS8970

DOMAIN : CYBERSECURITY AND ETHICAL HACKING

DURATION : 8 WEEKS

INTERNSHIP PERIOD : 17 May 2026 - 12 July 2026

MENTOR : Neela Santhosh Kumar

### A TOOL TO ENCRYPT ANDDECRYPT FILES USING ADVANCEDALGORITHMS LIKE AES-256
#A ROBUST
ENCRYPTION APPLICATION WITH AUSER-FRIENDLY INTERFACE.

🔒 AES‑256 File Encryption Tool (GUI):

A Python application with a Tkinter GUI that allows users to encrypt and decrypt files using AES‑256 (GCM mode).
This tool is designed for secure file handling with password‑based encryption.


🚀 Features:

AES‑256 Encryption (GCM mode) for strong security.

Password‑based key derivation using PBKDF2 with SHA‑256.

File encryption with .enc extension output.

File decryption with _decrypted suffix output.

Simple GUI built with Tkinter:

Select files via file dialog.

Enter password securely.

Encrypt or decrypt multiple files at once.

Success/Error pop‑ups for user feedback.

🛠️ How It Works:

Key Derivation

Password + random salt → PBKDF2 → 256‑bit key.

Encryption

AES‑256 in GCM mode with random IV.

Output file contains: salt + iv + tag + ciphertext.

Decryption

Reads salt, IV, and tag from encrypted file.

Reconstructs key and decrypts ciphertext.

Saves output with _decrypted suffix.

GUI Workflow

Enter password → Select files → Click Encrypt or Decrypt → Get results.

📦 Requirements:
Python 3.7+

Install dependencies like cryptography tool


GUI will open:

Enter a password.

Click Encrypt Files → select files → encrypted versions saved with .enc.

Click Decrypt Files → select .enc files → decrypted versions saved with _decrypted.

📁 Project Structure:

aes-encryption-tool/
│── aes_tool.py         # Main script with GUI
│── README.md           # Documentation


⚠️ Notes
Always remember your password — without it, files cannot be decrypted.

Encrypted files are saved with .enc extension.

Decrypted files are saved with _decrypted suffix.

This tool is for personal and educational use.

Do not use weak passwords — prefer long, complex ones.

OUTPUT1- WHEN PROGRAM RUN AND IT"S FIRST INITIAL STEP 1:
OUTPUT2- WHEN THE PROGRAM IS ENCRYPTED IT APPEARS WITH .enc EXTENSION:
<img width="1920" height="1200" alt="Image" src="https://github.com/user-attachments/assets/1759e27f-5196-4f58-a823-f5e2269ccec7" />
