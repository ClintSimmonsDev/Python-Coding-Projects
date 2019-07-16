
from tkinter import *
import tkinter as tk

import Check_Files_Window_Func

def load_gui(self):

    
    self.btn_add = tk.Button(self.master, width=12, height=1, text='Browse...', command=lambda: Check_Files_Window_Func.loadtemplate(self))
    self.btn_add.grid(row=8, column=0, padx=(25, 0), pady=(45, 10), sticky=W)
    self.btn_update = tk.Button(self.master, width=12, height=1, text='Browse...', command=lambda: Check_Files_Window_Func.loadtemplate(self))
    self.btn_update.grid(row=9, column=0, padx=(25, 0), pady=(5, 10), sticky=W)
    self.btn_delete = tk.Button(self.master, width=12, height=2, text='Check for files...', command=lambda: Check_Files_Window_Func.no_threats(self))
    self.btn_delete.grid(row=10, column=0, padx=(25, 0), pady=(5, 0), sticky=W)
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close Program', command=lambda: Check_Files_Window_Func.ask_quit(self))
    self.btn_close.grid(row=10, column=0, padx=(430, 0), pady=(5, 0), sticky=E)

    self.txt_browse1 = tk.Entry(self.master, text='')
    self.txt_browse1.grid(row=8, column=0, rowspan=1, columnspan=2, padx=(150, 0), pady=(40, 10), sticky=W+E)
    self.txt_browse2 = tk.Entry(self.master, text='')
    self.txt_browse2.grid(row=9, column=0, rowspan=1, columnspan=2, padx=(150, 0), pady=(0, 10), sticky=W+E)


if __name__ == "__main__":
    pass
