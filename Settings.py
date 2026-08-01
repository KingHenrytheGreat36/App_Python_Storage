from asyncio import log

from User import *
import tkinter as tk
from tkinter import messagebox
import time
import os

def settings_win(user_obj):
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

    NicknameChangeScreen = tk.Frame(SettingsWin)

    NicknameR1 = tk.Frame(NicknameChangeScreen)
    NicknameR1.pack()
    NicknameR2 = tk.Frame(NicknameChangeScreen)
    NicknameR2.pack()
    
    SettingsList.pack()


    def to_change_pass_screen():
        SettingsList.pack_forget()
        HeadLabel.configure(text="Change Password")
        ChangePassScreen.pack()
    def from_change_pass_screen():
        ChangePassScreen.pack_forget()
        SettingsList.pack()
        HeadLabel.configure(text="Choose a Setting")
    def do_change_pass():
        Oldpassword = Oldpassbox.get()
        Newpassword1 = Newpassbox1.get()
        Newpassword2 = Newpassbox2.get()
        if Newpassword1.lower() == Newpassword2.lower():
            if user_obj.PassEncrypt(Oldpassword.lower()) == user_obj.password:
                user_obj.password = user_obj.PassEncrypt(Newpassword1.lower())
                save_user(user_obj)
                messagebox.showinfo("Password Saved", "Your Password has been saved.")
                from_change_pass_screen()
            else:
                messagebox.showerror("Password Incorrect", "Old password is not correct")
        else:
            messagebox.showerror("Error", "New Passwords are not the same.") # old passwrods must match
    def to_nickname_change():
        SettingsList.pack_forget()
        HeadLabel.configure(text="Change Nickname")   # NOTE ADD previous nickname to entry
        NicknameChangeScreen.pack()
    def from_nickname_change():
        NicknameChangeScreen.pack_forget()
        SettingsList.pack()
        HeadLabel.configure(text="Choose a Setting")
    def save_nickname():
        newnickname = NicknameBox.get()
        oldnickname = user_obj.nickname
        Log(f"Changed {user_obj.username}'s nickname from {oldnickname} to {newnickname}")
        user_obj.nickname = newnickname.capitalize()
        save_user(user_obj)
        messagebox.showinfo("Nickname change", f"Your nickname has been changed from {oldnickname} to {newnickname}.")

    def delacount():
        yn = messagebox.askyesnocancel("Acount Deletion", "Would you like to delete your account?")
        if yn:
            time.sleep(1)
            yn2 =  messagebox.askyesnocancel("Acount Deletion", "Are you sure?")
            if yn2:
                didwork = user_obj.DeleteAcount()
                if didwork:
                    Log(f"User {user_obj.username} deleted their account.")
                    messagebox.showinfo("Successful", "Account deleted")
                    time.sleep(3)
                    Log(f"Application Closed.")
                    messagebox.showwarning("Closing", "Application will close")
                    os._exit(0)
                else:
                    ErrorLog(f"User {user_obj.username} failed to delete their account.")
                    messagebox.showinfo("Error", "An error occured. Account not deleted")
            else:
                ErrorLog(f"User {user_obj.username} cancelled the account deletion.")

                messagebox.showinfo("Aborted", "Aborted - Account not deleted")
        else:
            messagebox.showinfo("Aborted", "Aborted - Account not deleted")
            ErrorLog(f"User {user_obj.username} cancelled the account deletion.")



    tk.Button(SettingsList, text="Change Password", command=to_change_pass_screen).pack()
    tk.Button(SettingsList, text="Change Nickname", command=to_nickname_change).pack(pady=10)
    tk.Label(SettingsList, text="").pack()
    tk.Label(SettingsList, text="").pack()
    tk.Button(SettingsList, text="Delete Acount", command=delacount).pack()



    tk.Label(ChangePassR1, text="Old Password ").pack(side="left")
    Oldpassbox = tk.Entry(ChangePassR1)
    Oldpassbox.pack()
    tk.Label(ChangePassR2, text="New Password").pack(side="left")
    Newpassbox1 = tk.Entry(ChangePassR2)
    Newpassbox1.pack()
    tk.Label(ChangePassR3, text="New Password").pack(side="left")
    Newpassbox2 = tk.Entry(ChangePassR3)
    Newpassbox2.pack()
    tk.Button(ChangePassR4, text="Change Password", command=do_change_pass).pack(side="left" )
    tk.Button(ChangePassR4, text="Back", command=from_change_pass_screen).pack(side="right")


    tk.Label(NicknameR1, text="Nickname").pack(side="left")
    NicknameBox = tk.Entry(NicknameR1)
    NicknameBox.pack()
    tk.Button(NicknameR2, text="Back", command=from_nickname_change).pack(side="left")
    tk.Button(NicknameR2, text="Save", command=save_nickname).pack(side="right" )
    





    SettingsWin.wait_window()   # outer waits here until win closes
    Log("Settings window closed.")
    return 1