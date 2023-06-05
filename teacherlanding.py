from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)
import exam1



class teacher:

    def __init__(self, root):

        teacher.root = root
        teacher.root.geometry("1250x700+0+0")
        teacher.root.title('Teacher Landing')

        lbl_title = Label(teacher.root, text='ONLINE EXAM MANAGEMENT SYSTEM', font=(
            'timens new roman', 36, 'bold'), fg='orange', bg='light green')
        lbl_title.place(x=4, y=4, width=1250, height=50)

        img_logo = Image.open(
            'photos\logo.png')
        img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
        teacher.photo_logo = ImageTk.PhotoImage(img_logo)

        teacher.logo = Label(teacher.root, image=teacher.photo_logo)
        teacher.logo.place(x=126, y=4, width=50, height=50)
        # frame1
        image_frame = Frame(teacher.root, bd=0, relief=None, bg='white')
        image_frame.place(x=0, y=50, width=1250, height=360)

        # Exam
        img_exam = Image.open(
            'photos\Exam.png')
        img_exam = img_exam.resize((125, 125), Image.ANTIALIAS)
        self.photo4_logo = ImageTk.PhotoImage(img_exam)

        self.exam = Label(image_frame, image=self.photo4_logo)
        self.exam.grid(row=0, column=3, padx=25, pady=21, sticky=W)

        btn_exam = Button(image_frame, command=lambda: exam1.exam.__init__(self, root), text='Exam', font=(
            "arial", 15, "bold"), width=10, bg='light green', fg='orange')
        btn_exam.grid(row=1, column=3, padx=10, pady=3)

        






        
        
         # Mainframe
        Main_frame = Frame(teacher.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=0, y=300, width=1250, height=530)

        # upper frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Marks pulbhishing', font=(
            'timens new roman', 12, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1250, height=265)

        # down frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Marks_Data', font=(
            'timens new roman', 12, 'bold'), fg='red')
        down_frame.place(x=10, y=275, width=1250, height=265)

        # search frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white', text='Search', font=(
            'timens new roman', 12, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1250, height=60)

        search_by = Label(search_frame, text='Registration Number:', font=(
            'arial', 12, 'bold'), bg='white')
        search_by.grid(row=0, column=0, padx=5, sticky=W)

        teacher.var_search = StringVar()

        txt_search = ttk.Entry(search_frame, textvariable=teacher.var_search, width=22,
                               font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=1, padx=5)

        but_search = Button(search_frame, command=teacher.search_data, width=14, text='Search', font=(
            "arial", 11, "bold"), bg='light green', fg='orange')
        but_search.grid(row=0, column=2, padx=5)

        but_showall = Button(search_frame, command=teacher.fetch, width=14, text='Show all', font=(
            "arial", 11, "bold"), bg='light green', fg='orange')
        but_showall.grid(row=0, column=4, padx=5)


        teacher.var_id = StringVar()
        teacher.var_sid = StringVar()
        teacher.var_rgid = StringVar()
        teacher.exaname = StringVar()
        teacher.var_marks = StringVar()


        # Id
        lbl_id = Label(upper_frame, text="Exam_Id:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_id.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        txt_id = ttk.Entry(upper_frame, textvariable=teacher.var_id, font=(
            'arial', 13, 'bold'))
        txt_id.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        # sub Id
        lbl_sid = Label(upper_frame, text="teacher_Id:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_sid.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        txt_sid = ttk.Entry(upper_frame, textvariable=teacher.var_sid, font=(
            'arial', 13, 'bold'))
        txt_sid.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # Registration 
        lbl_rgid = Label(upper_frame, text="Registration NUmber:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_rgid.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        txt_rgid = ttk.Entry(upper_frame, textvariable=teacher.var_rgid, font=(
            'arial', 13, 'bold'))
        txt_rgid.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        # Exname
        lbl_exname = Label(upper_frame, text="Exam Name:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_exname.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        txt_exname = ttk.Entry(upper_frame, textvariable=teacher.exaname, font=(
            'arial', 13, 'bold'))
        txt_exname.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        # marks
        lbl_marks = Label(upper_frame, text="Marks:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_marks.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        txt_marks = ttk.Entry(upper_frame, textvariable=teacher.var_marks, font=(
            'arial', 13, 'bold'))
        txt_marks.grid(row=4, column=1, padx=2, pady=7, sticky=W)

        # Button frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=950, y=15, width=170, height=190)

        btn_add = Button(button_frame, command=teacher.add_data, text='Save', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_add.grid(row=0, column=0, padx=1, pady=3)

        btn_update = Button(button_frame, command=teacher.update_data, text='Update', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_update.grid(row=1, column=0, padx=1, pady=3)

        btn_delete = Button(button_frame, command=teacher.delete_data, text='Delete', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_delete.grid(row=2, column=0, padx=1, pady=3)

        btn_reset = Button(button_frame, command=teacher.reset_data, text='Clear', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_reset.grid(row=3, column=0, padx=1, pady=3)


        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=65, width=1250, height=170)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        teacher.marks_table = ttk.Treeview(table_frame, columns=(
            "1", "2", "3", "4", "5"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=teacher.marks_table.xview)
        scroll_y.config(command=teacher.marks_table.yview)

        teacher.marks_table.heading('1', text='Exam_ID')
        teacher.marks_table.heading('2', text='Subject_ID')
        teacher.marks_table.heading('3', text='Registration_Number')
        teacher.marks_table.heading('4', text='Exam_Name')
        teacher.marks_table.heading('5', text='Marks')

        teacher.marks_table['show'] = 'headings'

        teacher.marks_table.column('1', width=100)
        teacher.marks_table.column('2', width=100)
        teacher.marks_table.column('3', width=100)
        teacher.marks_table.column('4', width=100)
        teacher.marks_table.column('5', width=100)

        teacher.marks_table.pack(fill=BOTH, expand=1)
        teacher.marks_table.bind("<ButtonRelease>", teacher.get_cursor)
        teacher.fetch()




    def add_data():
        if teacher.var_id == "" or teacher.var_sid == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                my_cursor.execute(
                    'INSERT INTO marks VALUES(%s,%s,%s,%s,%s)', (
                        teacher.var_id.get(),
                        teacher.var_sid.get(),
                        teacher.var_rgid.get(),
                        teacher.exaname.get(),
                        teacher.var_marks.get()
                    ))
                cnx.commit()
                teacher.fetch()
                cnx.close()
                messagebox.showinfo(
                    'Success', 'marks has been added', parent=teacher.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=teacher.root)

    def fetch():
        cnx = mysql.connector.connect(
            host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
        my_cursor = cnx.cursor()
        my_cursor.execute('SELECT * FROM marks WHERE Subject_ID=(SELECT Subject_ID FROM instructor WHERE Instructor_ID=1001)')
        data = my_cursor.fetchall()
        if len(data) != 0:
            teacher.marks_table.delete(*teacher.marks_table.get_children())
            for i in data:
                teacher.marks_table.insert("", END, values=i)
        cnx.commit()
        cnx.close()

    # get cursor
    def get_cursor(event=""):
        cursor_row = teacher.marks_table.focus()
        content = teacher.marks_table.item(cursor_row)
        data = content['values']

        teacher.var_id.set(data[0]),
        teacher.var_sid.set(data[1]),
        teacher.var_rgid.set(data[2]),
        teacher.exaname.set(data[3]),
        teacher.var_marks.set(data[4]),

    def update_data():
        if teacher.var_id.get == "" or teacher.var_sid == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure..?')
                if update > 0:
                    cnx = mysql.connector.connect(
                        host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                    my_cursor = cnx.cursor()

                    my_cursor.execute('UPDATE marks SET Exam_ID=%s,Subject_ID=%s,Exam_Name=%s,Marks=%s WHERE Registration_Number=%s', (

                        teacher.var_id.get(),
                        teacher.var_sid.get(),
                        teacher.exaname.get(),
                        teacher.var_marks.get(),

                        teacher.var_rgid.get(),
                    ))
                else:
                    if not update:
                        return
                cnx.commit()
                teacher.fetch()
                cnx.close()
                messagebox.showinfo(
                    'success', 'updates successfully', parent=teacher.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=teacher.root)

    def delete_data():
        if teacher.var_id.get() == "":
            messagebox.showerror('ERROR', "All fields are required")
        else:
            try:
                Delete = messagebox.askyesno(
                    'Delete', 'Are you sure..? Wantted to Delete', parent=teacher.root)
                if Delete > 0:
                    cnx = mysql.connector.connect(
                        host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                    my_cursor = cnx.cursor()
                    query = 'DELETE FROM marks WHERE Registration_Number=%s and Exam_ID=%s'
                    value = (teacher.var_rgid.get(),teacher.var_id.get())
                    my_cursor.execute(query, value)
                else:
                    if not Delete:
                        return
                cnx.commit()
                teacher.fetch()
                cnx.close()
                messagebox.showinfo(
                    'success', 'Deleted successfully', parent=teacher.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=teacher.root)

    def reset_data():

        teacher.var_id.set(""),
        teacher.var_sid.set(""),
        teacher.var_rgid.set(""),
        teacher.exaname.set(""),
        teacher.var_marks.set(""),



    def search_data():
        if teacher.var_search == '':
            messagebox.showerror('ERROR', 'Enter Registration_Number')
        else:
            try:
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                query = 'SELECT * FROM marks WHERE Registration_Number=%s'
                value = (teacher.var_search.get(),)
                my_cursor.execute(query, value)
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    teacher.marks_table.delete(
                        *teacher.marks_table.get_children())
                    for i in rows:
                        teacher.marks_table.insert("", END, values=i)
                cnx.commit()
                cnx.close()
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=teacher.root)














    

if __name__ == "__main__":
    root = Tk()
    obj = teacher(root)
    root.mainloop()
