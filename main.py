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

#region --- Frames (Screens) ---
login_row1 = tk.Frame(root)
login_row2 = tk.Frame(root)
login_row3 = tk.Frame(root)

newaccount_row1 = tk.Frame(root)
newaccount_row2 = tk.Frame(root)
newaccount_row3 = tk.Frame(root)
newaccount_row4 = tk.Frame(root)

menu_frame = tk.Frame(root)
about_frame = tk.Frame(root)
login_row1.pack()
login_row2.pack()
login_row3.pack()

#for frame in (login_frame, menu_frame):
#    frame.place(relwidth=1, relheight=1)
#def show_frame(frame):
 #   frame.tkraise()

#endregion
def create_account_frame_start():
    login_row1.pack_forget()
    login_row2.pack_forget()
    login_row3.pack_forget()
    newaccount_row1.pack()
    newaccount_row2.pack()
    newaccount_row3.pack()
    newaccount_row4.pack()
def SysEnter(username):
    pass
def create_account_button():
    username = newacountusername.get()   # Make this lower
    password1 = newacountpassword1.get()
    password2 = newacountpassword2.get()
    print(f"You typed: {username}, {password1}, {password2}")
    if password1.lower() == password2.lower():
        user_obj = User(username.lower(), password1.lower())
        messagebox.showinfo("Success", f"Account ({username}) Created")
        print("Account created")
        SysEnter(username.lower())
    else: messagebox.showerror("Error", "Incorrect password.")
    
    save_user(user_obj)
def login_button():
    print(f"Login Button pressed,{loginusernamebox.get().lower()}, {loginpasswordbox.get().lower()}")
    username = loginusernamebox.get()
    try:
        user_obj = load_user(loginusernamebox.get().lower())
    except:
        messagebox.showerror("Error", "No such User")
    password = username.lower()
    if user_obj.PassEncrypt(password) == user_obj.password: 
        print("You have successfully logged in.")
        SysEnter(username.lower())
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