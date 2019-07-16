#!/usr/bin/python
"""
    #!/usr/bin/python
    It's a recommended way, proposed in documentation:
    2.2.2. Executable Python Scripts.
    In a Unix-like operating system, the program loader
    takes the presence of these two characters as an
    indication that the file is a script, and tries to
    execute that script using the interpreter specified
    by the rest of the first line in the file.
"""
# -*- coding: utf-8 -*-
"""
    # -*- coding: utf-8 -*-
    This sets the charset if it is present on the first two lines of the file.
    this is Syntax to declare the encoding of a Python source file. It's discussed
    in PEP 0263 - Defining Python Source Code Encodings.
    https://www.python.org/dev/peps/pep-0263/
"""
#
# Python Ver:   3.5.1
#
# Author:       Daniel A. Christie
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk

import drill50_phonebook_gui
import drill50_phonebook_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(200,500) #(Height, Width)
        self.master.maxsize(400,1000)
        # This CenterWindow method will center our app on the user's screen
        drill50_phonebook_func.center_window(self,200,500)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: drill50_phonebook_func.ask_quit(self))

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        drill50_phonebook_gui.load_gui(self)


        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
