from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)
from datetime import date
import exam
import admin
import login


class studetail:
    def __init__(self, root):
        studetail.root = root
        studetail.root.geometry("1250x700+0+0")
        studetail.root.title('student landing page')

        studetail.x = StringVar()
        x = date.today()

        lbl_title = Label(studetail.root, text='ONLINE EXAM MANAGEMENT SYSTEM', font=(
            'timens new roman', 36, 'bold'), fg='orange', bg='light green')
        lbl_title.place(x=4, y=4, width=1250, height=50)

        img_logo = Image.open(
            'photos\logo.png')
        img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
        studetail.photo_logo = ImageTk.PhotoImage(img_logo)

        studetail.logo = Label(studetail.root, image=studetail.photo_logo)
        studetail.logo.place(x=126, y=4, width=50, height=50)
        # frame1
        image_frame = Frame(studetail.root, bd=0, relief=None, bg='white')
        image_frame.place(x=0, y=50, width=1250, height=360)

        # upper frame
        upper_frame = LabelFrame(studetail.root, bd=2, relief=RIDGE, bg='white', text='Scheduled Exams', font=(
            'timens new roman', 12, 'bold'), fg='red')
        upper_frame.place(x=10, y=300, width=1250, height=150)

        table_frame = Frame(upper_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=15, width=1250, height=100)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        studetail.studetail_table = ttk.Treeview(table_frame, columns=(
            "1", "2", "3", "4", "5", "6", "7"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=studetail.studetail_table.xview)
        scroll_y.config(command=studetail.studetail_table.yview)

        studetail.studetail_table.heading('1', text='Exam_ID')
        studetail.studetail_table.heading('2', text='Subject_ID')
        studetail.studetail_table.heading('3', text='Instructor_ID')
        studetail.studetail_table.heading('4', text='Exam_Link')
        studetail.studetail_table.heading('5', text='Duration')
        studetail.studetail_table.heading('6', text='Start_time')
        studetail.studetail_table.heading('7', text='Date')

        studetail.studetail_table['show'] = 'headings'

        studetail.studetail_table.column('1', width=100)
        studetail.studetail_table.column('2', width=100)
        studetail.studetail_table.column('3', width=100)
        studetail.studetail_table.column('4', width=180)
        studetail.studetail_table.column('5', width=100)
        studetail.studetail_table.column('6', width=100)
        studetail.studetail_table.column('7', width=100)

        studetail.studetail_table.pack(fill=BOTH, expand=1)

        studetail.fetch(self, x)
        root.mainloop()

    def fetch(self, x):
        cnx = mysql.connector.connect(
            host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
        my_cursor = cnx.cursor()
        my_cursor.execute('SELECT * From exam WHERE Date=%s', (x,))
        data = my_cursor.fetchall()
        if len(data) != 0:
            studetail.studetail_table.delete(
                *studetail.studetail_table.get_children())
            for i in data:
                studetail.studetail_table.insert("", END, values=i)
        cnx.commit()
        cnx.close()

        # down frame
        down_frame = LabelFrame(studetail.root, bd=2, relief=RIDGE, bg='white', text='Marks', font=(
            'timens new roman', 12, 'bold'), fg='red')
        down_frame.place(x=10, y=500, width=1250, height=250)

        table1_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table1_frame.place(x=0, y=15, width=1250, height=100)

        scroll1_x = ttk.Scrollbar(table1_frame, orient=HORIZONTAL)
        scroll1_y = ttk.Scrollbar(table1_frame, orient=VERTICAL)

        studetail.markss_table = ttk.Treeview(table1_frame, columns=(
            "1", "2", "3", "4"), xscrollcommand=scroll1_x.set, yscrollcommand=scroll1_y.set)

        scroll1_x.pack(side=BOTTOM, fill=X)
        scroll1_y.pack(side=RIGHT, fill=Y)

        scroll1_x.config(command=studetail.markss_table.xview)
        scroll1_y.config(command=studetail.markss_table.yview)

        studetail.markss_table.heading('1', text='Exam_ID')
        studetail.markss_table.heading('2', text='Subject_ID')
        studetail.markss_table.heading('3', text='Exam_Name')
        studetail.markss_table.heading('4', text='Marks')

        studetail.markss_table['show'] = 'headings'

        studetail.markss_table.column('1', width=100)
        studetail.markss_table.column('2', width=100)
        studetail.markss_table.column('3', width=100)
        studetail.markss_table.column('4', width=180)

        studetail.markss_table.pack(fill=BOTH, expand=1)

        studetail.fetch2()
        root.mainloop()

    def fetch2():
        
        cnx = mysql.connector.connect(
            host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
        my_cursor = cnx.cursor()
        my_cursor.execute(
            'SELECT Exam_ID,Subject_ID,Exam_Name,Marks FROM marks WHERE Registration_Number = %s', ('CH.EN.U4CSE21010' ,))
        data = my_cursor.fetchall()
        if len(data) != 0:
            studetail.markss_table.delete(
                *studetail.markss_table.get_children())
            for i in data:
                studetail.markss_table.insert("", END, values=i)
        cnx.commit()
        cnx.close()


if __name__ == "__main__":
    root = Tk()
    obj = studetail(root)
    root.mainloop()
