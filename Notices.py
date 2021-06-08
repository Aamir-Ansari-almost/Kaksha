import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import ImageTk, Image

def NoticesPage(student_id):
    global root
    global student_session
    root = tk.Tk()
    root.maxsize(width=1280 ,  height=720)
    root.minsize(width=1280 ,  height=720)
    w = 1280
    h = 720
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
    cursor = con.cursor(buffered=True)
    cursor.execute("SELECT * FROM student WHERE student_id='"+str(student_id)+"'")
    student_session = cursor.fetchone()

    cursor.execute("SELECT * FROM notice WHERE type=2 AND class_id="+str(student_session[9]))
    notices = cursor.fetchall()

    root.configure(background="#f3efd6")
    root.configure(highlightbackground="#d9d9d9")
    root.configure(highlightcolor="black")

    # title
    title = tk.Message(root)
    title.place(relx=0.008, rely=0.022, relheight=0.096, relwidth=0.983)
    title.configure(background="#800040")
    title.configure(font="-family {Imprint MT Shadow} -size 17 -weight bold")
    title.configure(foreground="#ffffff")
    title.configure(highlightbackground="#d9d9d9")
    title.configure(highlightcolor="#800040")
    title.configure(text="NOTICES")
    title.configure(width=590)

    rightFrame = tk.Frame(root)
    rightFrame.place(relx=0.008, rely=0.13, relheight=0.877, relwidth=0.983)
    rightFrame.configure(relief='groove')
    rightFrame.configure(borderwidth="2")
    rightFrame.configure(relief="groove")
    rightFrame.configure(background="#e8dfae")
    rightFrame.configure(highlightbackground="#d9d9d9")
    rightFrame.configure(highlightcolor="black")

    i = 0
    for notice in notices:
        l_notice = tk.Label(rightFrame)
        l_notice.place(relx=0.008, rely=0.022+i, relheight=0.096, relwidth=0.983)
        l_notice.configure(relief='groove')
        l_notice.configure(borderwidth="2")
        l_notice.configure(background="#ffffff")
        l_notice.configure(highlightbackground="#d9d9d9")
        l_notice.configure(highlightcolor="black")
        l_notice.configure(font="-family {Imprint MT Shadow} -size 12 -weight bold")
        l_notice.configure(text=(notice[1]+"\n"+notice[2]))
        i = i+0.12

    root.mainloop()

if __name__ == "__main__":
    NoticesPage(8)
