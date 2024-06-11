import tkinter as tk

def encrypt(text, key):
    encrypted_text = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index].lower()) - ord('a')
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ''
    key_index = 0
    for char in encrypted_text:
        if char.isalpha():
            shift = ord(key[key_index].lower()) - ord('a')
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_button_click():
    key = key_entry.get()
    plaintext = plaintext_entry.get("1.0", tk.END).strip()
    encrypted_text = encrypt(plaintext, key)
    encrypted_text_result.config(state=tk.NORMAL)
    encrypted_text_result.delete("1.0", tk.END)
    encrypted_text_result.insert(tk.END, encrypted_text)
    encrypted_text_result.config(state=tk.DISABLED)

def decrypt_button_click():
    key = key_entry.get()
    encrypted_text = encrypted_text_result.get("1.0", tk.END).strip()
    decrypted_text = decrypt(encrypted_text, key)
    decrypted_text_result.config(state=tk.NORMAL)
    decrypted_text_result.delete("1.0", tk.END)
    decrypted_text_result.insert(tk.END, decrypted_text)
    decrypted_text_result.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("Polyalphabetic Cipher")

# Key input
key_label = tk.Label(root, text="Key:")
key_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
key_entry = tk.Entry(root)
key_entry.grid(row=0, column=1, padx=5, pady=5)

# Plaintext input
plaintext_label = tk.Label(root, text="Plaintext:")
plaintext_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
plaintext_entry = tk.Text(root, height=5, width=30)
plaintext_entry.grid(row=1, column=1, padx=5, pady=5)

# Encrypted text output
encrypted_text_label = tk.Label(root, text="Encrypted Text:")
encrypted_text_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
encrypted_text_result = tk.Text(root, height=5, width=30)
encrypted_text_result.grid(row=2, column=1, padx=5, pady=5)
encrypted_text_result.config(state=tk.DISABLED)

# Decrypted text output
decrypted_text_label = tk.Label(root, text="Decrypted Text:")
decrypted_text_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
decrypted_text_result = tk.Text(root, height=5, width=30)
decrypted_text_result.grid(row=3, column=1, padx=5, pady=5)
decrypted_text_result.config(state=tk.DISABLED)

# Encrypt and Decrypt buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_button_click)
encrypt_button.grid(row=4, column=0, padx=5, pady=5)
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_button_click)
decrypt_button.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()
