from Notes import Note, load_note, save_note
from User import *
import tkinter as tk
from tkinter import messagebox
from Settings import settings_win

def MainSystem(user_obj):
    mainsys = tk.Tk()
    mainsys.title("Python Storage")
    mainsys.geometry("800x600")
    tk.Label(mainsys, text="Python Secure(ish) Storage").pack()
    HeadLabel = tk.Label(mainsys, text=f"Welcome {user_obj.nickname}!")
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
    
    AboutScreen = tk.Frame(mainsys)
    AboutR1 = tk.Frame(AboutScreen)
    AboutR1.pack()
    AboutR2 = tk.Frame(AboutScreen)
    AboutR2.pack()
#endregion

# region Functions
    def return_to_button_screen():    # To return to button screen
        HeadLabel.config(text=f"Welcome {user_obj.nickname}!")
        ButtonList.pack()
    def logout():
        nonlocal restart
        restart = True
        mainsys.destroy()
#region Note Stuff
    def open_note(noteid):
        for widget in ViewNoteR1.winfo_children():  # Remove stuff that was there before
            widget.destroy()
        for widget in ViewNoteR2.winfo_children():  # Remove stuff that was there before
            widget.destroy()

        note = load_note(noteid) # Get note
        NotesList.pack_forget()
        ViewNoteScreen.pack()
        HeadLabel.config(text="Note " + note.name)
        Note_Content = tk.Text(ViewNoteR1, width=40,height=8)
        Note_Content.pack()
        Note_Content.insert("1.0", note.content)
        def MyNoteSaveNote(noteid):
            Log(f"Open note function not finished. Note ID: {noteid}")
            content = Note_Content.get("1.0", "end-1c")
            note = load_note(noteid)
            note.content = Note_Content.get("1.0", "end-1c") # Says user_obj has the new note
            save_note(note)
            messagebox.showinfo("Saved", note.name + " was saved.")
            Log(f"Note {note.name} saved for {note.owner}. Note number: {note.id}")
            ViewNoteScreen.pack_forget()
            notes_button()
        tk.Button(ViewNoteR2, text="Save Changes", command=lambda: MyNoteSaveNote(noteid)).pack()


    def notes_button():
        for widget in NotesList.winfo_children(): # Remove Privious
            widget.destroy()
        ButtonList.pack_forget()
        HeadLabel.config(text="My Notes - Choose a note to view/edit") # Create Header
        row = 0
        col = 0
        tk.Button(NotesList, text="Back", command=lambda: [NotesList.pack_forget(), return_to_button_screen()]).grid(row=row, column=col, padx=5, pady=5)
        col += 1
        tk.Button( NotesList,text="Create New", command=create_notes_screen).grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col == 5:
            col = 0
            row += 1
        for noteid in user_obj.notes:
            note = load_note(noteid)
            tk.Button(
                NotesList,
                text=note.name.capitalize(),
                command=lambda n=noteid: open_note(n)
            ).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col == 5:
                col = 0
                row += 1
        NotesList.pack()
    def create_notes_screen():
        NotesList.pack_forget()
        HeadLabel.config(text=f"Create a semi-secure Note tied to your account.\nThe name can be anything you want. It is used to read the note later.\n")
        CreateNoteScreen.pack()
    def create_note_button():
        nonlocal user_obj
        content = CreateNoteText.get("1.0", "end-1c")
        nickname = user_obj.nickname
        if CreateNoteName.get() == "":
            messagebox.showerror("Missing Content", "Write a note name")
        else:
            note = Note(CreateNoteName.get(), content, user_obj.username)
            save_note(note)
            user_obj.notes.append(note.id)
            save_user(user_obj)
            messagebox.showinfo(f"Note Created", f"Note, {note.name}, has been saved for {nickname}.")
            Log(f"Note {note.id} created for user {note.owner}.")
        CreateNoteScreen.pack_forget()
        return_to_button_screen()
#endregion
    def to_about_screen():
            ButtonList.pack_forget()
            HeadLabel.configure(text="About Python Storing")
            AboutScreen.pack()
    def fromaboutscreen():
         AboutScreen.pack_forget()
         ButtonList.pack()
         HeadLabel.configure(text=f"Welcome {user_obj.nickname}!")

    def settingsbutton():
        mainsys.withdraw()     # hide window 
        settings_win(user_obj)
        mainsys.deiconify()    # show window again
    
#endregion

    # Button Screen
    tk.Button(ButtonList, text="My Notes", command=notes_button).pack(pady=15)
    tk.Button(ButtonList, text="About", command=to_about_screen).pack(pady=15)
    tk.Button(ButtonList, text=f"{user_obj.username.capitalize()}'s Settings", command=settingsbutton).pack(pady=15)
    tk.Button(ButtonList, text="Log out", command=logout).pack(pady=15)
    if user_obj.testsetting:
        tk.Button(ButtonList, text="Test Setting", command=lambda: messagebox.showinfo("Test Setting", "This is a test setting.")).pack(pady=15)


    # Create Note Screen
    tk.Label(CreateNoteR1, text="Note Name   ").pack(side="left")
    CreateNoteName = tk.Entry(CreateNoteR1)
    CreateNoteName.pack()
    tk.Label(CreateNoteR2, text="Note Content").pack()
    CreateNoteText = tk.Text(CreateNoteR3, width=40, height=8)
    CreateNoteText.pack()
    tk.Button(CreateNoteR4, text="Create", command=create_note_button).pack(pady=5)

    #About Screen
    AboutStuff = "This is a simple storage system written in Python.\nThis was created by @HenrytheGreat36 on Github.\nThis is a app version of a previous console version by the same name.\nAs you know, you can make an acount to store notes."
    tk.Label(AboutR1, text=AboutStuff).pack()
    tk.Button(AboutR2, text="Back", command=fromaboutscreen).pack(pady=10)
    def Estop():
        ErrorLog("E‑STOP triggered.", "CRITICAL")
        os._exit(0)
    tk.Button(ButtonList, text="E‑STOP", fg="red", command=Estop).pack(pady=15)


    mainsys.wait_window()   # outer waits here until win closes
    Log("Primary_System window closed.")

    return restart