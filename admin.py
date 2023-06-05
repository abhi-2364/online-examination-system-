from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from mysql.connector import errorcode
from mysql.connector import (connection)
import exam
import student
import subject
import instructor


class home:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x700+0+0")
        self.root.title('Online Exam Management System')

        lbl_title = Label(self.root, text='ONLINE EXAM MANAGEMENT SYSTEM', font=(
            'timens new roman', 36, 'bold'), fg='orange', bg='white')
        lbl_title.place(x=4, y=4, width=1250, height=50)

        img_logo = Image.open(
            'photos\logo.png')
        img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=126, y=4, width=50, height=50)
        # frame1
        image_frame1 = Frame(self.root, bd=0, relief=None, bg='white')
        image_frame1.place(x=0, y=50, width=1250, height=360)

        # Mainframe
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=0, y=300, width=1250, height=530)

        # upper frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='dumy text', font=(
            'timens new roman', 12, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1250, height=265)

        # Home
        img_home = Image.open(
            'photos\Home.png')
        img_home = img_home.resize((125, 125), Image.ANTIALIAS)
        self.photo1_logo = ImageTk.PhotoImage(img_home)

        self.home = Label(upper_frame, image=self.photo1_logo)
        self.home.grid(row=0, column=0, padx=25, pady=21, sticky=W)

        btn_Home = Button(upper_frame, text='Home', font=(
            "arial", 15, "bold"), width=10, bg='light green', fg='orange')
        btn_Home.grid(row=1, column=0, padx=10, pady=3)

        # student
        img_student = Image.open(
            'photos\Student-3-icon.png')
        img_student = img_student.resize((125, 125), Image.ANTIALIAS)
        self.photo2_logo = ImageTk.PhotoImage(img_student)

        self.student = Label(upper_frame, image=self.photo2_logo)
        self.student.grid(row=0, column=1, padx=25, pady=21, sticky=W)

        btn_student = Button(upper_frame, command=lambda: student.student.__init__(self, root), text='Student', font=(
            "arial", 15, "bold"), width=10, bg='light green', fg='orange')
        btn_student.grid(row=1, column=1, padx=10, pady=3)

        # subject
        img_subject = Image.open(
            'photos\subject.png')
        img_subject = img_subject.resize((125, 125), Image.ANTIALIAS)
        self.photo3_logo = ImageTk.PhotoImage(img_subject)

        self.subject = Label(upper_frame, image=self.photo3_logo)
        self.subject.grid(row=0, column=2, padx=25, pady=21, sticky=W)

        btn_subject = Button(upper_frame, command=lambda: subject.subject.__init__(self, root), text='Subject', font=(
            "arial", 15, "bold"), width=10, bg='light green', fg='orange')
        btn_subject.grid(row=1, column=2, padx=10, pady=3)

        # Exam
        img_exam = Image.open(
            'photos\Exam.png')
        img_exam = img_exam.resize((125, 125), Image.ANTIALIAS)
        self.photo4_logo = ImageTk.PhotoImage(img_exam)

        self.exam = Label(upper_frame, image=self.photo4_logo)
        self.exam.grid(row=0, column=3, padx=25, pady=21, sticky=W)

        btn_exam = Button(upper_frame, command=lambda: exam.exam.__init__(self, root), text='Exam', font=(
            "arial", 15, "bold"), width=10, bg='light green', fg='orange')
        btn_exam.grid(row=1, column=3, padx=10, pady=3)

        # Instructor
        img_instructor = Image.open(
            'photos\instructor.png')
        img_instructor = img_instructor.resize((125, 125), Image.ANTIALIAS)
        self.photo5_logo = ImageTk.PhotoImage(img_instructor)

        self.instructor = Label(upper_frame, image=self.photo5_logo)
        self.instructor.grid(row=0, column=3, padx=25, pady=21, sticky=W)

        btn_instructor = Button(upper_frame, command=lambda: instructor.instructor.__init__(self, root),  text='Instructor', font=(
            "arial", 15, "bold"), width=10, bg='light green', fg='orange')
        btn_instructor.grid(row=1, column=3, padx=10, pady=3)
        
         # down frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='dummy text', font=(
            'timens new roman', 12, 'bold'), fg='red')
        down_frame.place(x=10, y=275, width=1250, height=265)

if __name__ == "__main__":
    root = Tk()
    obj = home(root)
    root.mainloop()
