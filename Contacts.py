import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import ImageTk, Image

def ContactsPage(student_id):
    global student_session
    root_contacts = tk.Tk()
    root_contacts.maxsize(width=1280 ,  height=720)
    root_contacts.minsize(width=1280 ,  height=720)
    w = 1280
    h = 720
    ws = root_contacts.winfo_screenwidth()
    hs = root_contacts.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root_contacts.geometry('%dx%d+%d+%d' % (w, h, x, y))
    con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
    cursor = con.cursor(buffered=True)
    cursor.execute("SELECT * FROM student WHERE student_id='"+str(student_id)+"'")
    student_session = cursor.fetchone()

    cursor.execute("SELECT * FROM teaches WHERE class_id="+str(student_session[9]))
    teaches = cursor.fetchall()

    root_contacts.configure(background="#f3efd6")
    root_contacts.configure(highlightbackground="#d9d9d9")
    root_contacts.configure(highlightcolor="black")

    # title
    title = tk.Message(root_contacts)
    title.place(relx=0.008, rely=0.022, relheight=0.096, relwidth=0.983)
    title.configure(background="#800040")
    title.configure(font="-family {Imprint MT Shadow} -size 17 -weight bold")
    title.configure(foreground="#ffffff")
    title.configure(highlightbackground="#d9d9d9")
    title.configure(highlightcolor="#800040")
    title.configure(text="CONTACTS")
    title.configure(width=590)

    rightFrame = tk.Frame(root_contacts)
    rightFrame.place(relx=0.008, rely=0.13, relheight=0.877, relwidth=0.983)
    rightFrame.configure(relief='groove')
    rightFrame.configure(borderwidth="2")
    rightFrame.configure(relief="groove")
    rightFrame.configure(background="#e8dfae")
    rightFrame.configure(highlightbackground="#d9d9d9")
    rightFrame.configure(highlightcolor="black")

    i = 0
    for teach in teaches:
        cursor.execute("SELECT * FROM staff WHERE staff_id="+str(teach[1]))
        teacher = cursor.fetchone()

        cursor.execute("SELECT * FROM subject WHERE subject_id="+str(teach[3]))
        # print(teach[1],teach[2],teach[3],teach[1])
        subject = cursor.fetchone()

        printString = teacher[1]+" "+teacher[2]+" : : "+teacher[3]+" : : "+teacher[4]+"  : :  "+subject[1]

        l_teacher = tk.Label(rightFrame)
        l_teacher.place(relx=0.008, rely=0.022+i, relheight=0.096, relwidth=0.983)
        l_teacher.configure(relief='groove')
        l_teacher.configure(borderwidth="2")
        l_teacher.configure(background="#ffffff")
        l_teacher.configure(highlightbackground="#d9d9d9")
        l_teacher.configure(highlightcolor="black")
        l_teacher.configure(font="-family {Imprint MT Shadow} -size 12 -weight bold")
        l_teacher.configure(text=(printString))
        i = i+0.12

    root_contacts.mainloop()
