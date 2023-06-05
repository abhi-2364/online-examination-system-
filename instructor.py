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
import subject

class instructor:
    def __init__(self, root):
        instructor.root = root
        instructor.root.geometry("1250x700+0+0")
        instructor.root.title('instructor')

        lbl_title = Label(instructor.root, text='ONLINE EXAM MANAGEMENT SYSTEM', font=(
            'timens new roman', 36, 'bold'), fg='orange', bg='white')
        lbl_title.place(x=4, y=4, width=1250, height=50)

        img_logo = Image.open(
            'photos\logo.png')
        img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
        instructor.photo_logo = ImageTk.PhotoImage(img_logo)

        instructor.logo = Label(instructor.root, image=instructor.photo_logo)
        instructor.logo.place(x=126, y=4, width=50, height=50)

        # frame1
        image_frame = Frame(instructor.root, bd=0, relief=None, bg='white')
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
        Main_frame = Frame(instructor.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=0, y=300, width=1250, height=530)

        # upper frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='instructor_DETAILS', font=(
            'timens new roman', 12, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1250, height=265)
        #labels and fields

        # variables
        instructor.var_id = StringVar()
        instructor.var_name = StringVar()
        instructor.var_mail = StringVar()
        instructor.var_outlook = StringVar()
        instructor.var_Department = StringVar()
        instructor.var_pass = StringVar()
        instructor.var_sid = StringVar()
        instructor.var_phone = StringVar()

        # Id
        lbl_id = Label(upper_frame, text="Instructor_Id:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_id.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        txt_id = ttk.Entry(upper_frame, textvariable=instructor.var_id, font=(
            'arial', 13, 'bold'))
        txt_id.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        # Name
        lbl_naame = Label(upper_frame, text="Name:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_naame.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        txt_naame = ttk.Entry(upper_frame, textvariable=instructor.var_name, font=(
            'arial', 13, 'bold'))
        txt_naame.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # mails
        lbl_cred = Label(upper_frame, text="Mail:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_cred.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        txt_cred = ttk.Entry(upper_frame, textvariable=instructor.var_mail, font=(
            'arial', 13, 'bold'))
        txt_cred.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        # subject_id
        lbl_sid = Label(upper_frame, text="Subject_ID:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_sid.grid(row=4, column=2, padx=2, pady=7, sticky=W)

        txt_sid = ttk.Entry(upper_frame, textvariable=instructor.var_sid, font=(
            'arial', 13, 'bold'))
        txt_sid.grid(row=4, column=3, padx=2, pady=7, sticky=W)

        # phone
        lbl_phone = Label(upper_frame, text="Phone:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_phone.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        txt_phone = ttk.Entry(upper_frame, textvariable=instructor.var_phone, font=(
            'arial', 13, 'bold'))
        txt_phone.grid(row=4, column=1, padx=2, pady=7, sticky=W)

        # outlookmail
        lbl_Instructor = Label(upper_frame, text="outlook mail:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_Instructor.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        txt_Instructor = ttk.Entry(upper_frame, textvariable=instructor.var_outlook, font=(
            'arial', 13, 'bold'))
        txt_Instructor.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        # InstructorID
        lbl_Department = Label(upper_frame, text="Department:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_Department.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        txt_Department = ttk.Entry(upper_frame, textvariable=instructor.var_Department, font=(
            'arial', 13, 'bold'))
        txt_Department.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        # pass
        lbl_pass = Label(upper_frame, text="Password:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_pass.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        txt_pass = ttk.Entry(upper_frame, textvariable=instructor.var_pass, font=(
            'arial', 13, 'bold'))
        txt_pass.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        # Button frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=950, y=15, width=170, height=190)

        btn_add = Button(button_frame, command=instructor.add_data, text='Save', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_add.grid(row=0, column=0, padx=1, pady=3)

        btn_update = Button(button_frame, command=instructor.update_data, text='Update', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_update.grid(row=1, column=0, padx=1, pady=3)

        btn_delete = Button(button_frame, command=instructor.delete_data, text='Delete', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_delete.grid(row=2, column=0, padx=1, pady=3)

        btn_reset = Button(button_frame, command=instructor.reset_data, text='Clear', font=(
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

        search_by = Label(search_frame, text='instructor ID:', font=(
            'arial', 12, 'bold'), bg='white')
        search_by.grid(row=0, column=0, padx=5, sticky=W)

        # saech

        instructor.var_search = StringVar()

        txt_search = ttk.Entry(search_frame, textvariable=instructor.var_search, width=22,
                               font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=1, padx=5)

        but_search = Button(search_frame, command=instructor.search_data, width=14, text='Search', font=(
            "arial", 11, "bold"), bg='light green', fg='orange')
        but_search.grid(row=0, column=2, padx=5)

        but_showall = Button(search_frame, command=instructor.fetch, width=14, text='Show all', font=(
            "arial", 11, "bold"), bg='light green', fg='orange')
        but_showall.grid(row=0, column=4, padx=5)

        # instructor table view
        # tableframe
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=65, width=1250, height=170)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        instructor.instructor_table = ttk.Treeview(table_frame, columns=(
            "1", "2", "3", "4", "5","6","7","8"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=instructor.instructor_table.xview)
        scroll_y.config(command=instructor.instructor_table.yview)

        instructor.instructor_table.heading('1', text='Instructor_ID')
        instructor.instructor_table.heading('2', text='Instructor_Name')
        instructor.instructor_table.heading('3', text='Email')
        instructor.instructor_table.heading('4', text='outlook_mail')
        instructor.instructor_table.heading('5', text='Department')
        instructor.instructor_table.heading('6', text='Phone')
        instructor.instructor_table.heading('7', text='Subject_ID')
        instructor.instructor_table.heading('8', text='password')

        instructor.instructor_table['show'] = 'headings'

        instructor.instructor_table.column('1', width=100)
        instructor.instructor_table.column('2', width=100)
        instructor.instructor_table.column('3', width=160)
        instructor.instructor_table.column('4', width=160)
        instructor.instructor_table.column('5', width=100)
        instructor.instructor_table.column('6', width=100)
        instructor.instructor_table.column('7', width=100)
        instructor.instructor_table.column('8', width=100)

        instructor.instructor_table.pack(fill=BOTH, expand=1)
        instructor.instructor_table.bind("<ButtonRelease>", instructor.get_cursor)
        instructor.fetch()

    def add_data():
        if instructor.var_id == "" or instructor.var_name == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                my_cursor.execute(
                    'INSERT INTO instructor VALUES(%s,%s,%s,%s,%s,%s,%s,%s)', (
                        instructor.var_id.get(),
                        instructor.var_name.get(),
                        instructor.var_mail.get(),
                        instructor.var_outlook.get(),
                        instructor.var_Department.get(),
                        instructor.var_phone.get(),
                        instructor.var_sid.get(),
                        instructor.var_pass.get()
                    ))
                cnx.commit()
                instructor.fetch()
                cnx.close()
                messagebox.showinfo(
                    'Success', 'instructor has been added', parent=instructor.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=instructor.root)

    def fetch():
        cnx = mysql.connector.connect(
            host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
        my_cursor = cnx.cursor()
        my_cursor.execute('SELECT * FROM instructor')
        data = my_cursor.fetchall()
        if len(data) != 0:
            instructor.instructor_table.delete(*instructor.instructor_table.get_children())
            for i in data:
                instructor.instructor_table.insert("", END, values=i)
        cnx.commit()
        cnx.close()

    # get cursor
    def get_cursor(event=""):
        cursor_row = instructor.instructor_table.focus()
        content = instructor.instructor_table.item(cursor_row)
        data = content['values']

        instructor.var_id.set(data[0]),
        instructor.var_name.set(data[1]),
        instructor.var_mail.set(data[2]),
        instructor.var_outlook.set(data[3]),
        instructor.var_Department.set(data[4]),
        instructor.var_phone.set(data[5]),
        instructor.var_sid.set(data[6]),
        instructor.var_pass.set(data[7]),

    def update_data():
        if instructor.var_id.get == "" or instructor.var_name == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure..?')
                if update > 0:
                    cnx = mysql.connector.connect(
                        host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                    my_cursor = cnx.cursor()

                    my_cursor.execute('UPDATE instructor SET Instructor_Name=%s,Email=%s,outlook_mail=%s,Department=%s,Phone=%s,Subject_ID=%s,password=%s WHERE Instructor_ID=%s', (

                        instructor.var_name.get(),
                        instructor.var_mail.get(),
                        instructor.var_outlook.get(),
                        instructor.var_Department.get(),
                        instructor.var_phone.get(),
                        instructor.var_sid.get(),
                        instructor.var_pass.get(),

                        instructor.var_id.get(),
                    ))
                else:
                    if not update:
                        return
                cnx.commit()
                instructor.fetch()
                cnx.close()
                messagebox.showinfo(
                    'success', 'updates successfully', parent=instructor.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=instructor.root)

    def delete_data():
        if instructor.var_id.get() == "":
            messagebox.showerror('ERROR', "All fields are required")
        else:
            try:
                Delete = messagebox.askyesno(
                    'Delete', 'Are you sure..? Wantted to Delete', parent=instructor.root)
                if Delete > 0:
                    cnx = mysql.connector.connect(
                        host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                    my_cursor = cnx.cursor()
                    query = 'Delete FROM instructor WHERE instructor_ID=%s'
                    value = (instructor.var_id.get(),)
                    my_cursor.execute(query, value)
                else:
                    if not Delete:
                        return
                cnx.commit()
                instructor.fetch()
                cnx.close()
                messagebox.showinfo(
                    'success', 'Deleted successfully', parent=instructor.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=instructor.root)

    def reset_data():

        instructor.var_id.set(""),
        instructor.var_name.set(""),
        instructor.var_mail.set(""),
        instructor.var_outlook.set(""),
        instructor.var_Department.set(""),
        instructor.var_phone.set(""),
        instructor.var_sid.set(""),
        instructor.var_pass.set(""),

    def search_data():
        if instructor.var_search == '':
            messagebox.showerror('ERROR', 'Enter instructor Id')
        else:
            try:
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                query = 'SELECT * FROM instructor WHERE instructor_ID=%s'
                value = (instructor.var_search.get(),)
                my_cursor.execute(query, value)
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    instructor.instructor_table.delete(
                        *instructor.instructor_table.get_children())
                    for i in rows:
                        instructor.instructor_table.insert("", END, values=i)
                cnx.commit()
                cnx.close()
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=instructor.root)


if __name__ == "__main__":
    root = Tk()
    obj = instructor(root)
    root.mainloop()
