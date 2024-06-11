import tkinter as tk

def caesar_cipher(text, s, encrypt=True):
    if not encrypt:  # If decrypting, adjust the key
        s = 26 - s
    
    result = ""  # Empty string
    for char in text:
        if char.isalpha():  # Only process alphabetic characters
            if char.isupper():  # If the character is uppercase
                result += chr((ord(char) + s - 65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char  # Keep spaces and non-alphabetic characters unchanged
    return result

def process_text():
    word = entry_text.get()
    key = int(entry_key.get())
    is_encrypt = algorithms_list.curselection()[0]  # Get the selected index
    result = caesar_cipher(word, key, is_encrypt)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("600x600")
root.configure(bg="#E5E5E5")

# Create input widgets
label_text = tk.Label(root, text="Enter the text:")
label_text.pack(pady=10)  # Add vertical padding

entry_text = tk.Entry(root)
entry_text.pack(pady=5)  # Add vertical padding

label_key = tk.Label(root, text="Enter the key:")
label_key.pack(pady=10)  # Add vertical padding

entry_key = tk.Entry(root)
entry_key.pack(pady=5)  # Add vertical padding

# Create output widget
output_text = tk.Text(root, height=5, width=30)

# Create ListBox for selecting encryption or decryption
algorithms_list = tk.Listbox(root, selectmode=tk.SINGLE)
algorithms_list.insert(1, "Decrypt")
algorithms_list.insert(2, "Encrypt")
algorithms_list.pack(pady=5)  # Add vertical padding

# Create button
process_button = tk.Button(root, text="Process", command=process_text)
process_button.pack(pady=10)  # Add vertical padding

output_text.pack(pady=10) # Add vertical padding

# Run the application
root.mainloop()