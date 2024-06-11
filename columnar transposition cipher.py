from tkinter import *
import numpy as np

# N  number of columns
# t  transpsition list
# n  length of plaintext
# r  complete rows
# l  number of char in last row

def decryption(text, N, t):
    # Step 2:
    n = len(text)
    # r: floor/integer division of n by N
    r = n // N
    l = n - N * r

    # Step 3:
    columns = N
    if n % N == 0:
        rows = n // N
    else:
        rows = (n // N) + 1

    arr = np.zeros((rows, columns), str)

    # Step 4:
    # counter hold index from beginning of CipherText to the last index on CipherText
    counter = 0

    # l has a value and based on l value determine which column will store all rows on matrix
    # and which one will store rows - 1
    if l > 0:
        for i in t:
            if i < l:
                for rowsValue in range(rows):
                    arr[rowsValue, i] = text[counter]
                    counter += 1
            else:
                for rowsValue in range(rows - 1):
                    arr[rowsValue, i] = text[counter]
                    counter += 1
    # l = 0 (no incomplete rows) and all matrix will store the same number of values in rows
    else:
        for i in t:
            for rowsValue in range(rows):
                arr[rowsValue, i] = text[counter]
                counter += 1

    # Step 5:
    plainText = ''
    for r in range(rows):
        for c in range(columns):
            plainText += arr[r, c]

    return plainText

def encryption(text, N, t):
    # Step 2:
    n = len(text)
    # r: floor/integer division of n by N
    r = n // N

    # Step 3:
    columns = N
    if n % N == 0:
        rows = n // N
    else:
        rows = (n // N) + 1

    arr = np.zeros((rows, columns), str) #create a matrex

    # Step 4:
    # counter hold index from beginning of plainText to the last index on plainText
    counter = 0
    for r in range(rows):
        for c in range(columns):
            if counter == n:
                break
            arr[r, c] = text[counter]
            counter += 1

    # Step 5:
    cipherText = ''
    # i: hold columns values from t to get it and put its value in cipherText
    for i in t:
        # rowsValue: hold rows index based rows value that determined previous in step 3
        for rowsValue in range(rows):
            cipherText += arr[rowsValue, i]
    return cipherText



def decrypt_text():
    text = input_text.get("1.0", END).strip()
    N = int(N_entry.get())
    t_str = transposition_entry.get()  # Get the transposition order as string
    t = [int(x.strip()) for x in t_str.split(',')]  # Convert string to list of integers
    decrypted_text = decryption(text, N, t)
    output_text.delete("1.0", END)
    output_text.insert("1.0", decrypted_text)

def encrypt_text():
    text = input_text.get("1.0", END).strip()
    N = int(N_entry.get())
    t_str = transposition_entry.get()  # Get the transposition order as string
    t = [int(x.strip()) for x in t_str.split(',')]  # Convert string to list of integers
    encrypted_text = encryption(text, N, t)
    output_text.delete("1.0", END)
    output_text.insert("1.0", encrypted_text)

# Create the main application window
root = Tk()
root.title("Encryption and Decryption")

# Create input and output text widgets
input_label = Label(root, text="Input Text:")
input_label.pack(pady=5)

input_text = Text(root, height=5, width=40)
input_text.pack(padx=5, pady=5)

# Create entry for N value
N_label = Label(root, text="N Value:")
N_label.pack(pady=5)

N_entry = Entry(root)
N_entry.pack(padx=5, pady=5)

# Create entry for transposition order
transposition_label = Label(root, text="Transposition (comma separated):")
transposition_label.pack(pady=5)

transposition_entry = Entry(root)
transposition_entry.pack(padx=5, pady=5)

# Create buttons for encryption and decryption
encrypt_button = Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack( padx=5, pady=5)

decrypt_button = Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack( padx=5, pady=5)


# Create output text widget at the bottom of the window
output_label = Label(root, text="Output Text:")
output_label.pack(pady=5)

output_text = Text(root, height=5, width=40)
output_text.pack(padx=5, pady=5)



root.mainloop()