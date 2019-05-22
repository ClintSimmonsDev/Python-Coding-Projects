

from tkinter import *
import tkinter as tk

import Check_Files_Window_Gui
import Check_Files_Window_Func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(550,200)
        self.master.maxsize(1100,400)

        Check_Files_Window_Func.center_window(self, 550, 200)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")

        self.master.protocol("WM_DELETE_WINDOW", lambda: Check_Files_Window_Func.ask_quit(self))

        Check_Files_Window_Gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
