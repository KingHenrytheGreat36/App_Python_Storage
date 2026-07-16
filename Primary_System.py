from User import *
import tkinter as tk
from tkinter import messagebox


def MainSystem(user_obj):
    mainsys = tk.Tk()
    mainsys.title("Python Storage")
    mainsys.geometry("800x600")
    tk.Label(mainsys, text="Python Secure(ish) Storage").pack()
    restart = False

    #region --- Frames (Screens) ---
    ButtonScreen = tk.Frame(mainsys)
    ButtonRow1 = tk.Frame(ButtonScreen)
    ButtonRow2 = tk.Frame(ButtonScreen)
    ButtonRow2 = tk.Frame(ButtonScreen)
    ButtonRow1.pack()
    ButtonRow2.pack()
    ButtonScreen.pack()

#endregion

    def Logout():
        nonlocal restart
        print("Loging out")
        restart = True
        mainsys.destroy()
        
# Button Screen
    tk.Label(ButtonRow1, text=f"Welcome {user_obj.username.capitalize()}!").pack(side="left")
    tk.Button(ButtonRow1, text="Log out", command=Logout).pack(side="right",pady=5)








    mainsys.wait_window()   # outer waits here until win closes
    return restart