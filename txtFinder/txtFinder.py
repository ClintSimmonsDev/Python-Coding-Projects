import sqlite3

conn = sqlite3.connect("txtFinder.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_VarFiles(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
    col_Files TEXT)")
    conn.commit()

    cur.execute("INSERT INTO tbl_VarFiles(col_Files) VALUES\
                     ('information.docx')")
    cur.execute("INSERT INTO tbl_VarFiles(col_Files) VALUES\
                     ('Hello.txt')")
    cur.execute("INSERT INTO tbl_VarFiles(col_Files) VALUES\
                         ('myImage.png')")
    cur.execute("INSERT INTO tbl_VarFiles(col_Files) VALUES\
                         ('myMovie.mpg')")
    cur.execute("INSERT INTO tbl_VarFiles(col_Files) VALUES\
                         ('World.txt')")
    cur.execute("INSERT INTO tbl_VarFiles(col_Files) VALUES\
                             ('data.pdf')")
    cur.execute("INSERT INTO tbl_VarFiles(col_Files) VALUES\
                             ('myPhoto.jpg')")
    conn.commit()

    cur.execute("SELECT col_Files FROM tbl_VarFiles WHERE col_Files LIKE '%.txt'")

    varTxtFile = cur.fetchall()

    print("\nThe following files in database txtFinder are .txt files:\n" + str(varTxtFile))

