import os
from tkinter import Tk, filedialog, simpledialog, messagebox, Button, Label
from cryptography.fernet import Fernet


# Generate a key based on user password (not secure key derivation — just for demo)
def generate_key(password: str) -> bytes:
    return Fernet.generate_key()  # Replace with a secure key derivation in production


# Encrypt a file
def encrypt_file(filepath, key):
    try:
        fernet = Fernet(key)
        with open(filepath, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        encrypted_path = filepath + ".enc"
        with open(encrypted_path, 'wb') as enc_file:
            enc_file.write(encrypted)
        messagebox.showinfo("Success", f"File encrypted: {encrypted_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Decrypt a file
def decrypt_file(filepath, key):
    try:
        fernet = Fernet(key)
        with open(filepath, 'rb') as enc_file:
            encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        decrypted_path = filepath.replace(".enc", "") + "_decrypted"
        with open(decrypted_path, 'wb') as dec_file:
            dec_file.write(decrypted)
        messagebox.showinfo("Success", f"File decrypted: {decrypted_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI functions
def encrypt_action():
    filepath = filedialog.askopenfilename()
    if filepath:
        password = simpledialog.askstring("Password", "Enter password for encryption:")
        key = generate_key(password)
        encrypt_file(filepath, key)


def decrypt_action():
    filepath = filedialog.askopenfilename()
    if filepath:
        password = simpledialog.askstring("Password", "Enter password for decryption:")
        key = generate_key(password)
        decrypt_file(filepath, key)


# GUI setup
root = Tk()
root.title("File Encryption/Decryption Tool")
root.geometry("300x200")

Label(root, text="Choose an action:", font=("Arial", 14)).pack(pady=10)
Button(root, text="Encrypt File", command=encrypt_action, width=20).pack(pady=10)
Button(root, text="Decrypt File", command=decrypt_action, width=20).pack(pady=10)

root.mainloop()

