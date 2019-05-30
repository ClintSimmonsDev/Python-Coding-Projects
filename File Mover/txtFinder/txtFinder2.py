import sqlite3

conn = sqlite3.connect("txtFinder.db")

fileList =('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
txtFiles = []

for i in fileList:
    if i not in txtFiles and i.endswith(".txt"):
        txtFiles.append(i)

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_VarFiles(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
    col_Files TEXT)")
    conn.commit()

    cur.executemany("INSERT INTO tbl_VarFiles(col_Files) VALUES (?)",
                    [(x,) for x in txtFiles])

    cur.execute("SELECT DISTINCT col_Files FROM tbl_VarFiles")

    varTxtFile = cur.fetchall()

    print("\nThe following files in database txtFinder are .txt files:\n" + str(varTxtFile))

