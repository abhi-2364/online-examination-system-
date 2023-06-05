# login form
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from twilio.rest import Client
import admin
import teacherlanding
import studentlanding
import forgot


class loginForm:
    def __init__(self, root):

        loginForm.root = root
        loginForm.root.geometry("1250x700+0+0")
        loginForm.root.title('Online Exam Management System')

        lbl_title = Label(loginForm.root, text='ONLINE EXAM MANAGEMENT SYSTEM', font=(
            'timens new roman', 36, 'bold'), fg='orange', bg='light green')
        lbl_title.place(x=4, y=4, width=1250, height=50)

        img_logo = Image.open(
            'photos\logo.png')
        img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
        loginForm.photo_logo = ImageTk.PhotoImage(img_logo)

        loginForm.logo = Label(loginForm.root, image=loginForm.photo_logo)
        loginForm.logo.place(x=126, y=4, width=50, height=50)
        # frame1
        image_frame = Frame(loginForm.root, bd=0, relief=None, bg='light grey')
        image_frame.place(x=0, y=50, width=1250, height=220)

        # Mainframe
        Main_frame = Frame(loginForm.root, bd=2, relief=RIDGE, bg='light grey')
        Main_frame.place(x=0, y=230, width=1250, height=530)

        # upper frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='light grey', font=(
            'timens new roman', 12, 'bold'), fg='red')
        upper_frame.place(x=300, y=50, width=450, height=300)

        # variables
        loginForm.var_rgid = StringVar()
        loginForm.var_pass = StringVar()
        loginForm.userInput = StringVar()
        loginForm.a = StringVar()

        lbl_head = Label(upper_frame, text="Sign in", font=(
            'arial', 24, ), bg='light grey', fg='orange')
        lbl_head.grid(row=0, column=1, padx=4, pady=7, sticky=W)

        lbl_uname = Label(upper_frame, text="User_ID:", font=(
            'arial', 14, 'bold'), bg='light grey')
        lbl_uname.grid(row=2, column=0, padx=4, pady=7, sticky=W)

        txt_uname = ttk.Entry(upper_frame, textvariable=loginForm.var_rgid, font=(
            'arial', 13, 'bold'))
        txt_uname.grid(row=2, column=1, padx=4, pady=7, sticky=W)

        lbl_pass = Label(upper_frame, text="Password:", font=(
            'arial', 14, 'bold'), bg='light grey')
        lbl_pass.grid(row=3, column=0, padx=4, pady=9, sticky=W)

        txt_pass = ttk.Entry(upper_frame, show="*", textvariable=loginForm.var_pass, font=(
            'arial', 13, 'bold'))
        txt_pass.grid(row=3, column=1, padx=4, pady=9, sticky=W)

        btn_log = Button(upper_frame, command=self.login_func, text='login', font=(
            "arial", 15, "bold"), width=13, bg='orange', fg='light grey')
        btn_log.grid(row=5, column=1, padx=1, pady=3)

        btn_forgot = Button(upper_frame, text='forgot password..?', activebackground='light grey', command=lambda: forgot.forgot.__init__(self, root), borderwidth=0, font=(
            "arial", 15, "bold"), width=13, bg='light grey', fg='blue')
        btn_forgot.place(x=20, y=220, width=185, height=35)

    # create a function to login

    def login_func(self):
        if loginForm.var_rgid.get() == "" or loginForm.var_pass.get() == "":
            messagebox.showerror('Error', "All fields are required")

        elif loginForm.var_rgid.get() == "admin001" and loginForm.var_pass.get() == "amrita@123":
            loginForm.new_window = Toplevel(loginForm.root)

            loginForm.app = admin.home(loginForm.new_window)

        else:

            if (loginForm.var_rgid.get()[0] != 'C'):
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                my_cursor.execute("SELECT * from instructor WHERE Instructor_ID=%s and password=%s", (
                    loginForm.var_rgid.get(),
                    loginForm.var_pass.get(),
                ))
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid username & password")
                else:
                    loginForm.new_window = Toplevel(loginForm.root)

                    loginForm.app = teacherlanding.teacher(
                        loginForm.new_window)
                    cnx.commit()
                    cnx.close()
            else:
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                my_cursor.execute("SELECT * from student WHERE Register_Number=%s and Password=%s", (
                    loginForm.var_rgid.get(),
                    loginForm.var_pass.get(),
                ))
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid username & Password")
                else:
                    cnx.commit()
                    cnx.close()

                    loginForm.new_window = Toplevel(loginForm.root)

                    loginForm.app = studentlanding.studetail(
                        loginForm.new_window)


if __name__ == '__main__':
    win = Tk()
    app = loginForm(win)
    win.mainloop()
