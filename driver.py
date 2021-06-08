import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from Home import HomePage
from CR_HomePage import CR_ShowHomePage

def login():
    email = e_email.get()
    password = e_password.get()
    con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
    cursor = con.cursor(buffered=True)
    cursor.execute("SELECT * FROM student WHERE email='"+email+"'")
    student_session = cursor.fetchone()

    if student_session is None:
        MessageBox.showinfo("Error", "Incorrect email")
    elif (student_session[5] == password):
        if (student_session[8] == 2):
            MessageBox.showinfo("Successfull", "Logged in!")
            root.destroy()
            HomePage(student_session[0])
        else:
            MessageBox.showinfo("great success", "Logged in!")
            root.destroy()
            CR_ShowHomePage(student_session[0])
    else:
        MessageBox.showinfo("Error", "Incorrect password")

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
root.configure(background="#f3efd6")
root.configure(highlightbackground="#d9d9d9")
root.configure(highlightcolor="black")

e_email = tk.StringVar()
e_password = tk.StringVar()

style = ttk.Style()
if sys.platform == "win32":
    style.theme_use('winnative')
style.configure('.',background='#d9d9d9')
style.configure('.',foreground='#000000')
style.configure('.',font="TkDefaultFont")
style.map('.',background=[('selected', '#d9d9d9'), ('active','#ececec')])

Message1 = tk.Message(root)
Message1.place(relx=0.008, rely=0.022, relheight=0.096, relwidth=0.983)
Message1.configure(background="#800040")
Message1.configure(font="-family {Imprint MT Shadow} -size 17 -weight bold")
Message1.configure(foreground="#ffffff")
Message1.configure(highlightbackground="#d9d9d9")
Message1.configure(highlightcolor="#800040")
Message1.configure(text='''KAKSHA''')
Message1.configure(width=590)

Message2 = tk.Message(root)
Message2.place(relx=0.117, rely=0.289, relheight=0.096, relwidth=0.217)
Message2.configure(background="#ebe3ba")
Message2.configure(borderwidth="11")
Message2.configure(font="-family {Segoe UI} -size 12 -weight bold")
Message2.configure(foreground="#000000")
Message2.configure(highlightbackground="#d9d9d9")
Message2.configure(highlightcolor="black")
Message2.configure(highlightthickness="1")
Message2.configure(text='''Enter e-mail id:''')
Message2.configure(width=130)

Message3 = tk.Message(root)
Message3.place(relx=0.517, rely=0.289, relheight=0.096, relwidth=0.217)
Message3.configure(background="#ebe3ba")
Message3.configure(borderwidth="11")
Message3.configure(font="-family {Segoe UI} -size 12 -weight bold")
Message3.configure(foreground="#000000")
Message3.configure(highlightbackground="#d9d9d9")
Message3.configure(highlightcolor="black")
Message3.configure(highlightthickness="1")
Message3.configure(text='''Enter password:''')
Message3.configure(width=130)

# Entry Box
TEntry1 = ttk.Entry(root, textvariable=e_email)
TEntry1.place(relx=0.117, rely=0.4, relheight=0.047, relwidth=0.343)
TEntry1.configure(takefocus="",font="-family {Segoe UI} -size 15")
TEntry1.configure(cursor="ibeam")

TEntry2 = ttk.Entry(root, textvariable=e_password, show="*")
TEntry2.place(relx=0.517, rely=0.4, relheight=0.047, relwidth=0.343)
TEntry2.configure(takefocus="",font="-family {Segoe UI} -size 15")
TEntry2.configure(cursor="ibeam")

TButton1 = ttk.Button(root, command=login)
TButton1.place(relx=0.7, rely=0.511, height=25, width=86)
TButton1.configure(takefocus="")
TButton1.configure(text='''LOGIN''')
TButton1.configure(cursor="arrow")
root.mainloop()
