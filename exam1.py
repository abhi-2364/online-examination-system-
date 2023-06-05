from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)
import student
import subject
import teacherlanding


class exam:
    def __init__(self, root):
        exam.root = root
        exam.root.geometry("1250x700+0+0")
        exam.root.title('Exam')

        lbl_title = Label(exam.root, text='ONLINE EXAM MANAGEMENT SYSTEM', font=(
            'timens new roman', 36, 'bold'), fg='orange', bg='white')
        lbl_title.place(x=4, y=4, width=1250, height=50)

        img_logo = Image.open(
            'photos\logo.png')
        img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
        exam.photo_logo = ImageTk.PhotoImage(img_logo)

        exam.logo = Label(exam.root, image=exam.photo_logo)
        exam.logo.place(x=126, y=4, width=50, height=50)
        # frame1
        image_frame = Frame(exam.root, bd=0, relief=None, bg='white')
        image_frame.place(x=0, y=50, width=1250, height=360)

        #icons
        # Home
        img_home = Image.open(
            'photos/back.png')
        img_home = img_home.resize((125, 125), Image.ANTIALIAS)
        self.photo1_logo = ImageTk.PhotoImage(img_home)

        self.home = Label(image_frame, image=self.photo1_logo)
        self.home.grid(row=0, column=0, padx=25, pady=21, sticky=W)

        btn_Home = Button(image_frame, command=lambda: teacherlanding.teacher.__init__(self, root), text='BACK', font=(
            "arial", 15, "bold"), width=10, bg='light green', fg='orange')
        btn_Home.grid(row=1, column=0, padx=10, pady=3)

        
        #icons-end

        # Mainframe
        Main_frame = Frame(exam.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=0, y=300, width=1250, height=530)

        # upper frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='EXAM_DETAILS', font=(
            'timens new roman', 12, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1250, height=265)
        #labels and fields

        # variables
        exam.var_Eid = StringVar()
        exam.var_Sid = StringVar()
        exam.var_dura = StringVar()
        exam.var_Exlink = StringVar()
        exam.var_date = StringVar()
        exam.var_stime = StringVar()
        exam.var_Iid = StringVar()

        # Id
        lbl_id = Label(upper_frame, text="Exam_Id:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_id.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        txt_id = ttk.Entry(upper_frame, textvariable=exam.var_Eid, font=(
            'arial', 13, 'bold'))
        txt_id.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        # SID
        lbl_sid = Label(upper_frame, text="Subject_Id:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_sid.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        txt_sid = ttk.Entry(upper_frame, textvariable=exam.var_Sid, font=(
            'arial', 13, 'bold'))
        txt_sid.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # IID
        lbl_Iid = Label(upper_frame, text="Instructor_Id:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_Iid.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        txt_Iid = ttk.Entry(upper_frame, textvariable=exam.var_Iid, font=(
            'arial', 13, 'bold'))
        txt_Iid.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        # Link
        lbl_link = Label(upper_frame, text="Exam_Link:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_link.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        txt_link = ttk.Entry(upper_frame, textvariable=exam.var_Exlink, font=(
            'arial', 13, 'bold'))
        txt_link.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        # date
        lbl_date = Label(upper_frame, text="Date:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_date.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        txt_date = ttk.Entry(upper_frame, textvariable=exam.var_date, font=(
            'arial', 13, 'bold'))
        txt_date.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        # duration
        lbl_dur = Label(upper_frame, text="Duration(min):", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_dur.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        txt_dur = ttk.Entry(upper_frame, textvariable=exam.var_dura, font=(
            'arial', 13, 'bold'))
        txt_dur.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        # start time
        lbl_st = Label(upper_frame, text="Start_Time:", font=(
            'arial', 12, 'bold'), bg='white')
        lbl_st.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        txt_st = ttk.Entry(upper_frame, textvariable=exam.var_stime, font=(
            'arial', 13, 'bold'))
        txt_st.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        # Button frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=950, y=15, width=170, height=190)

        btn_add = Button(button_frame, command=exam.add_data, text='Save', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_add.grid(row=0, column=0, padx=1, pady=3)

        btn_update = Button(button_frame, command=exam.update_data, text='Update', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_update.grid(row=1, column=0, padx=1, pady=3)

        btn_delete = Button(button_frame, command=exam.delete_data, text='Delete', font=(
            "arial", 15, "bold"), width=13, bg='light green', fg='orange')
        btn_delete.grid(row=2, column=0, padx=1, pady=3)

        btn_reset = Button(button_frame, command=exam.reset_data, text='Clear', font=(
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

        search_by = Label(search_frame, text='exam ID:', font=(
            'arial', 12, 'bold'), bg='white')
        search_by.grid(row=0, column=0, padx=5, sticky=W)

        # saech

        exam.var_search = StringVar()

        txt_search = ttk.Entry(search_frame, textvariable=exam.var_search, width=22,
                               font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=1, padx=5)

        but_search = Button(search_frame, command=exam.search_data, width=14, text='Search', font=(
            "arial", 11, "bold"), bg='light green', fg='orange')
        but_search.grid(row=0, column=2, padx=5)

        but_showall = Button(search_frame, command=exam.fetch, width=14, text='Show all', font=(
            "arial", 11, "bold"), bg='light green', fg='orange')
        but_showall.grid(row=0, column=4, padx=5)

        # exam table view
        # tableframe
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=65, width=1250, height=170)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        exam.exam_table = ttk.Treeview(table_frame, columns=(
            "1", "2", "3", "4", "5", "6", "7"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=exam.exam_table.xview)
        scroll_y.config(command=exam.exam_table.yview)

        exam.exam_table.heading('1', text='Exam_ID')
        exam.exam_table.heading('2', text='Subject_ID')
        exam.exam_table.heading('3', text='Instructor_ID')
        exam.exam_table.heading('4', text='Exam_Link')
        exam.exam_table.heading('5', text='Duration')
        exam.exam_table.heading('6', text='Start_time')
        exam.exam_table.heading('7', text='Date')

        exam.exam_table['show'] = 'headings'

        exam.exam_table.column('1', width=100)
        exam.exam_table.column('2', width=100)
        exam.exam_table.column('3', width=100)
        exam.exam_table.column('4', width=180)
        exam.exam_table.column('5', width=100)
        exam.exam_table.column('6', width=100)
        exam.exam_table.column('7', width=100)

        exam.exam_table.pack(fill=BOTH, expand=1)
        exam.exam_table.bind("<ButtonRelease>", exam.get_cursor)
        exam.fetch()

    def add_data():
        if exam.var_Sid == "" or exam.var_Sid == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                my_cursor.execute(
                    'INSERT INTO exam VALUES(%s,%s,%s,%s,%s,%s,%s)', (
                        exam.var_Eid.get(),
                        exam.var_Sid.get(),
                        exam.var_Iid.get(),
                        exam.var_Exlink.get(),
                        exam.var_dura.get(),
                        exam.var_stime.get(),
                        exam.var_date.get(),
                    ))
                cnx.commit()
                exam.fetch()
                cnx.close()
                messagebox.showinfo(
                    'Success', 'exam has been added', parent=exam.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=exam.root)

    def fetch():
        cnx = mysql.connector.connect(
            host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
        my_cursor = cnx.cursor()
        my_cursor.execute('SELECT * FROM exam')
        data = my_cursor.fetchall()
        if len(data) != 0:
            exam.exam_table.delete(*exam.exam_table.get_children())
            for i in data:
                exam.exam_table.insert("", END, values=i)
        cnx.commit()
        cnx.close()

    # get cursor
    def get_cursor(event=""):
        cursor_row = exam.exam_table.focus()
        content = exam.exam_table.item(cursor_row)
        data = content['values']

        exam.var_Eid.set(data[0]),
        exam.var_Sid.set(data[1]),
        exam.var_Iid.set(data[2]),
        exam.var_Exlink.set(data[3]),
        exam.var_dura.set(data[4]),
        exam.var_stime.set(data[5]),
        exam.var_date.set(data[6]),

    def update_data():
        if exam.var_Sid.get == "" or exam.var_Eid.get == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure..?')
                if update > 0:
                    cnx = mysql.connector.connect(
                        host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                    my_cursor = cnx.cursor()

                    my_cursor.execute('UPDATE exam SET Subject_ID=%s,Instructor_ID=%s,Exam_Link=%s,Duration=%s,Start_time=%s, Date=%s WHERE Exam_ID=%s', (

                        exam.var_Sid.get(),
                        exam.var_Iid.get(),
                        exam.var_Exlink.get(),
                        exam.var_dura.get(),
                        exam.var_stime.get(),
                        exam.var_date.get(),
                        exam.var_Eid.get()
                    ))
                else:
                    if not update:
                        return
                cnx.commit()
                exam.fetch()
                cnx.close()
                messagebox.showinfo(
                    'success', 'updates successfully', parent=exam.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=exam.root)

    def delete_data():
        if exam.var_Eid.get() == "":
            messagebox.showerror('ERROR', "All fields are required")
        else:
            try:
                Delete = messagebox.askyesno(
                    'Delete', 'Are you sure..? Wantted to Delete', parent=exam.root)
                if Delete > 0:
                    cnx = mysql.connector.connect(
                        host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                    my_cursor = cnx.cursor()
                    query = 'Delete FROM exam WHERE Exam_ID=%s'
                    value = (exam.var_Eid.get(),)
                    my_cursor.execute(query, value)
                else:
                    if not Delete:
                        return
                cnx.commit()
                exam.fetch()
                cnx.close()
                messagebox.showinfo(
                    'success', 'Deleted successfully', parent=exam.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=exam.root)

    def reset_data():

        exam.var_Sid.set(""),
        exam.var_Iid.set("")
        exam.var_Eid.set(""),
        exam.var_Exlink.set(""),
        exam.var_dura.set(""),
        exam.var_date.set(""),
        exam.var_stime.set("")

    def search_data():
        if exam.var_search == '':
            messagebox.showerror('ERROR', 'Enter exam Id')
        else:
            try:
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                query = 'SELECT * FROM exam WHERE Exam_ID=%s'
                value = (exam.var_search.get(),)
                my_cursor.execute(query, value)
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    exam.exam_table.delete(
                        *exam.exam_table.get_children())
                    for i in rows:
                        exam.exam_table.insert("", END, values=i)
                cnx.commit()
                cnx.close()
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=exam.root)


if __name__ == "__main__":
    root = Tk()
    obj = exam(root)
    root.mainloop()
