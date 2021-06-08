import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import ImageTk, Image
from DisplayPDF import DisplayPdf
from Examination import ExaminationPage
from Notices import NoticesPage
from tkPDFViewer import tkPDFViewer as pdf
from multiprocessing import Process

def callContacts():
    pass

def callMarks():
    pass

def callAssignments():
    # root.destroy()
    pass

def showNotes():
    pass

def callNotices():
    pass

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

root = ""
student_session = []

def showMarks(exam_fullname):
    con = mysql.connect(host="localhost", user="root", password="", database="kaksha")
    cursor = con.cursor(buffered=True)

    cursor.execute("SELECT * FROM exam WHERE exam_fullname='"+str(exam_fullname)+"'")
    currentExams = cursor.fetchall()

    subjectNames = []
    subjectMarks = []
    for exam in currentExams:
        cursor.execute("SELECT * FROM subject WHERE subject_id='"+str(exam[2])+"'")
        temp = cursor.fetchone()
        subjectNames.append(temp[4])

        cursor.execute("SELECT * FROM result WHERE student_id='"+str(student_session[0])+"' AND exam_id='"+str(exam[0])+"'")
        temp = cursor.fetchone()
        subjectMarks.append(temp[3])

    root2 = tk.Tk()
    root2.maxsize(width=1280 ,  height=720)
    root2.minsize(width=1280 ,  height=720)
    w = 1280
    h = 720
    ws = root2.winfo_screenwidth()
    hs = root2.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root2.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root2.configure(background="#f3efd6")
    root2.configure(highlightbackground="#d9d9d9")
    root2.configure(highlightcolor="black")

    # title
    title = tk.Message(root2)
    title.place(relx=0.008, rely=0.022, relheight=0.096, relwidth=0.983)
    title.configure(background="#800040")
    title.configure(font="-family {Imprint MT Shadow} -size 17 -weight bold")
    title.configure(foreground="#ffffff")
    title.configure(highlightbackground="#d9d9d9")
    title.configure(highlightcolor="#800040")
    title.configure(text=exam_fullname)
    title.configure(width=590)

    rightFrame = tk.Frame(root2)
    rightFrame.place(relx=0.008, rely=0.13, relheight=0.877, relwidth=0.983)
    rightFrame.configure(relief='groove')
    rightFrame.configure(borderwidth="2")
    rightFrame.configure(relief="groove")
    rightFrame.configure(background="#e8dfae")
    rightFrame.configure(highlightbackground="#d9d9d9")
    rightFrame.configure(highlightcolor="black")

    i = 0
    for name, marks in zip(subjectNames, subjectMarks):
        l_notice = tk.Label(rightFrame)

        left_alignment = name
        left_alignment2 = left_alignment.ljust(40, " ")
        right_alignment = str(int(marks))+" / 20"
        displayString = f"{left_alignment2 : <160}{right_alignment}"

        # displayString = 

        l_notice.place(relx=0.008, rely=0.022+i, relheight=0.096, relwidth=0.983)
        l_notice.configure(relief='groove')
        l_notice.configure(borderwidth="2")
        l_notice.configure(background="#ffffff")
        l_notice.configure(highlightbackground="#d9d9d9")
        l_notice.configure(highlightcolor="black")
        l_notice.configure(font="-family {Imprint MT Shadow} -size 12 -weight bold")
        l_notice.configure(text=displayString)
        print(name, marks)
        i = i+0.12

    root2.mainloop()

def MarksPage(student_id):
    global root
    global student_session
    root = tk.Tk()
    root.maxsize(width=1280 ,  height=720)
    root.minsize(width=1280 ,  height=720)
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
    
    cursor.execute("SELECT * FROM exam WHERE class_id='"+str(student_session[9])+"' GROUP BY exam_name")
    examNames_session = cursor.fetchall()

    # cursor.execute("SELECT * FROM subject WHERE branch_id='"+str(class_session[3])+"' AND semester='"+str(class_session[2])+"'")
    # subject_session = cursor.fetchall()

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

    b_timetable = tk.Button(leftFrame, command=callTimeTable)
    b_timetable.place(relx=0.019, rely=0.099, height=34, width=187)
    b_timetable.configure(activebackground="#9d004f")
    b_timetable.configure(activeforeground="white")
    b_timetable.configure(activeforeground="#ffffff")
    b_timetable.configure(background="#ae0057")
    b_timetable.configure(disabledforeground="#a3a3a3")
    b_timetable.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
    b_timetable.configure(foreground="#ffffff")
    b_timetable.configure(highlightbackground="#d9d9d9")
    b_timetable.configure(highlightcolor="black")
    b_timetable.configure(pady="0")
    b_timetable.configure(text='''Timetable''')

    b_notice = tk.Button(leftFrame, command=callNotices)
    b_notice.place(relx=0.019, rely=0.198, height=34, width=187)
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
    b_notes.place(relx=0.019, rely=0.296, height=34, width=187)
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

    b_contacts = tk.Button(leftFrame, command=callContacts)
    b_contacts.place(relx=0.019, rely=0.395, height=34, width=187)
    b_contacts.configure(activebackground="#9d004f")
    b_contacts.configure(activeforeground="white")
    b_contacts.configure(activeforeground="#ffffff")
    b_contacts.configure(background="#ae0057")
    b_contacts.configure(disabledforeground="#a3a3a3")
    b_contacts.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
    b_contacts.configure(foreground="#ffffff")
    b_contacts.configure(highlightbackground="#d9d9d9")
    b_contacts.configure(highlightcolor="black")
    b_contacts.configure(pady="0")
    b_contacts.configure(text='''Contacts''')

    b_marks = tk.Button(leftFrame, command=callMarks)
    b_marks.place(relx=0.019, rely=0.494, height=34, width=187)
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
    b_assignments.place(relx=0.019, rely=0.593, height=34, width=187)
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

    def select():
        showMarks(examNamesListbox.get(examNamesListbox.curselection()))

    examNamesListbox = tk.Listbox(root, font = "Helvetica", width=47, height=3)
    i=1
    for exam in examNames_session:
        examNamesListbox.insert(i, exam[4])
    examNamesListbox.pack(padx=5, pady=250)

    b_select = tk.Button(rightFrame, command=select)
    b_select.place(relx=0.3, rely=0.43, height=34, width=187)
    b_select.configure(activebackground="#9d004f")
    b_select.configure(activeforeground="white")
    b_select.configure(activeforeground="#ffffff")
    b_select.configure(background="#ae0057")
    b_select.configure(disabledforeground="#a3a3a3")
    b_select.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
    b_select.configure(foreground="#ffffff")
    b_select.configure(highlightbackground="#d9d9d9")
    b_select.configure(highlightcolor="black")
    b_select.configure(pady="0")
    b_select.configure(text='''Select''')

    root.mainloop()

if __name__ == "__main__":
    MarksPage(1)
