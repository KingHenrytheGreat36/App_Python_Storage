from User import *
import tkinter as tk
from tkinter import messagebox


def MainSystem(user_obj):
    mainsys = tk.Tk()
    mainsys.title("Python Storage")
    mainsys.geometry("800x600")
    tk.Label(mainsys, text="Python Secure(ish) Storage").pack()

    #region --- Frames (Screens) ---
    Buttons = tk.Frame(mainsys)
    Buttons.pack()

#endregion
