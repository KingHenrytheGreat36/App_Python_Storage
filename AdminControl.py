from User import *
import tkinter as tk
from tkinter import messagebox
from Primary_System import MainSystem

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
    tk.Button(AdminWin, text="OLD SYSTEM", command=Executive).pack(pady=5)















    AdminWin.wait_window()
    print("Admin left.")





# Old Console Version of program did this, so I will keep it for now
def Executive():
    pa = input("")
    hashed = Hash(pa)
    import os

    if hashed == "f99bac0c814f3feb1325ef9698a2ad37dfad1694dab51fcc29ef4b445ce6fc74":
        print("Hello, Henry, The Wise Creator who knows the secret code!\nExecutive Functions Active.")
        print("1. Delete All Storage.\n2. Execute Python Code.\n3. Log in as someone else.\n4. Encrypt and turn to lowercase 50,000 times.")
        what = input("Whitch Number?")

        if what == "1": # Clear Storage
            for ext in (".db", ".dat", ".dir"):
                try:
                    os.remove("Storage" + ext)
                except FileNotFoundError:
                    pass
            print("All Storage Deleted.")
            exit()
        elif what == "2": # Execute Code
            command = input("Be careful about executing code. It can destroy your system, or corupt all storage.\nDo control C or write c to cancel. \nBe careful! \nEnter Python code: ")
            if command.lower() == "c":
                print("Code not Executed. Cancelled. Bye, Henry!")
                exit()
            try:
                exec(command)
                print("Code Executed. Bye, Henry!")
                exit()
            except Exception as e:
                print("Code not Executed. Error:", e)
                exit()
        elif what == "3":   # Impersonate  
            with shelve.open("Storage") as db:
                print("Choose a user to inpersonate:")
                for user in db.keys():
                    print(user + ",")
                n = input("What username:")
                try:
                    MainSystem(n.lower())
                except:
                    print("No user.")
                exit()
        elif what == "4":
            pre = input("What? ")
            slt = input("Salt? ")
            print(Hash(pre, slt))
        else:
            exit()

    else: # If no permision to access the backdoor, exit the program.
        exit()