from User import *
import tkinter as tk
from tkinter import messagebox
import time
import os

def SettingsWin(user_obj):
    SettingsWin = tk.Tk()
    SettingsWin.title("Python Storage")
    SettingsWin.geometry("800x600")
    tk.Label(SettingsWin, text=f"{user_obj.username.capitalize()}'s Settings").pack()
    tk.Label(SettingsWin, text="").pack() # Spacer
    HeadLabel = tk.Label(SettingsWin, text=f"Choose a setting") 
    HeadLabel.pack()

    SettingsList = tk.Frame(SettingsWin)

    ChangePassScreen = tk.Frame(SettingsWin)

    ChangePassR1 = tk.Frame(ChangePassScreen)
    ChangePassR1.pack()
    ChangePassR2 = tk.Frame(ChangePassScreen)
    ChangePassR2.pack()
    ChangePassR3 = tk.Frame(ChangePassScreen)
    ChangePassR3.pack()
    ChangePassR4 = tk.Frame(ChangePassScreen)
    ChangePassR4.pack()
    
    SettingsList.pack()


    def ToChangePassScreen():
        SettingsList.pack_forget()
        HeadLabel.configure(text="Change Password")
        ChangePassScreen.pack()
    def FromChangePassScreen():
        ChangePassScreen.pack_forget()
        SettingsList.pack()
        HeadLabel.configure(text="Choose a Setting")
    def DoChangePass():
        Oldpassword = Oldpassbox.get()
        Newpassword1 = Newpassbox1.get()
        Newpassword2 = Newpassbox2.get()
        if Newpassword1.lower() == Newpassword2.lower():
            if user_obj.PassEncrypt(Oldpassword.lower()) == user_obj.password:
                user_obj.password = user_obj.PassEncrypt(Newpassword1.lower())
                save_user(user_obj)
                messagebox.showinfo("Password Saved", "Your Password has been saved.")
                FromChangePassScreen()
            else:
                messagebox.showerror("Password Incorrect", "Old password is not correct")
        else:
            messagebox.showerror("Error", "New Passwords are not the same.") # old passwrods must match
    def ToNicknameChange():
        messagebox.showerror("Nothing Now", "Nothing Now")
    def FromNicknameChange():
        pass
    def DelAcount():
        yn = messagebox.askyesnocancel("Acount Deletion", "Would you like to delete your account?")
        if yn:
            time.sleep(1)
            yn2 =  messagebox.askyesnocancel("Acount Deletion", "Are you sure?")
            if yn2:
                didwork = user_obj.DeleteAcount()
                if didwork:
                    messagebox.showinfo("Successful", "Account deleted")
                    time.sleep(3)
                    messagebox.showwarning("Closing", "Application will close")
                    os._exit(0)
                else:
                    messagebox.showinfo("Error", "An error occured. Account not deleted")
            else:
                messagebox.showinfo("Aborted", "Aborted - Account not deleted")
        else:
            messagebox.showinfo("Aborted", "Aborted - Account not deleted")


    tk.Button(SettingsList, text="Change Password", command=ToChangePassScreen).pack()
    tk.Button(SettingsList, text="Change Nickname? (NOTHING NOW)", command=ToNicknameChange).pack(pady=10)
    tk.Label(SettingsList, text="").pack()
    tk.Label(SettingsList, text="").pack()
    tk.Button(SettingsList, text="Delete Acount", command=DelAcount).pack()



    tk.Label(ChangePassR1, text="Old Password ").pack(side="left")
    Oldpassbox = tk.Entry(ChangePassR1)
    Oldpassbox.pack()
    tk.Label(ChangePassR2, text="New Password").pack(side="left")
    Newpassbox1 = tk.Entry(ChangePassR2)
    Newpassbox1.pack()
    tk.Label(ChangePassR3, text="New Password").pack(side="left")
    Newpassbox2 = tk.Entry(ChangePassR3)
    Newpassbox2.pack()
    tk.Button(ChangePassR4, text="Change Password", command=DoChangePass).pack(side="left" )
    tk.Button(ChangePassR4, text="Back", command=FromChangePassScreen).pack(side="right")



    SettingsWin.wait_window()   # outer waits here until win closes
    return 1