import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(file_path, password):
    try:
        salt = os.urandom(16)
        key = derive_key(password, salt)
        iv = os.urandom(12)
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        with open(file_path, 'rb') as f:
            plaintext = f.read()

        ciphertext = encryptor.update(plaintext) + encryptor.finalize()

        with open(file_path + ".enc", 'wb') as f:
            f.write(salt + iv + encryptor.tag + ciphertext)

        messagebox.showinfo("Success", f"Encrypted: {file_path}.enc")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")

def decrypt_file(file_path, password):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        salt, iv, tag, ciphertext = data[:16], data[16:28], data[28:44], data[44:]
        key = derive_key(password, salt)
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()

        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

        # Always write to a new file with "_decrypted" suffix
        base_name = file_path.replace(".enc", "")
        decrypted_file = base_name + "_decrypted"

        with open(decrypted_file, 'wb') as f:
            f.write(decrypted_data)

        messagebox.showinfo("Success", f"Decrypted: {decrypted_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")

def select_files_encrypt():
    files = filedialog.askopenfilenames()
    password = password_entry.get()
    if files and password:
        for file in files:
            encrypt_file(file, password)
    else:
        messagebox.showerror("Error", "Select files and enter a password!")

def select_files_decrypt():
    files = filedialog.askopenfilenames()
    password = password_entry.get()
    if files and password:
        for file in files:
            decrypt_file(file, password)
    else:
        messagebox.showerror("Error", "Select files and enter a password!")

root = tk.Tk()
root.title("AES-256 Encryption Tool")
root.geometry("400x250")

tk.Label(root, text="Enter Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt Files", command=select_files_encrypt)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt Files", command=select_files_decrypt)
decrypt_button.pack(pady=10)

root.mainloop()
