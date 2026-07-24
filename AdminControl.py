from User import *
import tkinter as tk
from tkinter import messagebox
from Primary_System import MainSystem
import os

def HasAdminAccess():
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
        if Hash(EnteredCode, "asdf") == AccualCode:
            print("Hello, Henry, The Wise Creator who knows the secret code!\nExecutive Functions Active.")
            AdminAuthWin.destroy()
            AdminControls()
        else:
            exit()
    tk.Button(R1, text="Go", command=PressGo).pack(pady=5)

def AdminControls():
    AdminWin = tk.Tk()
    AdminWin.title("Python Storage")
    AdminWin.geometry("800x600")
    tk.Label(AdminWin, text="Admin Control").pack()

    ImpersonateR1 = tk.Frame(AdminWin)
    ButtonScreen = tk.Frame(AdminWin)

    UserList = tk.Frame(AdminWin)


    ButtonScreen.pack()

    def DelStorage():
        yn = messagebox.askyesnocancel("Storage Deletion", "Would you like to delete all data?")
        if yn == True:
            for ext in (".db", ".dat", ".dir"):
                try:
                    os.remove("Storage" + ext)
                except FileNotFoundError: # Will happen every time, so just ignore
                    pass
            messagebox.showinfo("Storage Deleted", "The aplication will exit")
        else:
            messagebox.showinfo("Aborted", "Storage not deleted")
        exit()
    def ImpersonateThis(username):
        print(username.capitalize())
    def OpenImpersonate():
        for widget in UserList.winfo_children(): # Remove Privious
            widget.destroy()
        ButtonScreen.pack_forget()
        ImpersonateR1.pack()
        row = 0
        col = 0
        col += 1
        with shelve.open("Storage") as db:
            for user in db.keys():       
                print(user)         
                tk.Button(UserList,text=user.capitalize(), command=lambda username=user: ImpersonateThis(username)).grid(row=row, column=col, padx=5, pady=5)
                col += 1
                if col == 5:
                    col = 0
                    row += 1
        UserList.pack()


    tk.Button(ButtonScreen, text="Clear Storage", command=DelStorage).pack(pady=5)
    tk.Button(ButtonScreen, text="Impersonate", command=OpenImpersonate).pack(pady=5)


    tk.Label(ImpersonateR1, text="Select a user to become").pack()








    AdminWin.wait_window()
