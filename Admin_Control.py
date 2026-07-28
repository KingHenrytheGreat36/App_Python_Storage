from User import *
import tkinter as tk
from tkinter import messagebox
from Primary_System import MainSystem
import os

def is_admin():
    AdminAuthWin = tk.Tk()
    AdminAuthWin.title("Python Storage")
    AdminAuthWin.geometry("400x200")
    R1 = tk.Frame(AdminAuthWin)
    R1.pack()

    AdminCode = tk.Entry(R1, text="Admin Control")
    AdminCode.pack(side="left")
    def PressGo():
        AccualCode = "da2189620361d30d8a71eb74741bc2c733093ae45f122a5984161df2c602909d"
        EnteredCode = AdminCode.get()
        if hash(EnteredCode, "asdf") == AccualCode:
            AdminAuthWin.destroy()
            admin_control()
        else:
            exit()
    tk.Button(R1, text="Go", command=PressGo).pack(pady=5)

def admin_control():
    AdminWin = tk.Tk()
    AdminWin.title("Python Storage")
    AdminWin.geometry("800x600")
    tk.Label(AdminWin, text="Admin Control").pack()

    ImpersonateR1 = tk.Frame(AdminWin)
    ButtonScreen = tk.Frame(AdminWin)

    UserList = tk.Frame(AdminWin)


    ButtonScreen.pack()

    def delstorage():
        yn = messagebox.askyesnocancel("Storage Deletion", "Would you like to delete all data?")
        if yn:
            for ext in (".db", ".dat", ".dir"):
                try:
                    os.remove("PyStorage" + ext)
                except FileNotFoundError: # Will happen every time, so just ignore
                    pass
            messagebox.showinfo("Storage Deleted", "Storage Deleted - the aplication will exit")
            os._exit(0)
        else:
            messagebox.showinfo("Aborted", "Aborted - Storage not deleted")
            os._exit(0)
    def impersonatethis(username):
        user_obj = load_user(username)
        print(username.capitalize() + " should be " + user_obj.username.capitalize())
        restart = MainSystem(user_obj)
        if restart:
            pass
        else: 
            exit()
    def openimpersonate():
        for widget in UserList.winfo_children(): # Remove Privious
            widget.destroy()
        ButtonScreen.pack_forget()
        ImpersonateR1.pack()
        row = 0
        col = 0
        col += 1
        with shelve.open("PyStorage") as db:
            for user in db.keys():       
                tk.Button(UserList,text=user.capitalize(), command=lambda username=user: impersonatethis(username)).grid(row=row, column=col, padx=5, pady=5)
                col += 1
                if col == 5:
                    col = 0
                    row += 1
        UserList.pack()
    def impersonate2home():
        UserList.pack_forget()
        ImpersonateR1.pack_forget()
        ButtonScreen.pack()



    tk.Button(ButtonScreen, text="Clear Storage", command=delstorage).pack(pady=5)
    tk.Button(ButtonScreen, text="Impersonate", command=openimpersonate).pack(pady=5)


    tk.Label(ImpersonateR1, text="Select a user to become").pack(side="left")
    tk.Button(ImpersonateR1, text="Go back", command=impersonate2home).pack()






    AdminWin.wait_window()
