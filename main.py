import tkinter as tk
from tkinter import messagebox
from Primary_Functions import *
from User import *

print("Welcome to Python Secure(ish) Storage!")
print("By Henry F.")
root = tk.Tk()
root.title("Python Storage")
root.geometry("600x400")
tk.Label(root, text="Welcome to Python Secure(ish) Storage by Henry F.").pack()
messagebox.showinfo("Success", f"Created")

# --- Frames (Screens) ---
login_frame = tk.Frame(root)
newaccount_row1 = tk.Frame(root)
newaccount_row2 = tk.Frame(root)
newaccount_row3 = tk.Frame(root)
newaccount_row4 = tk.Frame(root)

menu_frame = tk.Frame(root)
about_frame = tk.Frame(root)
login_frame.pack()
#for frame in (login_frame, menu_frame):
#    frame.place(relwidth=1, relheight=1)
#def show_frame(frame):
 #   frame.tkraise()

# END
def create_account_frame_start():
    login_frame.pack_forget()
    newaccount_row1.pack()
    newaccount_row2.pack()
    newaccount_row3.pack()
    newaccount_row4.pack()
def create_account_button():
    username = newacountusername.get()   # Make this lower
    password1 = newacountpassword1.get()
    password2 = newacountpassword2.get()
    print(f"You typed: {username}, {password1}, {password2}")
    if password1 == password2:
        user_obj = User(username, password1)
        messagebox.showinfo("Success", f"Account ({username}) Created")
    else: messagebox.showerror("Error", "Incorrect password.")
    

    save_user(user_obj)
#  Login_Frame
tk.Label(login_frame, text="Log in  ").pack(side="left")
tk.Button(login_frame, text="or Create Acount", command=create_account_frame_start).pack(pady=5)
# New acount frame
tk.Label(newaccount_row1, text="Enter your new username  ").pack(side="left")
newacountusername = tk.Entry(newaccount_row1).pack(side="right")
tk.Label(newaccount_row2, text="Enter same password  ").pack(side="left")
newacountpassword1 = tk.Entry(newaccount_row2).pack()
tk.Label(newaccount_row3, text="Enter same password  ").pack(side="left")
newacountpassword2 = tk.Entry(newaccount_row3).pack()
tk.Button(newaccount_row4, text="Go", command=create_account_button).pack(pady=5)














root.mainloop()