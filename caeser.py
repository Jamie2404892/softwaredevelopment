##import tkinter as tk
##
##root = tk.Tk()
##root.title("encryption")
##root.mainloop()


data = input("data...")
shift = 3


def encrypt(data,key,decrypt):
    if decrypt:
        key = -key
    newdata = ""
    for letter in data:
        newdata = newdata + chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
    return newdata

print(encrypt(data,shift,True))

