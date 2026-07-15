import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test!")
root.geometry("400x200")

tk.Label(root, text="Username:").pack()

username_entry = tk.Entry(root)
username_entry.pack()

def login():
    username = username_entry.get()
    print("You typed:", username)

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
