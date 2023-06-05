# login form
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from twilio.rest import Client
import login
import random











class forgot:

    def __init__(self, root):

        forgot.root = root
        forgot.root.geometry("1250x700+0+0")
        forgot.root.title('Online Exam Management System - Forgot Password')

        lbl_title = Label(forgot.root, text='ONLINE EXAM MANAGEMENT SYSTEM', font=(
            'timens new roman', 36, 'bold'), fg='orange', bg='light green')
        lbl_title.place(x=4, y=4, width=1250, height=50)

        img_logo = Image.open(
            'photos\logo.png')
        img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
        forgot.photo_logo = ImageTk.PhotoImage(img_logo)

        forgot.logo = Label(forgot.root, image=forgot.photo_logo)
        forgot.logo.place(x=126, y=4, width=50, height=50)
        # frame1
        image_frame = Frame(forgot.root, bd=0, relief=None, bg='light grey')
        image_frame.place(x=0, y=50, width=1250, height=220)

        # Mainframe
        Main_frame = Frame(forgot.root, bd=2, relief=RIDGE, bg='light grey')
        Main_frame.place(x=0, y=230, width=1250, height=530)

        # upper frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='light grey', font=(
            'timens new roman', 12, 'bold'), fg='red')
        upper_frame.place(x=300, y=50, width=450, height=300)

        # variables
        forgot.var_rgid = StringVar()
        forgot.var_pass = StringVar()
        forgot.userInput = StringVar()
        forgot.new1 = StringVar()
        forgot.new2 = StringVar()
        forgot.x=StringVar()

        lbl_head = Label(upper_frame, text="Forgot Password", font=(
            'arial', 24, ), bg='light grey', fg='orange')
        lbl_head.grid(row=0, column=1, padx=4, pady=7, sticky=W)

        lbl_uname = Label(upper_frame, text="User_ID:", font=(
            'arial', 14, 'bold'), bg='light grey')
        lbl_uname.grid(row=2, column=0, padx=4, pady=7, sticky=W)

        txt_uname = ttk.Entry(upper_frame, textvariable=forgot.var_rgid, font=(
            'arial', 13, 'bold'))
        txt_uname.grid(row=2, column=1, padx=4, pady=7, sticky=W)

        

        btn_next = Button(upper_frame, text='Next',command=lambda:forgot.functionn(), font=(
            "arial", 15, "bold"), width=13, bg='orange', fg='light grey')
        btn_next.grid(row=6, column=1, padx=1, pady=3)

        btn_bac = Button(upper_frame, text='Back',bd=0,command=lambda:login.loginForm.__init__(self,root), font=(
            "arial", 15, "bold"), width=13, bg='light grey', fg='blue')
        btn_bac.grid(row=8, column=0, padx=1, pady=3)
        
        
    



    def functionn():


        if forgot.var_rgid.get() == "":
            messagebox.showerror(
                "Error", "Please enter the user_id to reset password")
        else:
            if (forgot.var_rgid.get()[0] != 'C'):
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                my_cursor.execute("SELECT Phone from instructor WHERE Instructor_ID=%s", (
                    forgot.var_rgid.get(),
                ))
                row = my_cursor.fetchone()
                y = row[0]
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid username")
                else:
                    cnx.close()
                    forgot.otp(y)
                    forgot.window = Toplevel()
                    forgot.window.title("otp verification")
                    forgot.window.geometry("340x360+400+170")

                    lbl_otp = Label(forgot.window, text="Enter OTP:", font=(
                        'arial', 14, 'bold'), bg='light grey')
                    lbl_otp.grid(row=2, column=0, padx=4, pady=7, sticky=W)

                    txt_otp = ttk.Entry(forgot.window, textvariable=forgot.userInput, font=(
                        'arial', 13, 'bold'))
                    txt_otp.grid(row=2, column=1, padx=4, pady=7, sticky=W)

                    btn_next = Button(forgot.window, text='Next',command=lambda:forgot.checkotp(),font=(
                        "arial", 15, "bold"), width=13, bg='orange', fg='light grey')
                    btn_next.grid(row=4, column=1, padx=1, pady=3)
            else:
                cnx = mysql.connector.connect(
                    host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                my_cursor = cnx.cursor()
                my_cursor.execute("SELECT Phone from student WHERE Register_Number=%s", (
                    forgot.var_rgid.get(),
                    ))
                row = my_cursor.fetchone()
                y = row[0]
                if row == None:
                        messagebox.showerror(
                            "Error", "Invalid username")
                else:
                        cnx.close()
                        forgot.otp(y)
                        forgot.window = Toplevel()
                        forgot.window.title("otp verification")
                        forgot.window.geometry("340x360+400+170")

                        lbl_otp = Label(forgot.window, text="Enter OTP:", font=(
                            'arial', 14, 'bold'), bg='light grey')
                        lbl_otp.grid(row=2, column=0, padx=4, pady=7, sticky=W)

                        txt_otp = ttk.Entry(forgot.window, textvariable=forgot.userInput, font=(
                            'arial', 13, 'bold'))
                        txt_otp.grid(row=2, column=1, padx=4, pady=7, sticky=W)

                        btn_next = Button(forgot.window, text='Next', command=lambda: forgot.checkotp2(), font=(
                            "arial", 15, "bold"), width=13, bg='orange', fg='light grey')
                        btn_next.grid(row=4, column=1, padx=1, pady=3)








                    

    def otp(x):
        forgot.n = random.randint(100000, 999999)
        forgot.client = Client(
            "ACd0367c3fdfc62f05a02c86817d45fc15", "5e2de945fd5f7f6af6c3976f88b4c484")
        forgot.client.messages.create(to=[x], from_='+1 562 837 2323',
                                         body=f"OTP to reset your password- {forgot.n}")

    def checkotp():
            if int(forgot.userInput.get()) == forgot.n:
                forgot.n = "done"
                forgot.window2 = Toplevel()
                forgot.window2.title("otp verification")
                forgot.window2.geometry("560x350+400+170")

                lbl_new = Label(forgot.window2, text="Enter New Password:", font=(
                    'arial', 14, 'bold'), bg='light grey')
                lbl_new.grid(row=2, column=0, padx=4, pady=7, sticky=W)

                txt_new = ttk.Entry(forgot.window2, textvariable=forgot.new1, font=(
                    'arial', 13, 'bold'))
                txt_new.grid(row=2, column=1, padx=4, pady=7, sticky=W)

                lbl_new2 = Label(forgot.window2, text="Re-Enter New Password:", font=(
                    'arial', 14, 'bold'), bg='light grey')
                lbl_new2.grid(row=3, column=0, padx=4, pady=7, sticky=W)

                txt_new2 = ttk.Entry(forgot.window2, show="*",textvariable=forgot.new2, font=(
                    'arial', 13, 'bold'))
                txt_new2.grid(row=3, column=1, padx=4, pady=7, sticky=W)

                btn_savee = Button(forgot.window2, text='Save', command=lambda:forgot.update_data1(), font=(
                    "arial", 15, "bold"), width=13, bg='orange', fg='light grey')
                btn_savee.grid(row=4, column=1, padx=1, pady=3)

              

                





            elif forgot.n == "done":
                messagebox.showinfo("show info", "otp already has been used")

            else:
                messagebox.showerror("Error", "Invalid OTP")


    def checkotp2():
            if int(forgot.userInput.get()) == forgot.n:
                forgot.n = "done"
                forgot.window2 = Toplevel()
                forgot.window2.title("otp verification")
                forgot.window2.geometry("560x350+400+170")

                lbl_new = Label(forgot.window2, text="Enter New Password:", font=(
                    'arial', 14, 'bold'), bg='light grey')
                lbl_new.grid(row=2, column=0, padx=4, pady=7, sticky=W)

                txt_new = ttk.Entry(forgot.window2, textvariable=forgot.new1, font=(
                    'arial', 13, 'bold'))
                txt_new.grid(row=2, column=1, padx=4, pady=7, sticky=W)

                lbl_new2 = Label(forgot.window2, text="Re-Enter New Password:", font=(
                    'arial', 14, 'bold'), bg='light grey')
                lbl_new2.grid(row=3, column=0, padx=4, pady=7, sticky=W)

                txt_new2 = ttk.Entry(forgot.window2, show="*",textvariable=forgot.new2, font=(
                    'arial', 13, 'bold'))
                txt_new2.grid(row=3, column=1, padx=4, pady=7, sticky=W)

                btn_savee = Button(forgot.window2, text='Save', command=lambda: forgot.update_data2(), font=(
                    "arial", 15, "bold"), width=13, bg='orange', fg='light grey')
                btn_savee.grid(row=4, column=1, padx=1, pady=3)


            elif forgot.n == "done":
                messagebox.showinfo("show info", "otp already has been used")

            else:
                messagebox.showerror("Error", "Invalid OTP")



    def update_data1():
        if forgot.new1.get() == "" or forgot.new2.get() == "":
            messagebox.showerror('Error', 'All fields are required')
        
        elif forgot.new1.get()!=forgot.new2.get():
            messagebox.showerror('Error','Both should be same')
        
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure..?')
                if update > 0:
                    cnx = mysql.connector.connect(
                        host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                    my_cursor = cnx.cursor()

                    my_cursor.execute('UPDATE instructor SET password=%s WHERE Instructor_ID=%s', (

                        forgot.new1.get(),
                        forgot.var_rgid.get(),
                        
                    ))
                else:
                    if not update:
                        return
                cnx.commit()
                cnx.close()
                messagebox.showinfo(
                    'success', 'Go back to Login Page and Login with your new password', parent=forgot.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=forgot.root)


    def update_data2():
        if forgot.new1.get() == "" or forgot.new2.get() == "":
            messagebox.showerror('Error', 'All fields are required')

        elif forgot.new1.get() != forgot.new2.get():
            messagebox.showerror('Error', 'Both should be same')

        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure..?')
                if update > 0:
                    cnx = mysql.connector.connect(
                        host='localhost', port=3306, user='root', password='Rohan@$$$1', database='python_project')
                    my_cursor = cnx.cursor()

                    my_cursor.execute('UPDATE student SET Password=%s WHERE Register_Number=%s', (

                        forgot.new1.get(),
                        forgot.var_rgid.get(),

                    ))
                else:
                    if not update:
                        return
                cnx.commit()
                cnx.close()
                messagebox.showinfo(
                    'success', 'Go back to Login Page and Login with your new password', parent=forgot.root)
            except Exception as se:
                messagebox.showerror(
                    'ERROR', f'Due To:{str(se)}', parent=forgot.root)







if __name__ == '__main__':
    win = Tk()
    app = forgot(win)
    win.mainloop()
   