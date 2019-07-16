
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
    if tkinter.messagebox.askokcancel("Exit program", "So you're done, huh?"):
        self.master.destroy()
        os._exit(0)



def loadtemplate(self):
    filename = filedialog.askdirectory(filetypes=(("Python Files", "*.py")
                                                       , ("Database Files", "*.db")
                                                       , ("All files", "*.*")))
    return filename


if __name__ == "__main__":
    pass
