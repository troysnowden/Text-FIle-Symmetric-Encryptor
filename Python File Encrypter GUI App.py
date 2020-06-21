import tkinter as tk
import os
from tkinter import filedialog, Text
from cryptography.fernet import Fernet

def chooseEncryptFile():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("Text Files", "*.txt"),("All Files","*.*" )))
    reversedFilename = filename[::-1]
    filename = ""
    for char in reversedFilename:
        if(char == "/"):
            break
        else:
            filename += char
    filename = filename[::-1]
    filesToEncrypt.append(filename)
    for file in filesToEncrypt:
        label = tk.Label(frame,text = file, bg = "gray")
        label.pack()

def encryptFiles():
    key = Fernet.generate_key()

    file = open("key.key", "wb")
    file.write(key)
    file.close()
    
    for file in filesToEncrypt:
        fileWithoutExtension = ""
        for char in file:
            if(char == "."):
                break
            else:
                fileWithoutExtension += char
        file = fileWithoutExtension
        encryptedFile = file + '.encrypted'

        with open(file + '.txt', 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open(encryptedFile, 'wb') as f:
            f.write(encrypted)

        os.remove(file + ".txt")

def chooseDecryptFile():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("Encrypted Files", "*.encrypted"),("All Files","*.*" )))
    reversedFilename = filename[::-1]
    filename = ""
    for char in reversedFilename:
        if(char == "/"):
            break
        else:
            filename += char
    filename = filename[::-1]
    filesToDecrypt.append(filename)
    for file in filesToDecrypt:
        label = tk.Label(frame,text = file, bg = "gray")
        label.pack()

def decryptFiles():
    file = open("key.key", "rb")
    key = file.read()
    
    for file in filesToDecrypt:
        fileWithoutExtension = ""
        for char in file:
            if(char == "."):
                break
            else:
                fileWithoutExtension += char
        file = fileWithoutExtension
        decryptedFile = file + '.decrypted'

        with open(file + '.encrypted', 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.decrypt(data)

        with open(decryptedFile, 'wb') as f:
            f.write(encrypted)

        os.remove(file + ".encrypted")

        
        
    
    
root = tk.Tk() #instantiates a new root window using the tkinter GUI framework
filesToEncrypt = []
filesToDecrypt = []

canvas = tk.Canvas(root, height=700, width=700, bg = "#515485")
canvas.pack()

frame = tk.Frame(root, bg="white")

frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) #adds a frame around the root window


chooseEncryptButton = tk.Button(root, text = "Choose Text Files to Encrypt", padx = 10, pady = 5, fg = "white", bg= "#515485", command = chooseEncryptFile)
chooseEncryptButton.pack()

encryptButton = tk.Button(root, text = "Encrypt Chosen Text Files", padx = 10, pady = 5, fg = "white", bg= "#515485", command = encryptFiles)
encryptButton.pack()

chooseDecryptButton = tk.Button(root, text = "Choose Text Files To Decrypt", padx = 10, pady = 5, fg = "white", bg= "#515485", command = chooseDecryptFile)
chooseDecryptButton.pack()

DecryptButton = tk.Button(root, text = "Decrypt Chosen Text Files", padx = 10, pady = 5, fg = "white", bg= "#515485", command = decryptFiles)
DecryptButton.pack()



root.mainloop()












