import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,80)
        self.master.maxsize(500,80)

        center_window(self, 550, 200)
        self.master.title("Choose Your Directory")
        self.master.configure(bg="#F0F0F0")

        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))

        load_gui(self)



def load_directory(self):
    files = filedialog.askdirectory()
    self.txt_browse1 = tk.Entry(self.master, text="")
    self.txt_browse1.grid(row=3, column=1, rowspan=1, columnspan=4, padx=(150, 0), pady=(20, 10), sticky=W + E)
    self.txt_browse1.insert(0, files)


def load_gui(self):

    self.btn_add = tk.Button(self.master, width=12, height=1, text='Browse...',
                             command=lambda: load_directory(self))
    self.btn_add.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(25, 25), pady=(20, 10), sticky=N)
    self.txt_browse1 = tk.Entry(self.master, text="")
    self.txt_browse1.grid(row=3, column=1, rowspan=1, columnspan=4, ipadx=(100), padx=(150, 0), pady=(20, 10), sticky=W + E)



def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "So you're done, huh?"):
        self.master.destroy()
        os._exit(0)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()