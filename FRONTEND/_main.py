# C:\Users\dipan\AppData\Local\Programs\Python\Python310\Lib\site-packages
# importing the library(cubra)
from logging import warning
from tkinter import font
from books import *
from user import *
from transaction import *
from report import *

# importing tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font

import mysql.connector


# connecting to the database
mycon = mysql.connector.connect(
    host="localhost", user="root", password="1234", database="library")
if not mycon:
    print("Error in connecting")
mycursor = mycon.cursor()

# variable to store the current userID (user who is using the application )
userID = ''

# setting uo the tkinter window
root = Tk()
root.iconbitmap('FRONTEND/iconAndImages/icon.ico')
root.geometry("690x450")
# root.attributes('-fullscreen', True)
# root.bind('<Escape>', lambda e: root.destroy()) make escape exit the program
root.title("cubra")
root.resizable(False, False)
root.configure(bg='pink')

# setting up the frame
frame = LabelFrame(root)
frame.pack(side="top", expand='yes', fill='both')


# clear the frame(window)


def clearFrame():
    for widget in frame.winfo_children():
        widget.destroy()


# function that verifys issue after taking in the bookid
def verifyissue():
    try:
        if bookid.get == "":
            messagebox.showinfo("Error", "Please complete the required field!")
        elif book_issue(str(userID), str(bookid.get())) == "Book Issued":
            messagebox.showinfo(
                "Issued", "Book issued, return it before 14 days to exempt any fine")
            after_login_signup()
        else:
            messagebox.showinfo("Error", book_issue(
                str(userID), str(bookid.get())))
    except:
        messagebox.showinfo("Error", "Can't verify issue")


# function that verifys return after taking in the bookid
def verifyreturn():
    try:
        if bookid6.get == "":
            messagebox.showinfo("Error", "Please complete the required field!")
        elif book_return(int(userID), int(bookid6.get())) == "Book Returned":
            messagebox.showinfo(
                "Returned", "Thankyou. May you have a good day ahead !")
            after_login_signup()
        else:
            messagebox.showinfo("Error", book_return(
                int(userID), int(bookid6.get())))
    except:
        messagebox.showinfo("Error", "Can't verify return")


# function to show all the books in the library to the users
def showallbooks():
    clearFrame()
    # a = str(bookid2.get())
    mycursor.execute("select * from bookstable ")

    # book_search(int(bookid2.get()))
    tv = ttk.Treeview(frame, columns=(1, 2, 3, 4),
                      show="headings", height="15")
    tv.place(x=20, y=20)

    tv.column("1", anchor=CENTER, width=120, minwidth=120)
    tv.column("2", anchor=CENTER, width=200, minwidth=120)
    tv.column("3", anchor=CENTER, width=200, minwidth=120)
    tv.column("4", anchor=CENTER, width=120, minwidth=120)

    tv.heading(1, text="BookID")
    tv.heading(2, text="Title")
    tv.heading(3, text="Author")
    tv.heading(4, text="Availability")
    i = 0
    for row in mycursor:
        if row[6] > 0:
            tv.insert('', i, text='', values=(
                row[0], row[1], row[2], "Available"))
        else:
            tv.insert('', i, text='', values=(
                row[0], row[1], row[2], " Not Available"))
        i = i+1

    back = Button(frame, text="Main Menu", bg='cyan',
                  command=after_login_signup)
    back.place(x=260, y=350, width=155)


# function that  decides what happen what happens when the user clicks the issue option after logging in
def after_issuebtn():
    clearFrame()
    lblfrstrow = Label(frame, text="Book ID *")
    lblfrstrow.place(x=150, y=150)

    global bookid
    bookid = Entry(frame, width=35, borderwidth=5)
    bookid.place(x=150, y=170, width=350)

    verifyissuebtn = Button(frame, text="ISSUE",
                            bg='yellow', command=verifyissue)
    verifyissuebtn.place(x=230, y=220, width=155)

    back = Button(frame, text="Back", bg='cyan',
                  command=after_login_signup)
    back.place(x=230, y=280, width=155)


# function that  decides what happen what happens when the user clicks the return option after logging in
def after_returnbtn():
    clearFrame()
    lblfrstrow = Label(frame, text="Book ID *")
    lblfrstrow.place(x=150, y=150)

    global bookid6
    bookid6 = Entry(frame, width=35, borderwidth=5)
    bookid6.place(x=150, y=170, width=350)

    verifyissuebtn = Button(frame, text="RETURN",
                            bg='yellow', command=verifyreturn)
    verifyissuebtn.place(x=230, y=220, width=155)

    back = Button(frame, text="Back", bg='cyan',
                  command=after_login_signup)
    back.place(x=230, y=280, width=155)
    return


# this function changes the password by calling the pwd_edit function from the library
def change_passworde():
    a = paw.get()
    if paw.get == "":
        messagebox.showinfo("Error", "Please complete the required field")
    elif len(paw.get()) < 6:
        messagebox.showinfo("Error", "Password too short ")
    elif pwd_edit(a, paw.get()):
        pwd_edit(int(userID), a)
        messagebox.showinfo("Success", "Password Changed")
        account()
    else:
        messagebox.showinfo("Success", "Error")


# this function changes the phone number by calling the phno_edit function from the library
def change_phone():
    a = phone2.get()
    if phone2.get == "":
        messagebox.showinfo("Error", "Please complete the required field")
    elif len(phone2.get()) != 10:
        messagebox.showinfo("Error", "Invalid Phone No")
    elif phno_edit(int(userID), phone2.get()):
        phno_edit(int(userID), a)
        messagebox.showinfo("Success", "PhoneNO Changed")
        account()
    else:
        messagebox.showinfo("Success", phno_edit(int(userID), a))


# this function changes the address by calling the ad_edit function from the library
def change_address():

    global address
    if address.get == "":
        messagebox.showinfo("Error", "Please complete the required field")
    a = address.get()
    if ad_edit(int(userID), address.get()):
        ad_edit(int(userID), a)
        messagebox.showinfo("Success", "Address Changed")
        account()
    else:
        messagebox.showinfo("Success", ad_edit(int(userID), a))


# this function deletes the user account by calling the member_delete function from the library
def delete_account():
    member_delete(int(userID))
    messagebox.showinfo("GoodBye", "We are sad to see you GO!!!")
    mainpro()


# entry box for change passwprd
def passwor():
    clearFrame()
    global paw
    paw = Entry(frame, width=35, borderwidth=5)
    paw.place(x=150, y=170, width=350)

    lblsecrow = Label(frame, text="New Password *")
    lblsecrow.place(x=150, y=150)

    submit = Button(frame, text="Change Password",
                    bg='red', command=change_passworde)
    submit.place(x=230, y=220, width=155)

    back = Button(frame, text="Back", bg='cyan',
                  command=account)
    back.place(x=230, y=280, width=155)


# entry box for change phone no
def phone():
    clearFrame()
    global phone2
    phone2 = Entry(frame, width=35, borderwidth=5)
    phone2.place(x=150, y=170, width=350)

    lblsecrow = Label(frame, text="New PhoneNO *")
    lblsecrow.place(x=150, y=150)

    submit = Button(frame, text="Change PhoneNo",
                    bg='red', command=change_phone)
    submit.place(x=230, y=220, width=155)

    back = Button(frame, text="Back", bg='cyan',
                  command=account)
    back.place(x=230, y=280, width=155)


# entry box for change address
def address():
    clearFrame()
    global address
    address = Entry(frame, width=35, borderwidth=5)
    address.place(x=150, y=170, width=350)

    lblsecrow = Label(frame, text="New Address *")
    lblsecrow.place(x=150, y=150)

    submit = Button(frame, text="Change Address", bg='red',
                    command=change_address)
    submit.place(x=230, y=220, width=155)

    back = Button(frame, text="Back", bg='cyan',
                  command=account)
    back.place(x=230, y=280, width=155)


# this function defines what happens after the user click the accountsettings from the right hand top corner dropdown menu
def account():
    clearFrame()

    l = Label(frame, text="Change account settings")
    l.place(x=500/2, y=50)
    changeaddress = Button(
        frame, text="Change Addres", width=35, borderwidth=5, command=address)
    changeaddress.place(x=180, y=80)

    changephone = Button(
        frame, text="Change PhoneNo", width=35, borderwidth=5, command=phone)
    changephone.place(x=180, y=120)

    def warning1():
        ans = messagebox.askyesno(
            "Delete", "Are you sure you want to change your password?")
        if ans:
            passwor()
    changepassword = Button(frame, text="Change Password",
                            width=35, borderwidth=5, command=warning1)
    changepassword.place(x=180, y=160)

    def warning():
        ans = messagebox.askyesno(
            "Delete", "Are you sure you want to delete your account?")
        if ans:
            delete_account()
    delete = Button(
        frame, text="Delete Account", width=35, borderwidth=5, bg="red", comman=warning)
    delete.place(x=180, y=200)

    back = Button(frame, text="Main Menu", bg='cyan',
                  command=after_login_signup)
    back.place(x=230, y=280, width=155)


# this function defines what happens after the user login
def after_login_signup():
    clearFrame()
    x = current_users()
    global userID
    name = str(x[0])
    userID = current_user_id(name)

    def selected(event):
        if clicked.get() == "logout":
            clearFrame()
            mainpro()
        elif clicked.get() == "accountsettings":
            clearFrame()
            account()

    clicked = StringVar()
    clicked.set(name)

    drop = OptionMenu(frame, clicked, name, "accountsettings",
                      "logout", command=selected)
    drop.place(x=0, y=0)

    issuebtn = Button(frame, text="ISSUE BOOKS",
                      width=35, borderwidth=5, command=after_issuebtn)
    issuebtn.place(x=180, y=130)
    returnbtn = Button(frame, text="RETURN BOOKS",
                       width=35, borderwidth=5, command=after_returnbtn)
    returnbtn.place(x=180, y=170)
    searchbtn = Button(frame, text="SHOW ALL BOOKS",
                       width=35, borderwidth=5, command=showallbooks)
    searchbtn.place(x=180, y=210)
    chart = Button(frame, text="BEST READING BOOKS", command=col_chart,
                   width=35, borderwidth=5)
    chart.place(x=180, y=250)


#  button function for signing up(new users)
def signup_click():
    error = new_user(str(Username2.get()), str(password2.get()),
                     str(contact2.get()), str(address2.get()))
    if Username2.get() == "" or password2.get() == "" or contact2.get() == "" or address2.get() == "":
        messagebox.showinfo("Error", "Please complete the required field!")

    elif error != True:
        messagebox.showinfo("Error", error)
        Username2.delete(0, END)
        password2.delete(0, END)
        contact2.delete(0, END)
        address2.delete(0, END)

    elif error:
        messagebox.showinfo(
            "Success", "User Created Succesfully. Use Your Phone number as your username.")
        mainpro()
    else:
        messagebox.messagebox.showinfo("Error", "User cant be created")


# this function takes all the needed data for new user
def signup():
    clearFrame()

    lblfrstrow = Label(frame, text="Name *")
    lblfrstrow.place(x=150, y=60)
    global Username2
    Username2 = Entry(frame, width=35, borderwidth=5)
    Username2.place(x=150, y=80, width=200)

    lblsecrow = Label(frame, text="Password *")
    lblsecrow.place(x=150, y=110)

    global password2
    password2 = Entry(frame, width=35, borderwidth=5)
    password2.place(x=150, y=130, width=200)

    lblthrdrow = Label(frame, text="Contact Number *")
    lblthrdrow.place(x=150, y=160)

    global contact2
    contact2 = Entry(frame, width=35, borderwidth=5)
    contact2.place(x=150, y=180, width=200)

    lblthrdrow = Label(frame, text="Address *")
    lblthrdrow.place(x=150, y=210)

    global address2
    address2 = Entry(frame, width=35, borderwidth=5)
    address2.place(x=150, y=230, width=200)

    global signinbtn2
    signinbtn2 = Button(frame, text="Create Account",
                        command=signup_click, width=35, borderwidth=5, bg="yellow")
    signinbtn2.place(x=160, y=300, width=155)

    login = Button(frame, text="Back To Login",
                   command=mainpro, width=35, borderwidth=5)
    login.place(x=160, y=340, width=155)


# button function login(existing users)
def login():

    if Username.get() == "" or password.get() == "":
        messagebox.showinfo("Error", "Please complete the required field!")
    elif(existing_user(str(Username.get()), str(password.get()))):
        # messagebox.showinfo("Welcome","valid username or password.")
        clearFrame()
        after_login_signup()
        # lblscnrow = Label(frame, text="Welcome to the library", bg='pink')
        # lblscnrow.place(x=0, y=10)

    else:
        messagebox.showinfo("Error", "Invalid username or password.")
        Username.delete(0, END)
        password.delete(0, END)


# button function for adding books
def addbookbutton():
    try:
        if bookname.get() == "" or author.get() == "" or genre.get() == "" or publisher.get() == "" or stock.get() == "":
            messagebox.showinfo(
                "Missing fields", "Please complete the required fields")
        elif add_book(bookname.get(), author.get(), genre.get(), publisher.get(), int(stock.get())):
            messagebox.showinfo(
                "Success", "Successfully added the book into the library")
            afteradlog()
        else:
            messagebox.showinfo("Error", "Could not add the books")
    except:
        messagebox.showinfo("Error", "Check your stock field properly!!!")


# button fnction for deleting buttons
def deletebooksbutton():
    try:
        if bookid1.get() == "":
            messagebox.showinfo("Error", "Complete the required field")
        elif book_delete(int(bookid1.get())):
            messagebox.showinfo("Success", "Books Successfully Deleted")
            afteradlog()
        else:
            messagebox.showinfo("Error", "Wrong BookID")
    except:
        messagebox.showinfo("Error", "Wrong BookID")


# button function for showing all members
def showallmembers():
    clearFrame()
    # a = str(bookid2.get())
    mycursor.execute("select * from usersdata ")

    # book_search(int(bookid2.get()))
    tv = ttk.Treeview(frame, columns=(1, 2, 3, 4),
                      show="headings", height="15")
    tv.place(x=20, y=20)

    tv.column("1", anchor=CENTER, width=120, minwidth=120)
    tv.column("2", anchor=CENTER, width=200, minwidth=120)
    tv.column("3", anchor=CENTER, width=200, minwidth=120)
    tv.column("4", anchor=CENTER, width=120, minwidth=120)

    tv.heading(1, text="UserID")
    tv.heading(2, text="Name")
    tv.heading(3, text="Phone No")
    tv.heading(4, text="Current Books Issued")
    i = 0
    for row in mycursor:
        tv.insert('', i, text='', values=(
            row[2], row[0], row[3], row[5]))
        i = i+1

    back = Button(frame, text="Back", bg='cyan',
                  command=afteradlog)
    back.place(x=260, y=350, width=155)


# entry box for deleting books
def delbboks():
    clearFrame()
    lblfrstrow = Label(frame, text="BookID *")
    lblfrstrow.place(x=150, y=150)
    global bookid1
    bookid1 = Entry(frame, width=35, borderwidth=5)
    bookid1.place(x=150, y=170, width=350)

    def warning1():
        ans = messagebox.askyesno(
            "Delete", "Are you sure you want to delete this book?")
        if ans:
            deletebooksbutton
    delbtn = Button(frame, text="DELETE",
                    width=35, borderwidth=5, command=warning1, fg="red")
    delbtn.place(x=180, y=220)
    delbtn = Button(frame, text="Back", width=35,
                    borderwidth=5, command=afteradlog, bg="cyan")
    delbtn.place(x=180, y=280)


# entry boxes for adding books
def adaddboks():
    clearFrame()
    lblfrstrow = Label(frame, text="Title *")
    lblfrstrow.place(x=150, y=70)
    global bookname
    bookname = Entry(frame, width=35, borderwidth=5)
    bookname.place(x=150, y=90, width=350)

    lblfrstrow1 = Label(frame, text="Author *")
    lblfrstrow1.place(x=150, y=120)
    global author
    author = Entry(frame, width=35, borderwidth=5)
    author.place(x=150, y=140, width=350)
    global genre
    lblfrstrow2 = Label(frame, text="Genre *")
    lblfrstrow2.place(x=150, y=170)

    genre = Entry(frame, width=35, borderwidth=5)
    genre.place(x=150, y=190, width=350)

    lblfrstrow3 = Label(frame, text="Publisher *")
    lblfrstrow3.place(x=150, y=220)
    global publisher
    publisher = Entry(frame, width=35, borderwidth=5)
    publisher.place(x=150, y=240, width=350)

    lblfrstrow = Label(frame, text="Stock *")
    lblfrstrow.place(x=150, y=270)
    global stock
    stock = Entry(frame, width=35, borderwidth=5)
    stock.place(x=150, y=290, width=350)

    addbtn = Button(frame, text="ADD", fg="red",
                    width=35, borderwidth=5, command=addbookbutton)
    addbtn.place(x=180, y=320)
    back = Button(frame, text="Back",
                  width=35, borderwidth=5, command=afteradlog, bg="cyan")
    back.place(x=180, y=360)


# this functions defines what happens after admin login
def afteradlog():
    clearFrame()
    issuebtn = Button(frame, text="ADD BOOKS", command=adaddboks,
                      width=35, borderwidth=5)
    issuebtn.place(x=180, y=130)
    returnbtn = Button(frame, text="DELETE BOOKS", command=delbboks,
                       width=35, borderwidth=5)
    returnbtn.place(x=180, y=170)
    searchbtn = Button(frame, text="SHOW ALL MEMBERS", command=showallmembers,
                       width=35, borderwidth=5)
    searchbtn.place(x=180, y=210)
    chart = Button(frame, text="SHOW STATS", command=col_chart,
                   width=35, borderwidth=5)
    chart.place(x=180, y=250)

    def warning1():
        ans = messagebox.askyesno("Delete", "Are you sure you want to logout?")
        if ans:
            mainpro()
    logout = Button(frame, text="LOGOUT", command=warning1, bg="red",
                    width=35, borderwidth=5)
    logout.place(x=180, y=290)
    return


# verify the admin logn
def adlog():
    if Username4.get() == "" or password4.get() == "":
        messagebox.showinfo("Error", "Please complete the required fields")
    elif Username4.get() == "thumbCancer" and password4.get() == "bidipta":
        messagebox.showinfo("Success", "Logged in as admin")
        afteradlog()
    elif Username4.get() != "thumbCancer" and password4.get() == "bidipta":
        messagebox.showinfo("Error", "Wrong Username")
    elif Username4.get() == "thumbCancer" and password4.get() != "bidipta":
        messagebox.showinfo("Error", "Wrong password")
    elif Username4.get() != "thumbCancer" and password4.get() != "bidipta":
        messagebox.showinfo("Error", "Wrong username and wrong password")
        Username4.delete(0, END)
        password4.delete(0, END)

    return


# entry box for admin login
def admin():
    clearFrame()
    global Username
    global password

    def selected(event):
        if clicked.get() == "memberlogin":
            clearFrame()
            mainpro()
        elif clicked.get() == "adminlogin":
            clearFrame()
            admin()

    clicked = StringVar()
    clicked.set("memberlogin")
    drop = OptionMenu(frame, clicked, "memberlogin",
                      "adminlogin", command=selected)
    drop.place(x=0, y=0)
    lblfrstrow = Label(frame, text="Administrative Username *")
    lblfrstrow.place(x=150, y=90)
    global Username4
    Username4 = Entry(frame, width=35, borderwidth=5)
    Username4.place(x=150, y=110, width=200)

    lblsecrow4 = Label(frame, text="Administrative Password *")
    lblsecrow4.place(x=150, y=150)

    global password4
    password4 = Entry(frame, width=35, borderwidth=5)
    password4.place(x=150, y=170, width=200)

    submitbtn2 = Button(frame, text="Administrative Login", command=adlog,
                        width=35, borderwidth=5)
    submitbtn2.place(x=160, y=220, width=180)


# flow of control starts form here(it defines what shows up when the users/admin starts the application)
def mainpro():
    clearFrame()
    global Username
    global password

    def selected(event):
        if clicked.get() == "memberlogin":
            clearFrame()
            mainpro()
        elif clicked.get() == "adminlogin":
            clearFrame()
            admin()

    clicked = StringVar()
    clicked.set("memberlogin")
    drop = OptionMenu(frame, clicked, "adminlogin",
                      "memberlogin", command=selected)
    drop.place(x=0, y=0)

    lblfrstrow = Label(frame, text="Username *")
    lblfrstrow.place(x=150, y=90)

    Username = Entry(frame, width=35, borderwidth=5)
    Username.place(x=150, y=110, width=200)

    lblsecrow = Label(frame, text="Password *")
    lblsecrow.place(x=150, y=150)

    password = Entry(frame, width=35, borderwidth=5)
    password.place(x=150, y=170, width=200)

    login_btn = PhotoImage(
        file='FRONTEND/iconAndImages/login.png')
    submitbtn = Button(frame, image=login_btn,
                       command=login, borderwidth=0)
    submitbtn.place(x=160, y=220, width=155)

    labpwd = Button(frame, text="Forgot Password?",
                    fg="blue", height=1, borderwidth=0)
    labpwd.place(x=250, y=200)

    registerbtn = PhotoImage(file='FRONTEND/iconAndImages/reg.png')
    register = Button(frame, image=registerbtn,
                      command=signup, borderwidth=0)
    register.place(x=160, y=300, width=155)

    root.mainloop()


# main(flow starts )
mainpro()
