import re
import tkinter as tk
from tkinter import messagebox

def check_password():
    password = entry_password.get()
    score = 5
    result = ""

    if len(password) < 8:
        result += "⚠️ Your password is too short. It should be at least 8 characters."
        score -= 1

    if re.search("[A-Z]", password) == None:
        result += "⚠️ Add at least one upper case letter (A-Z) to strengthen your password."
        score -= 1

    if re.search("[a-z]", password) == None:
        result += "⚠️ Include lower case letters (a-z) for better security."
        score -= 1

    if re.search("[0-9]", password) == None:
        result += "⚠️ Consider adding numbers (0-9) to make your password harder to guess."
        score -= 1

    if re.search("[!@#$%^&*()_+=]", password) == None:
        result += "⚠️ Add special characters to boost password strength."
        score -= 1

    result += f"\n🧮 Password strength score: {score} / 5"
    if score < 5:
        result += "🚧 Your password could be stronger. Review the suggestions above and try again."
    else:
        result += "✅ Excellent! Your password is strong. Just Remember to update it regulary."

    messagebox.showinfo("Result", result)

root = tk.Tk()
root.title = "Password Checker"

tk.Label(root, text="Password: ").grid(row=0, column=0, padx=10, pady=10)
entry_password = tk.Entry(root)
entry_password.grid(row=0, column=1, padx=10, pady=5)

btn_check = tk.Button(root, text="Check password", command=check_password)
btn_check.grid(row=1,column=0, columnspan=2, pady=10)

root.mainloop()
