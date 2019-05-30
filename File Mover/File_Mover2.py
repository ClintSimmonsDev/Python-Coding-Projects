import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(470,80)
        self.master.maxsize(470,300)

        center_window(self, 550, 200)
        self.master.title("Locate & Move .txt Files")
        self.master.configure(bg="darkgrey")

        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))

        load_gui(self)


def load_directory(self):
    self.name = tk.StringVar()
    self.txt_browse1 = tk.Entry(self.master, textvariable=self.name)

    files = filedialog.askdirectory()
    self.txt_browse1.grid(row=3, column=1, rowspan=1, columnspan=4, padx=(150, 0), pady=(20, 10), sticky=W + E)
    self.txt_browse1.insert(1, files)


def load_destination(self):
    files = filedialog.askdirectory()
    self.txt_browse2 = tk.Entry(self.master, text="")
    self.txt_browse2.grid(row=4, column=1, rowspan=1, columnspan=4, padx=(150, 0), pady=(20, 10), sticky=W + E)
    self.txt_browse2.insert(1, files)
    self.txt_browse2.get()


file_list = []
time_list = []


def txt_transfer(self):
    conn = sqlite3.connect("txtFinder.db")
    with conn:

        cur = conn.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS tbl_TxtFiles(\
        id integer PRIMARY KEY AUTOINCREMENT,\
        Files TEXT,\
        Timestamp INTEGER)')

    destination = (self.txt_browse2.get())

    for files in os.listdir(self.txt_browse1.get()):
        if files.endswith(".txt"):
            joined_file = os.path.join(self.txt_browse1.get(), files)
            shutil.move(joined_file, destination)
            joined_file2 = os.path.join(self.txt_browse2.get(), files)
            time = os.path.getmtime(joined_file2)
            file_list.append(files)
            time_list.append(time)
            cur.execute("INSERT INTO tbl_TxtFiles(Files, Timestamp) VALUES (?,?)",
                        (files, time))

        cur.execute("SELECT * FROM tbl_TxtFiles")

        conn.commit()


    varTxtFile = cur.fetchall()
    print("\nThe following .txt files have been moved:\n" + str(varTxtFile))
    conn.close()


def load_gui(self):

    self.btn_src_dir = tk.Button(self.master, width=12, height=1, text='Source Directory',
                             command=lambda: load_directory(self))
    self.btn_src_dir.grid(row=3, column=0, rowspan=1, columnspan=2, ipadx=(15), padx=(25, 25), pady=(20, 10), sticky=N)

    self.btn_dest_dir = tk.Button(self.master, width=12, height=1, text='Destination Directory',
                                 command=lambda: load_destination(self))
    self.btn_dest_dir.grid(row=4, column=0, rowspan=1, columnspan=2, ipadx=(15), padx=(25, 25), pady=(20, 5), sticky=N)

    self.btn_txt = tk.Button(self.master, width=15, height=1, text='Move .txt Files',
                             command=lambda: txt_transfer(self))
    self.btn_txt.grid(row=5, column=1, rowspan=1, columnspan=7, ipadx=15, ipady=15, padx=(25, 25), pady=(10, 5), sticky=N)

    self.dir_choose = tk.Entry(self.master, text="")
    self.dir_choose.grid(row=3, column=1, rowspan=1, columnspan=4, ipadx=80, padx=(170, 0), pady=(20, 10), sticky=E)

    self.destination_choose = tk.Entry(self.master, text="")
    self.destination_choose.grid(row=4, column=1, rowspan=1, columnspan=4, ipadx=80, padx=(170, 0), pady=(20, 10), sticky=E)

  #  self.find_txt = tk.Entry(self.master, text="")
   # self.find_txt.grid(row=5, column=1, rowspan=1, columnspan=3, ipadx=80, padx=(170, 0), pady=(20, 10), sticky=E)


def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))

    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Ok to Exit?"):
        self.master.destroy()
        os._exit(0)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()