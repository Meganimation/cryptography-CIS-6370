
from tkinter import *
from tkinter import filedialog, messagebox
import os
import json
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

KEY_FILE = "hybrid_keys.json"
DATA_FILE = "hybrid_data.json"

def home(root, username):
    landing_frame = Frame(root, bg="black")
    landing_frame.pack(fill="both", expand=True)
    welcome_label = Label(landing_frame, text=f"Welcome, {username}!", fg="green", bg="black")
    welcome_label.pack(pady=10)

    # Table header
    table_frame = Frame(landing_frame, bg="black")
    table_frame.pack(pady=10)
    Label(table_frame, text="Filename", fg="green", bg="black", width=30).grid(row=0, column=0)
    Label(table_frame, text="File Type", fg="green", bg="black", width=20).grid(row=0, column=1)
    Label(table_frame, text="Action", fg="green", bg="black", width=15).grid(row=0, column=2)

    files = []  # List of dicts: {filename, filetype, filepath, encrypted, ciphertext, public_key}

    # Load previous data if exists
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            files = json.load(f)

    def save_files():
        # Only store safe info (no private key)
        with open(DATA_FILE, "w") as f:
            json.dump(files, f)

    def refresh_table():
        # Remove all rows except header
        for widget in table_frame.winfo_children():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()
        for idx, fileinfo in enumerate(files):
            Label(table_frame, text=fileinfo["filename"], fg="white", bg="black", width=30).grid(row=idx+1, column=0)
            Label(table_frame, text=fileinfo["filetype"], fg="white", bg="black", width=20).grid(row=idx+1, column=1)
            btn = Button(table_frame, text="Actions", command=lambda i=idx: decrypt_file(i))
            btn.grid(row=idx+1, column=2)

    def add_file():
        filepath = filedialog.askopenfilename()
        if not filepath:
            return
        filename = os.path.basename(filepath)
        filetype = os.path.splitext(filename)[1][1:] or "Unknown"
        aes_key = get_random_bytes(32)  # 256 bits
        with open(filepath, "rb") as f:
            plaintext = f.read()
        cipher_aes = AES.new(aes_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(plaintext)
        key = RSA.generate(2048)
        public_key = key.publickey().export_key().decode()
        private_key = key.export_key().decode()
        cipher_rsa = PKCS1_OAEP.new(key.publickey())
        enc_aes_key = cipher_rsa.encrypt(aes_key)
        file_entry = {
            "filename": filename,
            "filetype": filetype,
            "filepath": filepath,
            "encrypted": True,
            "ciphertext": base64.b64encode(ciphertext).decode(),
            "tag": base64.b64encode(tag).decode(),
            "nonce": base64.b64encode(cipher_aes.nonce).decode(),
            "enc_aes_key": base64.b64encode(enc_aes_key).decode(),
            "public_key": public_key
        }
        files.append(file_entry)
        save_files()
        refresh_table()

        def show_private_key():
            win = Toplevel(root)
            win.title("Your Private Key")
            win.configure(bg="black")
            Label(win, text="Save this RSA Private Key to decrypt your file!", fg="red", bg="black").pack(pady=5)
            text = Text(win, width=60, height=10, bg="black", fg="white")
            text.insert(END, private_key)
            text.pack(pady=5)
            def copy_key():
                root.clipboard_clear()
                root.clipboard_append(private_key)
                messagebox.showinfo("Copied", "Private key copied to clipboard!")
            def save_key():
                path = filedialog.asksaveasfilename(defaultextension=".pem", initialfile="private_key.pem")
                if path:
                    with open(path, "w") as f:
                        f.write(private_key)
                    messagebox.showinfo("Saved", f"Private key saved to {path}")
            Button(win, text="Save Key to File", command=save_key).pack(pady=5)
            Button(win, text="Copy to Clipboard", command=copy_key).pack(pady=5)
        show_private_key()
        messagebox.showinfo("Success", f"File '{filename}' encrypted and added. Your private key will now be shown. You must save it to decrypt later!")

    def decrypt_file(idx):
        fileinfo = files[idx]
        privkey_win = Toplevel(root)
        privkey_win.title("Enter Private Key")
        privkey_win.configure(bg="black")
        Label(privkey_win, text="Paste your RSA Private Key:", fg="green", bg="black").pack(pady=5)
        privkey_text = Text(privkey_win, width=60, height=10, bg="black", fg="white")
        privkey_text.pack(pady=5)
        def do_delete():
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{fileinfo['filename']}'? This action cannot be undone."):
                files.pop(idx)
                save_files()
                refresh_table()
                privkey_win.destroy()        

        def do_decrypt():
            privkey_str = privkey_text.get("1.0", END).strip()
            try:
                privkey = RSA.import_key(privkey_str)
                cipher_rsa = PKCS1_OAEP.new(privkey)
                aes_key = cipher_rsa.decrypt(base64.b64decode(fileinfo["enc_aes_key"]))
                cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=base64.b64decode(fileinfo["nonce"]))
                plaintext = cipher_aes.decrypt_and_verify(
                    base64.b64decode(fileinfo["ciphertext"]),
                    base64.b64decode(fileinfo["tag"])
                )
                # Save decrypted file
                save_path = filedialog.asksaveasfilename(defaultextension="", initialfile=fileinfo["filename"])
                if save_path:
                    with open(save_path, "wb") as f:
                        f.write(plaintext)
                    messagebox.showinfo("Success", f"File decrypted and saved as '{save_path}'.")
                privkey_win.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Decryption failed: {e}")

        Button(privkey_win, text="Decrypt", command=do_decrypt).pack(pady=5)
        Button(privkey_win, text="Delete", command=do_delete).pack(pady=5)
        Button(privkey_win, text="Cancel", command=privkey_win.destroy).pack(pady=5)

    add_file_btn = Button(landing_frame, text="Add File", command=add_file)
    add_file_btn.pack(pady=10)

    refresh_table()
    