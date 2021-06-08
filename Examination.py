import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import ImageTk, Image

root = ""
student_session = []

def ExaminationPage(student_id):
    global root
    global student_session
    root = tk.Tk()
    root.maxsize(width=1280 ,  height=720)
    root.minsize(width=1280 ,  height=720)
    con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
    cursor = con.cursor(buffered=True)
    cursor.execute("SELECT * FROM student WHERE student_id='"+str(student_id)+"'")
    student_session = cursor.fetchone()

    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'

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
    title.configure(text="KAKSHA")
    title.configure(width=590)

    rightFrame = tk.Frame(root)
    rightFrame.place(relx=0.008, rely=0.13, relheight=0.877, relwidth=0.983)
    rightFrame.configure(relief='groove')
    rightFrame.configure(borderwidth="2")
    rightFrame.configure(relief="groove")
    rightFrame.configure(background="#e8dfae")
    rightFrame.configure(highlightbackground="#d9d9d9")
    rightFrame.configure(highlightcolor="black")

    

    root.mainloop()

if __name__ == "__main__":
    ExaminationPage(8)
