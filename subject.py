from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)
import student
import exam
import admin
import instructor


class subject:
    def __init__(self, root):
        subject.root = root
        subject.root.geometry("1250x700+0+0")
        subject.root.title('Subject')

        lbl_title = Label(subject.root, text='ONLINE EXAM MANAGEMENT SYSTEM', font=(
            'timens new roman', 36, 'bold'), fg='orange', bg='white')
        lbl_title.place(x=4, y=4, width=1250, height=50)

        img_logo = Image.open(
            'photos\logo.png')
        img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
        subject.photo_logo = ImageTk.PhotoImage(img_logo)

        subject.logo = Label(subject.root, image=subject.photo_logo)
        subject.logo.place(x=126, y=4, width=50, height=50)

        # frame1
        image_frame = Frame(subject.root, bd=0, relief=None, bg='white')
        image_frame.place(x=0, y=50, width=1250, height=360)

        #icons
        # Home
        img_home = Image.open(
            'photos\Home.png')
        img_home = img_home.resize((125, 125), Image.ANTIALIAS)
        self.photo1_logo = ImageTk.PhotoImage(img_home)

        self.home = Label(image_frame, image=self.photo1_logo)
        self.home.grid(row=0, column=0, padx=25, pady=21, sticky=W)

        btn_Home = Button(image_frame, command=lambda: admin.home.__init__(self, root), text='Home', font=(
            "arial", 15, "bold"), width=10, bg='light green', fg='orange')
        btn_Home.grid(row=1, column=0, padx=10, pady=3)

        # student
        img_student = Image.open(
            'photos\Student-3-icon.png')
        img_student = img_student.resize((125, 125), Image.ANTIALIAS)
        self.photo2_logo = ImageTk.PhotoImage(img_student)

        self.student = Label(image_frame, image=self.photo2_logo)
        self.student.grid(row=0, column=1, padx=25, pady=21, sticky=W)

        btn_student = Button(image_frame, command=lambda: student.student.__init__(self, root), text='Student', font=(
            "arial", 15, "bold"), width=10, bg='light green', fg='orange')
        btn_student.grid(row=1, column=1, padx=10, pady=3)

       # Instructor
        img_instructor = Image.open(
            'photos\instructor.png')
        img_instructor = img_instructor.resize((125, 125), Image.ANTIALIAS)
        self.photo5_logo = ImageTk.PhotoImage(img_instructor)

        self.instructor = Label(image_frame, image=self.photo5_logo)
        self.instructor.grid(row=0, column=2, padx=25, pady=21, sticky=W)

        btn_instructor = Button(image_frame, command=lambda: instructor.instructor.__init__(self, root),  text='Instructor', font=(
            "arial", 15, "bold"), width=10, bg='light green', fg='orange')
        btn_instructor.grid(row=1, column=2, padx=10, pady=3)

        # Exam
        img_exam = Image.open(
            'photos\Exam.png')
        img_exam = img_exam.resize((125, 125), Image.ANTIALIAS)
        self.photo4_logo = ImageTk.PhotoImage(img_exam)

        self.exam = Label(image_frame, image=self.photo4_logo)
        self.exam.grid(row=0, column=3, padx=25, pady=21, sticky=W)

        btn_exam = Button(image_frame, command=lambda: exam.exam.__init__(self, root), text='Exam', font=(
            "arial", 15, "bold"), width=10, bg='light green', fg='orange')
        btn_exam.grid(row=1, column=3, padx=10, pady=3)

        #icons-end

        # Mainframe
        Main_frame = Frame(subject.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=0, y=300, width=1250, height=530)

        # upper frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='SUBJECT_DETAILS', font=(
            'timens new roman', 12, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1250, height=265)
        #labels and fields

        # variables
        subject.var_id = StringVar()
        subject.var_subname = StringVar()
        subject.var_credit = StringVar()
        subject.var_Instructor = StringVar()
        subject.var_tid = StringVar()

        # Id
        lbl_id = Label(upper_frame, text="Subject_Id:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_id.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        txt_id = ttk.Entry(upper_frame, textvariable=subject.var_id, font=(
            'arial', 13, 'bold'))
        txt_id.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        # Name
        lbl_naame = Label(upper_frame, text="Name:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_naame.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        txt_naame = ttk.Entry(upper_frame, textvariable=subject.var_subname, font=(
            'arial', 13, 'bold'))
        txt_naame.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # Credits
        lbl_cred = Label(upper_frame, text="Credits:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_cred.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        txt_cred = ttk.Entry(upper_frame, textvariable=subject.var_credit, font=(
            'arial', 13, 'bold'))
        txt_cred.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        # Instructor
        lbl_Instructor = Label(upper_frame, text="Instructor_name:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_Instructor.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        txt_Instructor = ttk.Entry(upper_frame, textvariable=subject.var_Instructor, font=(
            'arial', 13, 'bold'))
        txt_Instructor.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        # InstructorID
        lbl_tid = Label(upper_frame, text="Instructor_ID:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_tid.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        txt_tid = ttk.Entry(upper_frame, textvariable=subject.var_tid, font=(
            'arial', 13, 'bold'))
        txt_tid.grid(row=3, column=4, padx=2, pady=7, sticky=W)

        # Button frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=950, y=15, width=170, height=190)

        btn_add = Button(button_frame, command=subject.add_data, text='Save', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_add.grid(row=0, column=0, padx=1, pady=3)

        btn_update = Button(button_frame, command=subject.update_data, text='Update', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_update.grid(row=1, column=0, padx=1, pady=3)

        btn_delete = Button(button_frame, command=subject.delete_data, text='Delete', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_delete.grid(row=2, column=0, padx=1, pady=3)

        btn_reset = Button(button_frame, command=subject.reset_data, text='Clear', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_reset.grid(row=3, column=0, padx=1, pady=3)

        # down frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='DATA', font=(
            'timens new roman', 12, 'bold'), fg='red')
        down_frame.place(x=10, y=275, width=1250, height=265)

        # search frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white', text='Search', font=(
            'timens new roman', 12, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1250, height=60)

        search_by = Label(search_frame, text='Subject ID:', font=(
            'arial', 12, 'bold'), bg='white')
        search_by.grid(row=0, column=0, padx=5, sticky=W)

        # saech

        subject.var_search = StringVar()

        txt_search = ttk.Entry(search_frame, textvariable=subject.var_search, width=22,
                               font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=1, padx=5)

        but_search = Button(search_frame, command=subject.search_data, width=14, text='Search', font=(
            "arial", 11, "bold"), bg='light green', fg='orange')
        but_search.grid(row=0, column=2, padx=5)

        but_showall = Button(search_frame, command=subject.fetch, width=14, text='Show all', font=(
            "arial", 11, "bold"), bg='light green', fg='orange')
        but_showall.grid(row=0, column=4, padx=5)

        # subject table view
        # tableframe
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=65, width=1250, height=170)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        subject.subject_table = ttk.Treeview(table_frame, columns=(
            "1", "2", "3", "4", "5"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=subject.subject_table.xview)
        scroll_y.config(command=subject.subject_table.yview)

        subject.subject_table.heading('1', text='Subject_ID')
        subject.subject_table.heading('2', text='Subject_Name')
        subject.subject_table.heading('3', text='Credits')
        subject.subject_table.heading('4', text='Instructor_Name')
        subject.subject_table.heading('5', text='Instructor_ID')

        subject.subject_table['show'] = 'headings'

        subject.subject_table.column('1', width=100)
        subject.subject_table.column('2', width=100)
        subject.subject_table.column('3', width=100)
        subject.subject_table.column('4', width=100)
        subject.subject_table.column('5', width=100)

        subject.subject_table.pack(fill=BOTH, expand=1)
        subject.subject_table.bind("<ButtonRelease>", subject.get_cursor)
        subject.fetch()

    def add_data():
        if subject.var_id == "" or subject.var_subname == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                my_cursor.execute(
                    'INSERT INTO subject VALUES(%s,%s,%s,%s,%s)', (
                        subject.var_id.get(),
                        subject.var_subname.get(),
                        subject.var_credit.get(),
                        subject.var_Instructor.get(),
                        subject.var_tid.get()
                    ))
                cnx.commit()
                subject.fetch()
                cnx.close()
                messagebox.showinfo(
                    'Success', 'subject has been added', parent=subject.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=subject.root)

    def fetch():
        cnx = mysql.connector.connect(
            host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
        my_cursor = cnx.cursor()
        my_cursor.execute('SELECT * FROM subject')
        data = my_cursor.fetchall()
        if len(data) != 0:
            subject.subject_table.delete(*subject.subject_table.get_children())
            for i in data:
                subject.subject_table.insert("", END, values=i)
        cnx.commit()
        cnx.close()

    # get cursor
    def get_cursor(event=""):
        cursor_row = subject.subject_table.focus()
        content = subject.subject_table.item(cursor_row)
        data = content['values']

        subject.var_id.set(data[0]),
        subject.var_subname.set(data[1]),
        subject.var_credit.set(data[2]),
        subject.var_Instructor.set(data[3]),
        subject.var_tid.set(data[4]),

    def update_data():
        if subject.var_id.get == "" or subject.var_subname == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure..?')
                if update > 0:
                    cnx = mysql.connector.connect(
                        host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                    my_cursor = cnx.cursor()

                    my_cursor.execute('UPDATE subject SET Subject_Name=%s,Credits=%s,Instructor_Name=%s,Instructor_ID=%s WHERE Subject_ID=%s', (

                        subject.var_subname.get(),
                        subject.var_credit.get(),
                        subject.var_Instructor.get(),
                        subject.var_tid.get(),

                        subject.var_id.get(),
                    ))
                else:
                    if not update:
                        return
                cnx.commit()
                subject.fetch()
                cnx.close()
                messagebox.showinfo(
                    'success', 'updates successfully', parent=subject.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=subject.root)

    def delete_data():
        if subject.var_id.get() == "":
            messagebox.showerror('ERROR', "All fields are required")
        else:
            try:
                Delete = messagebox.askyesno(
                    'Delete', 'Are you sure..? Wantted to Delete', parent=subject.root)
                if Delete > 0:
                    cnx = mysql.connector.connect(
                        host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                    my_cursor = cnx.cursor()
                    query = 'Delete FROM subject WHERE subject_ID=%s'
                    value = (subject.var_id.get(),)
                    my_cursor.execute(query, value)
                else:
                    if not Delete:
                        return
                cnx.commit()
                subject.fetch()
                cnx.close()
                messagebox.showinfo(
                    'success', 'Deleted successfully', parent=subject.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=subject.root)

    def reset_data():

        subject.var_id.set(""),
        subject.var_subname.set(""),
        subject.var_credit.set(""),
        subject.var_Instructor.set(""),
        subject.var_tid.set(""),

    def search_data():
        if subject.var_search == '':
            messagebox.showerror('ERROR', 'Enter Subject Id')
        else:
            try:
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                query = 'SELECT * FROM subject WHERE Subject_ID=%s'
                value = (subject.var_search.get(),)
                my_cursor.execute(query, value)
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    subject.subject_table.delete(
                        *subject.subject_table.get_children())
                    for i in rows:
                        subject.subject_table.insert("", END, values=i)
                cnx.commit()
                cnx.close()
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=subject.root)


if __name__ == "__main__":
    root = Tk()
    obj = subject(root)
    root.mainloop()
