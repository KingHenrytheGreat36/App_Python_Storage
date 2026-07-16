import tkinter as tk
from tkinter import messagebox
from Primary_System import *
from User import *

root = tk.Tk()
root.title("Python Storage")
root.geometry("450x400")
tk.Label(root, text="Welcome to Python Secure(ish) Storage by Henry F.").pack()

#region --- Frames (Screens) ---
login_frame = tk.Frame(root)
login_row1 = tk.Frame(login_frame)
login_row2 = tk.Frame(login_frame)
login_row3 = tk.Frame(login_frame)
for row in (login_row1, login_row2, login_row3):
    row.pack()

newaccount_frame = tk.Frame(root)
newaccount_row1 = tk.Frame(newaccount_frame)
newaccount_row2 = tk.Frame(newaccount_frame)
newaccount_row3 = tk.Frame(newaccount_frame)
newaccount_row4 = tk.Frame(newaccount_frame)
for row in (newaccount_row1, newaccount_row2, newaccount_row3, newaccount_row4):
    row.pack()

login_frame.pack()

#endregion

def create_account_frame_start():
    login_frame.pack_forget()
    newaccount_frame.pack()
def SysEnter(user_obj):
    root.withdraw()   # hide window
    restart = MainSystem(user_obj)
    if restart == True:
        root.deiconify()  # show window again
        login_row1.pack()
        login_row2.pack()
        login_row3.pack()
    else: 
        exit()

def create_account_button():
    username = newacountusername.get()   # Make this lower
    password1 = newacountpassword1.get()
    password2 = newacountpassword2.get()
    if password1.lower() == password2.lower():
        user_obj = User(username.lower(), password1.lower())
        save_user(user_obj)

        messagebox.showinfo("Success", f"Account ({username}) Created")
        newaccount_row1.pack_forget()
        newaccount_row2.pack_forget()
        newaccount_row3.pack_forget()
        newaccount_row4.pack_forget()
        SysEnter(user_obj)
    else: messagebox.showerror("Incorrect Password", "Try again")
    
def login_button():
    username = loginusernamebox.get()
    password = loginpasswordbox.get()
    try:
        user_obj = load_user(username.lower())
    except:
        messagebox.showerror("Error", "No such User")
    if user_obj.PassEncrypt(password.lower()) == user_obj.password: 
        login_row1.pack_forget()
        login_row2.pack_forget()
        login_row3.pack_forget()
        SysEnter(user_obj)
    else: 
        messagebox.showerror("Incorrect Password", "Try again.")
#region  Login_Frame
tk.Label(login_row1, text="Username ").pack(side="left")
loginusernamebox = tk.Entry(login_row1)
loginusernamebox.pack()
tk.Label(login_row2, text="Password  ").pack(side="left")
loginpasswordbox = tk.Entry(login_row2)
loginpasswordbox.pack()
tk.Button(login_row3, text="Log In", command=login_button).pack(side="left",pady=5)
tk.Button(login_row3, text="or Create Acount", command=create_account_frame_start).pack(pady=5)
#endregion
#region New acount frame
tk.Label(newaccount_row1, text="Enter your new username  ").pack(side="left")
newacountusername = tk.Entry(newaccount_row1)
newacountusername.pack()
tk.Label(newaccount_row2, text="Enter same password  ").pack(side="left")
newacountpassword1 = tk.Entry(newaccount_row2)
newacountpassword1.pack()
tk.Label(newaccount_row3, text="Enter same password  ").pack(side="left")
newacountpassword2 = tk.Entry(newaccount_row3)
newacountpassword2.pack()
tk.Button(newaccount_row4, text="Go", command=create_account_button).pack(pady=5)
#endregion




root.mainloop()