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
    
    NotesList = tk.Frame(mainsys)

    ViewNoteScreen = tk.Frame(mainsys)
    ViewNoteR1 = tk.Frame(ViewNoteScreen)
    ViewNoteR2 = tk.Frame(ViewNoteScreen)
    for row in (ViewNoteR1, ViewNoteR2):
            row.pack()


#endregion
# region Functions
    def ReturntoButtonScreen():    # To return to button screen
        HeadLabel.config(text=f"Welcome {user_obj.username.capitalize()}!")
        ButtonList.pack()
    def Logout():
        nonlocal restart
        restart = True
        mainsys.destroy()
#region Note Stuff
    def OpenNote(noteid):
        for widget in ViewNoteR1.winfo_children():  # Remove stuff that was there before
            widget.destroy()
        for widget in ViewNoteR2.winfo_children():  # Remove stuff that was there before
            widget.destroy()

        note = user_obj.notes[noteid] # Get note
        NotesList.pack_forget()
        ViewNoteScreen.pack()
        HeadLabel.config(text="Note " + note["name"])
        Note_Content = tk.Text(ViewNoteR1, width=40,height=8)
        Note_Content.pack()
        Note_Content.insert("1.0", note["content"])
        def MyNoteSaveNote(noteid):
            content = Note_Content.get("1.0", "end-1c")
            user_obj.notes[noteid]["content"] = Note_Content.get("1.0", "end-1c") # Says user_obj has the new note
            save_user(user_obj)
            messagebox.showinfo("Saved", user_obj.notes[noteid]["name"] + " was saved.")
            ViewNoteScreen.pack_forget()
            ReturntoButtonScreen()
        tk.Button(ViewNoteR2, text="Save Changes", command=lambda: MyNoteSaveNote(noteid)).pack()

        
    def MyNotesButton():
        ButtonList.pack_forget()
        HeadLabel.config(text="My Notes - Choose a note to view/edit")
        for noteid, note in user_obj.notes.items():
            tk.Button( NotesList,
                text=note["name"],
                command=lambda n=noteid: OpenNote(n)
                ).pack(pady=5)

        NotesList.pack()
    def CreateNotesScreen():
        ButtonList.pack_forget()
        HeadLabel.config(text=f"Create a semi-secure Note tied to your account.\nThe name can be anything you want. It is used to read the note later.\n")
        CreateNoteScreen.pack()
    def AboutButton():
        pass
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
        ReturntoButtonScreen()
    def SettingsButton():
        pass
    #endregion
#endregion

    # Button Screen
    tk.Button(ButtonList, text="My Notes", command=MyNotesButton).pack(pady=15)
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