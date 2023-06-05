from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)
import subject
import exam
import admin 
import instructor


class student:

    def __init__(self, root):

        student.root = root
        student.root.geometry("1250x700+0+0")
        student.root.title('student')

        lbl_title = Label(student.root, text='ONLINE EXAM MANAGEMENT SYSTEM', font=(
            'timens new roman', 36, 'bold'), fg='orange', bg='light green')
        lbl_title.place(x=4, y=4, width=1250, height=50)

        img_logo = Image.open(
            'photos\logo.png')
        img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
        student.photo_logo = ImageTk.PhotoImage(img_logo)

        student.logo = Label(student.root, image=student.photo_logo)
        student.logo.place(x=126, y=4, width=50, height=50)
        # frame1
        image_frame = Frame(student.root, bd=0, relief=None, bg='white')
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

        # Instructor
        img_instructor = Image.open(
            'photos\instructor.png')
        img_instructor = img_instructor.resize((125, 125), Image.ANTIALIAS)
        self.photo5_logo = ImageTk.PhotoImage(img_instructor)

        self.instructor = Label(image_frame, image=self.photo5_logo)
        self.instructor.grid(row=0, column=1, padx=25, pady=21, sticky=W)

        btn_instructor = Button(image_frame,command=lambda: instructor.instructor.__init__(self, root),  text='Instructor', font=(
            "arial", 15, "bold"), width=10, bg='light green', fg='orange')
        btn_instructor.grid(row=1, column=1, padx=10, pady=3)

        # subject
        img_subject = Image.open(
            'photos\subject.png')
        img_subject = img_subject.resize((125, 125), Image.ANTIALIAS)
        self.photo3_logo = ImageTk.PhotoImage(img_subject)

        self.subject = Label(image_frame, image=self.photo3_logo)
        self.subject.grid(row=0, column=2, padx=25, pady=21, sticky=W)

        btn_subject = Button(image_frame, command=lambda: subject.subject.__init__(self, root), text='Subject', font=(
            "arial", 15, "bold"), width=10, bg='light green', fg='orange')
        btn_subject.grid(row=1, column=2, padx=10, pady=3)

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
        Main_frame = Frame(student.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=0, y=300, width=1250, height=530)

        # upper frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='STUDENT_ DETAILS', font=(
            'timens new roman', 12, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1250, height=265)
        #labels and fields

        # variables
        student.var_dep = StringVar()
        student.var_name = StringVar()
        student.var_phone = StringVar()
        student.var_reg = StringVar()
        student.var_mail = StringVar()
        student.var_outmail = StringVar()
        student.var_pass = StringVar()
        # department
        lbl_dep = Label(upper_frame, text='Department', font=(
            'arial', 12, 'bold'), bg='white')
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

        combo_dep = ttk.Combobox(upper_frame, textvariable=student.var_dep, font=(
            'arial', 13, 'bold'), width=16, state='readonly')
        combo_dep['value'] = ('select department', 'CSE',
                              'CYS', 'CCE', 'ECE', 'ARE', 'AIE', 'MEE')
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Name
        lbl_name = Label(upper_frame, text="Name:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_name.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        txt_name = ttk.Entry(upper_frame, textvariable=student.var_name, font=(
            'arial', 13, 'bold'))
        txt_name.grid(row=0, column=3, padx=2, pady=7, sticky=W)

        # Registernumber
        lbl_reg = Label(upper_frame, text="Register Number:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_reg.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        txt_reg = ttk.Entry(upper_frame, textvariable=student.var_reg, font=(
            'arial', 13, 'bold'))
        txt_reg.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # Email
        lbl_mail = Label(upper_frame, text="E-Mail:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_mail.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        txt_mail = ttk.Entry(upper_frame, textvariable=student.var_mail, font=(
            'arial', 13, 'bold'))
        txt_mail.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        # contact number
        lbl_num = Label(upper_frame, text="Phone:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_num.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        txt_num = ttk.Entry(upper_frame, textvariable=student.var_phone, font=(
            'arial', 13, 'bold'))
        txt_num.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        

        # College mail
        lbl_mail2 = Label(upper_frame, text="Outlook-Mail:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_mail2.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        txt_mail2 = ttk.Entry(upper_frame, textvariable=student.var_outmail, font=(
            'arial', 13, 'bold'))
        txt_mail2.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        # password
        lbl_pass = Label(upper_frame, text="password:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_pass.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        txt_pass = ttk.Entry(upper_frame, textvariable=student.var_pass, font=(
            'arial', 13, 'bold'))
        txt_pass.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        # Button frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=950, y=15, width=170, height=190)

        btn_add = Button(button_frame, command=student.add_data, text='Save', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_add.grid(row=0, column=0, padx=1, pady=3)

        btn_update = Button(button_frame, command=student.update_data, text='Update', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_update.grid(row=1, column=0, padx=1, pady=3)

        btn_delete = Button(button_frame, command=student.delete_data, text='Delete', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_delete.grid(row=2, column=0, padx=1, pady=3)

        btn_reset = Button(button_frame, command=student.reset_data, text='Clear', font=(
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

        search_by = Label(search_frame, text='Register Number:', font=(
            'arial', 12, 'bold'), bg='white')
        search_by.grid(row=0, column=0, padx=5, sticky=W)

        # saech

        student.var_search = StringVar()

        txt_search = ttk.Entry(search_frame, textvariable=student.var_search, width=22,
                               font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=1, padx=5)

        but_search = Button(search_frame, command=student.search_data, width=14, text='Search', font=(
            "arial", 11, "bold"), bg='light green', fg='orange')
        but_search.grid(row=0, column=2, padx=5)

        but_showall = Button(search_frame, command=student.fetch, width=14, text='Show all', font=(
            "arial", 11, "bold"), bg='light green', fg='orange')
        but_showall.grid(row=0, column=4, padx=5)

        # student table view
        # tableframe
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=65, width=1250, height=170)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        student.student_table = ttk.Treeview(table_frame, columns=(
            "1", "2", "3", "4", "5", "6", "7", "8"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=student.student_table.xview)
        scroll_y.config(command=student.student_table.yview)

        student.student_table.heading('1', text='Department')
        student.student_table.heading('2', text='Name')
        student.student_table.heading('3', text='Register Number')
        student.student_table.heading('4', text='Email')
        student.student_table.heading('5', text='Phone')
        student.student_table.heading('6', text='Outlook_Mail')
        student.student_table.heading('7', text='Password')

        student.student_table['show'] = 'headings'

        student.student_table.column('1', width=60)
        student.student_table.column('2', width=100)
        student.student_table.column('3', width=100)
        student.student_table.column('4', width=180)
        student.student_table.column('5', width=80)
        student.student_table.column('6', width=180)
        student.student_table.column('7', width=100)

        student.student_table.pack(fill=BOTH, expand=1)
        student.student_table.bind("<ButtonRelease>", student.get_cursor)
        student.fetch()
        root.mainloop()

    def add_data():
        if student.var_dep.get == "" or student.var_mail == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                my_cursor.execute(
                    'INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s)', (
                        student.var_dep.get(),
                        student.var_name.get(),
                        student.var_reg.get(),
                        student.var_mail.get(),
                        student.var_phone.get(),
                        student.var_outmail.get(),
                        student.var_pass.get()))
                cnx.commit()
                student.fetch()
                cnx.close()
                messagebox.showinfo(
                    'Success', 'Student has been added', parent=student.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=student.root)

    def fetch():
        cnx = mysql.connector.connect(
            host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
        my_cursor = cnx.cursor()
        my_cursor.execute('SELECT * FROM student')
        data = my_cursor.fetchall()
        if len(data) != 0:
            student.student_table.delete(*student.student_table.get_children())
            for i in data:
                student.student_table.insert("", END, values=i)
        cnx.commit()
        cnx.close()

    # get cursor

    def get_cursor(event=""):
        cursor_row = student.student_table.focus()
        content = student.student_table.item(cursor_row)
        data = content['values']

        student.var_dep.set(data[0]),
        student.var_name.set(data[1]),
        student.var_reg.set(data[2]),
        student.var_mail.set(data[3]),
        student.var_phone.set(data[4]),
        student.var_outmail.set(data[5]),
        student.var_pass.set(data[6])

    def update_data():
        if student.var_dep.get == "" or student.var_mail == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure..?')
                if update > 0:
                    cnx = mysql.connector.connect(
                        host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                    my_cursor = cnx.cursor()

                    my_cursor.execute('UPDATE student SET Department=%s,Name=%s,Personal_Mail=%s,Phone=%s,Outlook_Mail=%s,User_ID=%s,Password=%s WHERE Register_Number=%s', (

                        student.var_dep.get(),
                        student.var_name.get(),
                        student.var_mail.get(),
                        student.var_phone.get(),
                        student.var_outmail.get(),
                        student.var_pass.get(),
                        student.var_reg.get(),
                    ))
                else:
                    if not update:
                        return
                cnx.commit()
                student.fetch()
                cnx.close()
                messagebox.showinfo(
                    'success', 'updates successfully', parent=student.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=student.root)

    def delete_data():
        if student.var_reg.get() == "":
            messagebox.showerror('ERROR', "All fields are required")
        else:
            try:
                Delete = messagebox.askyesno(
                    'Delete', 'Are you sure..? Wantted to Delete', parent=student.root)
                if Delete > 0:
                    cnx = mysql.connector.connect(
                        host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                    my_cursor = cnx.cursor()
                    query = 'Delete FROM student WHERE Register_Number=%s'
                    value = (student.var_reg.get(),)
                    my_cursor.execute(query, value)
                else:
                    if not Delete:
                        return
                cnx.commit()
                student.fetch()
                cnx.close()
                messagebox.showinfo(
                    'success', 'Deleted successfully', parent=student.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=student.root)

    def reset_data():
        student.var_dep.set("select department"),
        student.var_name.set(""),
        student.var_reg.set(""),
        student.var_mail.set(""),
        student.var_phone.set(""),
        student.var_outmail.set(""),
        student.var_pass.set("")

    def search_data():
        if student.var_search == '':
            messagebox.showerror('ERROR', 'Enter Registeer Number')
        else:
            try:
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                query = 'SELECT * FROM student WHERE Register_Number=%s'
                value = (student.var_search.get(),)
                my_cursor.execute(query, value)
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    student.student_table.delete(
                        *student.student_table.get_children())
                    for i in rows:
                        student.student_table.insert("", END, values=i)
                cnx.commit()
                cnx.close()
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=student.root)


if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
