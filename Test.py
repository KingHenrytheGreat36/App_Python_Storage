import tkinter as tk
from tkinter import messagebox
from User import *
root = tk.Tk()
root.title("Tkinter Test!")
root.geometry("400x200")

tk.Label(root, text="Username:").pack()

username_entry = tk.Entry(root)
username_entry.pack()

def login():
    username = username_entry.get()
    print("You typed:", username)
    print(Hash("HFadmin", "asdf"))

tk.Button(root, text="Login", command=login).pack(pady=10)
res1 = messagebox.showinfo("Info", "This is an info box.")
res2 = messagebox.showwarning("Warning", "This is a warning box.")
res3 = messagebox.showerror("Error", "This is an error box.")

# 2. Boolean Questions
res4 = messagebox.askyesno("Yes/No", "Click Yes or No.")
res5 = messagebox.askokcancel("OK/Cancel", "Click OK or Cancel.")
res6 = messagebox.askretrycancel("Retry/Cancel", "Click Retry or Cancel.")

# 3. Special Questions
res7 = messagebox.askyesnocancel("Three-way", "Click Yes, No, or Cancel.")
res8 = messagebox.askquestion("Legacy Question", "Click Yes or No string.")

# Print all outputs to see how Python registers your clicks
print(res1, res2, res3, res4, res5, res6, res7, res8)
root.mainloop()
