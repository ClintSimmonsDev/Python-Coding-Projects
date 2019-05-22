
import os
import tkinter
from tkinter import messagebox
from tkinter import filedialog


def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if tkinter.messagebox.askokcancel("Exit program", "You really wanna go?"):
        self.master.destroy()
        os._exit(0)

def no_threats(self):
    messagebox.showinfo("Files checked",  "No threats found.")


def loadtemplate(self):
    filename = filedialog.askopenfilename(filetypes=(("Template files", "*.tplate")
                                                       , ("HTML files", "*.html;*.htm")
                                                       , ("All files", "*.*")))
    if filename:
        try:
            self.settings["template"].set(filename)
        except:
            messagebox.showerror("Open Source File", "Failed to read file \n'%s'" % filename)
            return

if __name__ == "__main__":
    pass
