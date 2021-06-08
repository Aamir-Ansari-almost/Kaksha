import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import ImageTk, Image
from Examination import ExaminationPage
from Notices import NoticesPage
from Notes import NotesPage
from Assignments import AssignmentsPage
from Marks import MarksPage
from tkinter.filedialog import askopenfilename

root = ""
student_session = []
rightFrame = ""
exam_id=1
def callMarks():
    root_marks = tk.Tk()
    root_marks.maxsize(width=1280 ,  height=720)
    root_marks.minsize(width=1280 ,  height=720)
    w = 1280
    h = 720
    ws = root_marks.winfo_screenwidth()
    hs = root_marks.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root_marks.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root_marks.configure(background="#f3efd6")
    root_marks.configure(highlightbackground="#d9d9d9")
    root_marks.configure(highlightcolor="black")

    title = tk.Message(root_marks)
    title.place(relx=0.008, rely=0.022, relheight=0.096, relwidth=0.983)
    title.configure(background="#800040")
    title.configure(font="-family {Imprint MT Shadow} -size 17 -weight bold")
    title.configure(foreground="#ffffff")
    title.configure(highlightbackground="#d9d9d9")
    title.configure(highlightcolor="#800040")
    title.configure(text="KAKSHA")
    title.configure(width=590)

    rightFrame = tk.Frame(root_marks)
    rightFrame.place(relx=0.008, rely=0.13, relheight=0.877, relwidth=0.983)
    rightFrame.configure(relief='groove')
    rightFrame.configure(borderwidth="2")
    rightFrame.configure(relief="groove")
    rightFrame.configure(background="#e8dfae")
    rightFrame.configure(highlightbackground="#d9d9d9")
    rightFrame.configure(highlightcolor="black")

    con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
    cursor = con.cursor(buffered=True)
    cursor.execute('SELECT * FROM exam WHERE class_id="%s" GROUP BY exam_fullname' %(student_session[9]))
    exam_names = cursor.fetchall()

    def select_exam():
        global exam_id
        exam_id=1
        print(examNamesListbox.get(examNamesListbox.curselection()))
        if (examNamesListbox.get(examNamesListbox.curselection()) == "IA-2"):
            exam_id=7
        print(exam_id)
        def submitMarks():
            global exam_id
            print(str(int(exam_id)))
            cursor.execute('INSERT INTO result (student_id, exam_id, marks, out_of) VALUES ("%s","%s","%s","%s")' %(e7.get(), str(int(exam_id)), e1.get(), "20"))
            con.commit()
            exam_id+=1
            print(exam_id)
            cursor.execute('INSERT INTO result (student_id, exam_id, marks, out_of) VALUES ("%s","%s","%s","%s")' %(e7.get(), str(int(exam_id)), e2.get(), "20"))
            con.commit()
            exam_id+=1
            cursor.execute('INSERT INTO result (student_id, exam_id, marks, out_of) VALUES ("%s","%s","%s","%s")' %(e7.get(), str(int(exam_id)), e3.get(), "20"))
            con.commit()
            exam_id+=1
            cursor.execute('INSERT INTO result (student_id, exam_id, marks, out_of) VALUES ("%s","%s","%s","%s")' %(e7.get(), str(int(exam_id)), e4.get(), "20"))
            con.commit()
            exam_id+=1
            cursor.execute('INSERT INTO result (student_id, exam_id, marks, out_of) VALUES ("%s","%s","%s","%s")' %(e7.get(), str(int(exam_id)), e5.get(), "20"))
            con.commit()
            exam_id+=1
            cursor.execute('INSERT INTO result (student_id, exam_id, marks, out_of) VALUES ("%s","%s","%s","%s")' %(e7.get(), str(int(exam_id)), e6.get(), "20"))
            con.commit()
            MessageBox.showinfo("Marks added", "Success!")
        
        
        root_select_exam = tk.Tk()
        root_select_exam.maxsize(width=1280 ,  height=720)
        root_select_exam.minsize(width=1280 ,  height=720)
        w = 1280
        h = 720
        ws = root_select_exam.winfo_screenwidth()
        hs = root_select_exam.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root_select_exam.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root_select_exam.configure(background="#f3efd6")
        root_select_exam.configure(highlightbackground="#d9d9d9")
        root_select_exam.configure(highlightcolor="black")

        title = tk.Message(root_select_exam)
        title.place(relx=0.008, rely=0.022, relheight=0.096, relwidth=0.983)
        title.configure(background="#800040")
        title.configure(font="-family {Imprint MT Shadow} -size 17 -weight bold")
        title.configure(foreground="#ffffff")
        title.configure(highlightbackground="#d9d9d9")
        title.configure(highlightcolor="#800040")
        title.configure(text="KAKSHA")
        title.configure(width=590)

        rightFrame = tk.Frame(root_select_exam)
        rightFrame.place(relx=0.008, rely=0.13, relheight=0.877, relwidth=0.983)
        rightFrame.configure(relief='groove')
        rightFrame.configure(borderwidth="2")
        rightFrame.configure(relief="groove")
        rightFrame.configure(background="#e8dfae")
        rightFrame.configure(highlightbackground="#d9d9d9")
        rightFrame.configure(highlightcolor="black")

        exam_name = examNamesListbox.get(examNamesListbox.curselection())
        con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
        cursor = con.cursor(buffered=True)
        cursor.execute('SELECT * FROM class WHERE class_id="%s"' %(student_session[9]))
        branch_id = cursor.fetchone()

        cursor.execute('SELECT * FROM subject WHERE branch_id="%s"' %(branch_id[3]))
        subjects = cursor.fetchall()

        label1 = tk.Label(rightFrame, text=subjects[0][1], width=13, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))
        label2 = tk.Label(rightFrame, text=subjects[1][1], width=13, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=4, padx=(10,0))
        label3 = tk.Label(rightFrame, text=subjects[2][1], width=13, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))
        label4 = tk.Label(rightFrame, text=subjects[3][1], width=13, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=4, padx=(10,0))
        label5 = tk.Label(rightFrame, text=subjects[4][1], width=13, anchor='w', font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))
        label6 = tk.Label(rightFrame, text=subjects[5][1], width=13, anchor='w', font=("Sylfaen", 12)).grid(row=3, column=4, padx=(10,0))
        label7 = tk.Label(rightFrame, text="Student id", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=4, column=2, padx=(10,0))

        e1 = tk.Entry(rightFrame, width=20,font=("Sylfaen", 12))
        e1.grid(row=1, column=1, padx=(0,10), pady = 20)
        e2 = tk.Entry(rightFrame, width=20,font=("Sylfaen", 12))
        e2.grid(row=1, column=5, padx=(0,10), pady = 20)
        e3 = tk.Entry(rightFrame, width=20,font=("Sylfaen", 12))
        e3.grid(row=2, column=1, padx=(0,10), pady = 20)
        e4 = tk.Entry(rightFrame, width=20,font=("Sylfaen", 12))
        e4.grid(row=2, column=5, padx=(0,10), pady = 20)
        e5 = tk.Entry(rightFrame, width=20,font=("Sylfaen", 12))
        e5.grid(row=3, column=1, padx=(0,10), pady = 20)
        e6 = tk.Entry(rightFrame, width=20,font=("Sylfaen", 12))
        e6.grid(row=3, column=5, padx=(0,10), pady = 20)
        e7 = tk.Entry(rightFrame, width=20,font=("Sylfaen", 12))
        e7.grid(row=4, column=3, padx=(0,10), pady = 20)

        b_submit = tk.Button(rightFrame, command=submitMarks)
        b_submit.place(relx=0.3, rely=0.53, height=34, width=187)
        b_submit.configure(activebackground="#9d004f")
        b_submit.configure(activeforeground="white")
        b_submit.configure(activeforeground="#ffffff")
        b_submit.configure(background="#ae0057")
        b_submit.configure(disabledforeground="#a3a3a3")
        b_submit.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
        b_submit.configure(foreground="#ffffff")
        b_submit.configure(highlightbackground="#d9d9d9")
        b_submit.configure(highlightcolor="black")
        b_submit.configure(pady="0")
        b_submit.configure(text='''Select''')

    examNamesListbox = tk.Listbox(rightFrame, font = "Helvetica", width=47, height=len(exam_names)+1)
    i=1
    for name in exam_names:
        examNamesListbox.insert(i, name[1])
    examNamesListbox.grid(padx=380, pady=150)
    
    b_select_exam = tk.Button(rightFrame, command=select_exam)
    b_select_exam.place(relx=0.3, rely=0.53, height=34, width=187)
    b_select_exam.configure(activebackground="#9d004f")
    b_select_exam.configure(activeforeground="white")
    b_select_exam.configure(activeforeground="#ffffff")
    b_select_exam.configure(background="#ae0057")
    b_select_exam.configure(disabledforeground="#a3a3a3")
    b_select_exam.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
    b_select_exam.configure(foreground="#ffffff")
    b_select_exam.configure(highlightbackground="#d9d9d9")
    b_select_exam.configure(highlightcolor="black")
    b_select_exam.configure(pady="0")
    b_select_exam.configure(text='''Select''')

# -----------------------------------------------------------------------------------------
def callAssignments():
    # root.destroy()
    # AssignmentsPage(student_session[0])
    pass
    
def showNotes():
    root_notes = tk.Tk()
    root_notes.maxsize(width=1280 ,  height=720)
    root_notes.minsize(width=1280 ,  height=720)
    w = 1280
    h = 720
    ws = root_notes.winfo_screenwidth()
    hs = root_notes.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root_notes.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root_notes.configure(background="#f3efd6")
    root_notes.configure(highlightbackground="#d9d9d9")
    root_notes.configure(highlightcolor="black")

    title = tk.Message(root_notes)
    title.place(relx=0.008, rely=0.022, relheight=0.096, relwidth=0.983)
    title.configure(background="#800040")
    title.configure(font="-family {Imprint MT Shadow} -size 17 -weight bold")
    title.configure(foreground="#ffffff")
    title.configure(highlightbackground="#d9d9d9")
    title.configure(highlightcolor="#800040")
    title.configure(text="KAKSHA")
    title.configure(width=590)

    rightFrame = tk.Frame(root_notes)
    rightFrame.place(relx=0.008, rely=0.13, relheight=0.877, relwidth=0.983)
    rightFrame.configure(relief='groove')
    rightFrame.configure(borderwidth="2")
    rightFrame.configure(relief="groove")
    rightFrame.configure(background="#e8dfae")
    rightFrame.configure(highlightbackground="#d9d9d9")
    rightFrame.configure(highlightcolor="black")

    con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
    cursor = con.cursor(buffered=True)
    cursor.execute('SELECT * FROM notes WHERE class_id="%s"' %(student_session[9]))
    notes = cursor.fetchall()

    def delete():
        notes_name = notesListbox.get(notesListbox.curselection())
        con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
        cursor = con.cursor(buffered=True)
        cursor.execute('DELETE FROM notes WHERE notes_name="%s"' %(notes_name))
        con.commit()
        root_notes.destroy()
        MessageBox.showinfo("Notes deleted", "Done!")

    def create():
        def createNotes():
            notes_name = e1.get()
            notes_path = e2.get()
            con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
            cursor = con.cursor(buffered=True)
            cursor.execute('INSERT INTO notes (notes_name, notes_pdf, class_id, subject_id) VALUES ("%s", "%s", "%s", "1")' %(notes_name, notes_path, student_session[9]))
            con.commit()
            MessageBox.showinfo("Notes Created!!", "Done!")
            root_create.destroy()

        root_create = tk.Tk()
        root_create.title("Create notice")
        root_create.geometry("850x360")
        root_create.configure(background="#f3efd6")
        root_create.configure(highlightbackground="#d9d9d9")
        root_create.configure(highlightcolor="black")
        root_notes.destroy()

        def browsefunc():
            filename = askopenfilename(filetypes=(("pdf file", "*.pdf"), ("png file",'*.png'), ("All files", "*.*"),))
            e2.insert(tk.END, filename)

        label1 = tk.Label(root_create, text="Notes name", width=13, anchor='w', font=("Sylfaen", 12)).place(relx=0.117, rely=0.15, relheight=0.096, relwidth=0.217)
        label2 = tk.Label(root_create, text="notes_path", width=13, anchor='w', font=("Sylfaen", 12)).place(relx=0.117, rely=0.3, relheight=0.096, relwidth=0.217)
        e1 = tk.Entry(root_create, width=20, font=("Sylfaen", 15))
        e1.place(relx=0.29, rely=0.15, relheight=0.096, relwidth=0.5)
        
        b1=tk.Button(root_create,text="Browse",font=40,command=browsefunc)
        b1.place(relx=0.56, rely=0.55, height=34, width=187)

        e2 = tk.Entry(root_create, width=80, font=("Sylfaen", 15))
        e2.place(relx=0.29, rely=0.3, relheight=0.2, relwidth=0.5)

        b_create = tk.Button(root_create, command=createNotes)
        b_create.place(relx=0.3, rely=0.55, height=34, width=187)
        b_create.configure(activebackground="#9d004f")
        b_create.configure(activeforeground="white")
        b_create.configure(activeforeground="#ffffff")
        b_create.configure(background="#ae0057")
        b_create.configure(disabledforeground="#a3a3a3")
        b_create.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
        b_create.configure(foreground="#ffffff")
        b_create.configure(highlightbackground="#d9d9d9")
        b_create.configure(highlightcolor="black")
        b_create.configure(pady="0")
        b_create.configure(text='''Create''')

    notesListbox = tk.Listbox(rightFrame, font = "Helvetica", width=47, height=len(notes)+1)
    i=1
    for note in notes:
        notesListbox.insert(i, note[1])
    notesListbox.grid(padx=380, pady=150)
    
    b_delete = tk.Button(rightFrame, command=delete)
    b_delete.place(relx=0.3, rely=0.53, height=34, width=187)
    b_delete.configure(activebackground="#9d004f")
    b_delete.configure(activeforeground="white")
    b_delete.configure(activeforeground="#ffffff")
    b_delete.configure(background="#ae0057")
    b_delete.configure(disabledforeground="#a3a3a3")
    b_delete.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
    b_delete.configure(foreground="#ffffff")
    b_delete.configure(highlightbackground="#d9d9d9")
    b_delete.configure(highlightcolor="black")
    b_delete.configure(pady="0")
    b_delete.configure(text='''Delete''')

    b_create = tk.Button(rightFrame, command=create)
    b_create.place(relx=0.5, rely=0.53, height=34, width=187)
    b_create.configure(activebackground="#9d004f")
    b_create.configure(activeforeground="white")
    b_create.configure(activeforeground="#ffffff")
    b_create.configure(background="#ae0057")
    b_create.configure(disabledforeground="#a3a3a3")
    b_create.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
    b_create.configure(foreground="#ffffff")
    b_create.configure(highlightbackground="#d9d9d9")
    b_create.configure(highlightcolor="black")
    b_create.configure(pady="0")
    b_create.configure(text='''Create''')
    
# --------------------------------------------------------------------
def callNotices():
    root_notice = tk.Tk()
    root_notice.maxsize(width=1280 ,  height=720)
    root_notice.minsize(width=1280 ,  height=720)
    w = 1280
    h = 720
    ws = root_notice.winfo_screenwidth()
    hs = root_notice.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root_notice.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
    cursor = con.cursor(buffered=True)
    cursor.execute('SELECT * FROM notice WHERE class_id="%s" AND type="%s"' %(student_session[9], str(2)))
    notices = cursor.fetchall()

    root_notice.configure(background="#f3efd6")
    root_notice.configure(highlightbackground="#d9d9d9")
    root_notice.configure(highlightcolor="black")

    title = tk.Message(root_notice)
    title.place(relx=0.008, rely=0.022, relheight=0.096, relwidth=0.983)
    title.configure(background="#800040")
    title.configure(font="-family {Imprint MT Shadow} -size 17 -weight bold")
    title.configure(foreground="#ffffff")
    title.configure(highlightbackground="#d9d9d9")
    title.configure(highlightcolor="#800040")
    title.configure(text="KAKSHA")
    title.configure(width=590)

    rightFrame = tk.Frame(root_notice)
    rightFrame.place(relx=0.008, rely=0.13, relheight=0.877, relwidth=0.983)
    rightFrame.configure(relief='groove')
    rightFrame.configure(borderwidth="2")
    rightFrame.configure(relief="groove")
    rightFrame.configure(background="#e8dfae")
    rightFrame.configure(highlightbackground="#d9d9d9")
    rightFrame.configure(highlightcolor="black")

    def delete():
        notice_title = noticesListbox.get(noticesListbox.curselection())
        con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
        cursor = con.cursor(buffered=True)
        cursor.execute('DELETE FROM notice WHERE notice_title="%s"' %(notice_title))
        con.commit()
        root_notice.destroy()
        MessageBox.showinfo("Notice deleted", "Done!")

    def create():
        def createNotice():
            notice_title = e1.get()
            notice_description = e2.get()
            con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
            cursor = con.cursor(buffered=True)
            cursor.execute('INSERT INTO notice (notice_title, notice_description, class_id, type) VALUES ("%s", "%s", "%s", "2")' %(notice_title, notice_description, student_session[9]))
            con.commit()
            MessageBox.showinfo("Notice Created!!", "Done!")
            root_create.destroy()

        root_create = tk.Tk()
        root_create.title("Create notice")
        root_create.geometry("850x360")
        root_create.configure(background="#f3efd6")
        root_create.configure(highlightbackground="#d9d9d9")
        root_create.configure(highlightcolor="black")
        root_notice.destroy()

        label1 = tk.Label(root_create, text="Title", width=13, anchor='w', font=("Sylfaen", 12)).place(relx=0.117, rely=0.15, relheight=0.096, relwidth=0.217)
        label2 = tk.Label(root_create, text="Description", width=13, anchor='w', font=("Sylfaen", 12)).place(relx=0.117, rely=0.3, relheight=0.096, relwidth=0.217)
        e1 = tk.Entry(root_create, width=20, font=("Sylfaen", 15))
        e1.place(relx=0.29, rely=0.15, relheight=0.096, relwidth=0.5)
        e2 = tk.Entry(root_create, width=80, font=("Sylfaen", 15))
        e2.place(relx=0.29, rely=0.3, relheight=0.2, relwidth=0.5)

        b_create = tk.Button(root_create, command=createNotice)
        b_create.place(relx=0.3, rely=0.55, height=34, width=187)
        b_create.configure(activebackground="#9d004f")
        b_create.configure(activeforeground="white")
        b_create.configure(activeforeground="#ffffff")
        b_create.configure(background="#ae0057")
        b_create.configure(disabledforeground="#a3a3a3")
        b_create.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
        b_create.configure(foreground="#ffffff")
        b_create.configure(highlightbackground="#d9d9d9")
        b_create.configure(highlightcolor="black")
        b_create.configure(pady="0")
        b_create.configure(text='''Create''')


    noticesListbox = tk.Listbox(rightFrame, font = "Helvetica", width=47, height=len(notices)+1)
    i=1
    for notice in notices:
        noticesListbox.insert(i, notice[1])
    noticesListbox.grid(padx=380, pady=150)

    b_delete = tk.Button(rightFrame, command=delete)
    b_delete.place(relx=0.3, rely=0.53, height=34, width=187)
    b_delete.configure(activebackground="#9d004f")
    b_delete.configure(activeforeground="white")
    b_delete.configure(activeforeground="#ffffff")
    b_delete.configure(background="#ae0057")
    b_delete.configure(disabledforeground="#a3a3a3")
    b_delete.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
    b_delete.configure(foreground="#ffffff")
    b_delete.configure(highlightbackground="#d9d9d9")
    b_delete.configure(highlightcolor="black")
    b_delete.configure(pady="0")
    b_delete.configure(text='''Delete''')

    b_create = tk.Button(rightFrame, command=create)
    b_create.place(relx=0.5, rely=0.53, height=34, width=187)
    b_create.configure(activebackground="#9d004f")
    b_create.configure(activeforeground="white")
    b_create.configure(activeforeground="#ffffff")
    b_create.configure(background="#ae0057")
    b_create.configure(disabledforeground="#a3a3a3")
    b_create.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
    b_create.configure(foreground="#ffffff")
    b_create.configure(highlightbackground="#d9d9d9")
    b_create.configure(highlightcolor="black")
    b_create.configure(pady="0")
    b_create.configure(text='''Create''')

def callTimeTable():
    con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
    cursor = con.cursor(buffered=True)
    cursor.execute("SELECT * FROM notice WHERE type=1 AND class_id="+str(student_session[9]))
    tt = cursor.fetchone()
    load = Image.open(tt[5])
    render = ImageTk.PhotoImage(load)
    img = tk.Label(root, image=render)
    img.image = render
    img.place(x=300, y=120)

def CR_ShowHomePage(student_id):
    # HomePage.student_id = student_id
    global root
    global student_session
    global rightFrame
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

    leftFrame = tk.Frame(root)
    leftFrame.place(relx=0.008, rely=0.13, relheight=0.877, relwidth=0.155)
    leftFrame.configure(relief='groove')
    leftFrame.configure(borderwidth="2")
    leftFrame.configure(relief="groove")
    leftFrame.configure(background="#e8dfae")
    leftFrame.configure(highlightbackground="#d9d9d9")
    leftFrame.configure(highlightcolor="black")

    rightFrame = tk.Frame(root)
    rightFrame.place(relx=0.17, rely=0.13, relheight=0.877, relwidth=0.821)
    rightFrame.configure(relief='groove')
    rightFrame.configure(borderwidth="2")
    rightFrame.configure(relief="groove")
    rightFrame.configure(background="#e8dfae")
    rightFrame.configure(highlightbackground="#d9d9d9")
    rightFrame.configure(highlightcolor="black")

    b_notice = tk.Button(leftFrame, command=callNotices)
    b_notice.place(relx=0.019, rely=0.099, height=34, width=187)
    b_notice.configure(activebackground="#9d004f")
    b_notice.configure(activeforeground="white")
    b_notice.configure(activeforeground="#ffffff")
    b_notice.configure(background="#ae0057")
    b_notice.configure(disabledforeground="#a3a3a3")
    b_notice.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
    b_notice.configure(foreground="#ffffff")
    b_notice.configure(highlightbackground="#d9d9d9")
    b_notice.configure(highlightcolor="black")
    b_notice.configure(pady="0")
    b_notice.configure(text='''Notice''')

    b_notes = tk.Button(leftFrame, command=showNotes)
    b_notes.place(relx=0.019, rely=0.198, height=34, width=187)
    b_notes.configure(activebackground="#9d004f")
    b_notes.configure(activeforeground="white")
    b_notes.configure(activeforeground="#ffffff")
    b_notes.configure(background="#ae0057")
    b_notes.configure(disabledforeground="#a3a3a3")
    b_notes.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
    b_notes.configure(foreground="#ffffff")
    b_notes.configure(highlightbackground="#d9d9d9")
    b_notes.configure(highlightcolor="black")
    b_notes.configure(pady="0")
    b_notes.configure(text='''Notes''')

    b_marks = tk.Button(leftFrame, command=callMarks)
    b_marks.place(relx=0.019, rely=0.296, height=34, width=187)
    b_marks.configure(activebackground="#9d004f")
    b_marks.configure(activeforeground="white")
    b_marks.configure(activeforeground="#ffffff")
    b_marks.configure(background="#ae0057")
    b_marks.configure(disabledforeground="#a3a3a3")
    b_marks.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
    b_marks.configure(foreground="#ffffff")
    b_marks.configure(highlightbackground="#d9d9d9")
    b_marks.configure(highlightcolor="black")
    b_marks.configure(pady="0")
    b_marks.configure(text='''Marks''')

    b_assignments = tk.Button(leftFrame, command=callAssignments)
    b_assignments.place(relx=0.019, rely=0.395, height=34, width=187)
    b_assignments.configure(activebackground="#9d004f")
    b_assignments.configure(activeforeground="white")
    b_assignments.configure(activeforeground="#ffffff")
    b_assignments.configure(background="#ae0057")
    b_assignments.configure(disabledforeground="#a3a3a3")
    b_assignments.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
    b_assignments.configure(foreground="#ffffff")
    b_assignments.configure(highlightbackground="#d9d9d9")
    b_assignments.configure(highlightcolor="black")
    b_assignments.configure(pady="0")
    b_assignments.configure(text='''Assignments''')

    root.mainloop()

if __name__ == "__main__":
    CR_ShowHomePage(8)
