import tkinter as tk
from tkinter import messagebox
import string
import random

def check_pwd(password):
    strength_levels = {
        1: "Very Weak - Change ASAP",
        2: "Weak - Consider changing",
        3: "Moderate - Could be improved",
        4: "Strong - Quite secure",
        5: "Very Strong - Excellent security"
    }
    strength = 0
    counts = {
        'lower': sum(1 for char in password if char.islower()),
        'upper': sum(1 for char in password if char.isupper()),
        'digit': sum(1 for char in password if char.isdigit()),
        'space': sum(1 for char in password if char.isspace()),
        'special': sum(1 for char in password if not char.isalnum() and not char.isspace())
    }

    strength = sum(1 for count in counts.values() if count > 0)
    remarks = strength_levels.get(strength, "Error evaluating password strength")
    return counts, strength, remarks

def update_feedback(*args):
    password = pwd_var.get()
    counts, strength, remarks = check_pwd(password)
    result_text = (f"Lowercase: {counts['lower']}, Uppercase: {counts['upper']}, Digits: {counts['digit']}, "
                   f"Spaces: {counts['space']}, Special: {counts['special']}\n\nStrength: {strength} ({remarks})")
    result_label.config(text=result_text)

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    generated_pwd = ''.join(random.choice(chars) for _ in range(12))
    pwd_var.set(generated_pwd)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(pwd_var.get())
    messagebox.showinfo("Clipboard", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter Password:").pack(pady=(15, 0))
pwd_var = tk.StringVar()
pwd_var.trace_add("write", update_feedback)
pwd_entry = tk.Entry(root, textvariable=pwd_var, show="*", width=40)
pwd_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=(5, 10))

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=(0, 20))

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=(5, 20))

root.mainloop()

