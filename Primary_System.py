from User import *
import tkinter as tk
from tkinter import messagebox


def MainSystem(user_obj):
    mainsys = tk.Tk()
    mainsys.title("Python Storage")
    mainsys.geometry("800x600")
    tk.Label(mainsys, text="Python Secure(ish) Storage").pack()
    HeadLabel = tk.Label(mainsys, text=f"Welcome {user_obj.username.capitalize()}!").pack()
    restart = False

    #region --- Frames (Screens) ---
    ButtonList = tk.Frame(mainsys)
    ButtonList.pack()

    CreateNoteScreen = tk.Frame(mainsys)
    CreateNoteR1 = tk.Frame(CreateNoteScreen)
    CreateNoteR2 = tk.Frame(CreateNoteScreen)
    CreateNoteR1 = tk.Frame(CreateNoteScreen)


#endregion
# region Functions
    def ReturnButtonScreen():    # To return to button screen
        HeadLabel.config(text=f"Welcome {user_obj.username.capitalize()}!")
        ButtonList.pack()
    def Logout():
        nonlocal restart
        print("Loging out")
        restart = True
        mainsys.destroy()
    def MyNotesButton():
        print("My Notes Button Pressed")
    def CreateNotesButton():
        print("Create Notes Button Pressed")
        ButtonList.pack_forget()
    def AboutButton():
        print("About  Button Pressed")
    def SettingsButton():
        print("Settings Button Pressed")
    #endregion

    # Button Screen
    tk.Button(ButtonList, text="My Notes ( No Click! )", command=MyNotesButton).pack(pady=15)
    tk.Button(ButtonList, text="Create Notes", command=CreateNotesButton).pack(pady=15)
    tk.Button(ButtonList, text="About ( No Click )", command=AboutButton).pack(pady=15)
    tk.Button(ButtonList, text=f"{user_obj.username.capitalize()}'s Settings (No Click)", command=SettingsButton).pack(pady=15)
    tk.Button(ButtonList, text="Log out", command=Logout).pack(side="right",pady=15, padx=20)









    mainsys.wait_window()   # outer waits here until win closes
    return restart