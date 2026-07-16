from User import *
import tkinter as tk
from tkinter import messagebox

def MainSystem(user_obj):
    mainsys = tk.Tk()
    mainsys.title("Python Storage")
    mainsys.geometry("800x600")
    tk.Label(mainsys, text="Python Secure(ish) Storage").pack()
    HeadLabel = tk.Label(mainsys, text=f"Welcome {user_obj.username.capitalize()}!")
    HeadLabel.pack()
    restart = False

    #region --- Frames (Screens) ---
    ButtonList = tk.Frame(mainsys)
    ButtonList.pack()

    CreateNoteScreen = tk.Frame(mainsys)
    CreateNoteR1 = tk.Frame(CreateNoteScreen)
    CreateNoteR2 = tk.Frame(CreateNoteScreen)
    CreateNoteR3 = tk.Frame(CreateNoteScreen)
    CreateNoteR4 = tk.Frame(CreateNoteScreen)
    for row in (CreateNoteR1, CreateNoteR2, CreateNoteR3, CreateNoteR4):
            row.pack()


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
    def CreateNotesScreen():
        ButtonList.pack_forget()
        HeadLabel.config(text=f"Create a semi-secure Note tied to your account.\nThe name can be anything you want. It is used to read the note later.\n")
        CreateNoteScreen.pack()
    def AboutButton():
        print("About  Button Pressed")
    def SettingsButton():
        print("Settings Button Pressed")
    def CreateNoteButton():
        nonlocal user_obj
        content = CreateNoteText.get("1.0", "end-1c")
        username = user_obj.username.lower()
        if CreateNoteName.get() == "":
            messagebox.showerror("Missing Content", "Write a note name")
        else:
            user_obj = load_user(username) 
            notecount = user_obj.add_note(CreateNoteName.get(), content)
            save_user(user_obj)
            messagebox.showinfo(f"Note Created", f"Note, {CreateNoteName.get()}, has been saved for {username}.")
            messagebox.showinfo("Debug", f"(For debuging purposes, it is acualy note {notecount})")
        CreateNoteScreen.pack_forget()
        ReturnButtonScreen()

    #endregion

    # Button Screen
    tk.Button(ButtonList, text="My Notes ( No Click )", command=MyNotesButton).pack(pady=15)
    tk.Button(ButtonList, text="Create Notes", command=CreateNotesScreen).pack(pady=15)
    tk.Button(ButtonList, text="About ( No Click )", command=AboutButton).pack(pady=15)
    tk.Button(ButtonList, text=f"{user_obj.username.capitalize()}'s Settings (No Click)", command=SettingsButton).pack(pady=15)
    tk.Button(ButtonList, text="Log out", command=Logout).pack(pady=15)

    # Create Note Screen

    tk.Label(CreateNoteR1, text="Note Name   ").pack(side="left")
    CreateNoteName = tk.Entry(CreateNoteR1)
    CreateNoteName.pack()
    tk.Label(CreateNoteR2, text="Note Content").pack()
    CreateNoteText = tk.Text(CreateNoteR3, width=40, height=8)
    CreateNoteText.pack()
    tk.Button(CreateNoteR4, text="Create", command=CreateNoteButton).pack(pady=5)









    mainsys.wait_window()   # outer waits here until win closes
    return restart