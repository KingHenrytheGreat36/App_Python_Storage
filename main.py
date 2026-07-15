import tkinter as tk
from Primary_Functions import *
from User import *

print("Welcome to Python Secure(ish) Storage!")
print("By Henry F.")
root = tk.Tk()
root.title("Python Storage")
root.geometry("600x400")
tk.Label(root, text="Welcome to Python Secure(ish) Storage by Henry F.").pack()

# --- Frames (Screens) ---
login_frame = tk.Frame(root)
newaccount_frame = tk.Frame(root)

menu_frame = tk.Frame(root)
about_frame = tk.Frame(root)
login_frame.pack()
#for frame in (login_frame, menu_frame):
#    frame.place(relwidth=1, relheight=1)
#def show_frame(frame):
 #   frame.tkraise()

# END
def create_account_button():
    login_frame.pack_forget()
    newaccount_frame.pack()
#  Login_Frame
tk.Label(login_frame, text="Log in  ").pack(side="left")
tk.Button(login_frame, text="or Create Acount", command=create_account_button).pack(pady=5)












root.mainloop()