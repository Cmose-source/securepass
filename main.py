import re
import hashlib
from getpass import getpass
import tkinter as tk

def checker_password(password):
    if len(password) < 8:
        return "Must be 8 letters"
    if not re.search(r"[A-Z]", password):
        return "Have to be uppercase"
    if not re.search(r"[0-9]", password):
        return "Must use a digit number"
    if not re.search(r"[!@#$%&*]", password):
        return "You have to add symbol"
    return "Strong!"

def encrypt(password):
    return hashlib.sha256(password.encode()).hexdigest()

def copy_to_clipboard(text):
    clipboard = tk.Tk()
    clipboard.withdraw()  
    clipboard.clipboard_clear()  
    clipboard.clipboard_append(text)  
    clipboard.update()  
    clipboard.destroy()  
    
user_pass = getpass("Put your password here! ")
result = checker_password(user_pass)
print(result)

if result == "Strong!":
    option = input("Do you want to encrypt the password (Y/n) ").strip().lower()
    if option in ['y', '']:
        encrypted = encrypt(user_pass)
        print(encrypted)
        copy_to_clipboard(encrypted)
        print("It has been copied into clipboard")
    else:
        print("Thanks for using this tools!")




    
