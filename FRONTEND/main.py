from books import *
from libraryMS.MEMBERSHIP.user import *
from libraryMS.ISSUE.transaction import *
# C:\Users\dipan\AppData\Local\Programs\Python\Python310\Lib\site-packages
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

mycon = mysql.connector.connect(
    host="localhost", user="root", password="1234", database="library")

if not mycon:
    print("Error in connecting")
mycursor = mycon.cursor()

userID = ''
root = Tk()
root.iconbitmap('E:/libraryMS/FRONTEND/icon.ico')
root.geometry("690x500")
frame = LabelFrame(root)
frame.pack(side="top", expand='yes', fill='both')
# root.attributes('-fullscreen', True)
root.title("cubra")
root.resizable(False, False)
# root.bind('<Escape>', lambda e: root.destroy()) make escape exit the program


def close_window():
    root.destroy()


def clearFrame():
    for widget in frame.winfo_children():
        widget.destroy()


def verifyissue():
    if bookid.get == "":
        messagebox.showinfo("Error", "Please complete the required field!")
    elif book_issue(str(userID), str(bookid.get())) == "Book Issued":
        messagebox.showinfo(
            "Issued", "Book issued, return it before 14 days to exempt any fine")
        after_login_signup()
    else:
        messagebox.showinfo("Error", book_issue(
            str(userID), str(bookid.get())))


def verifyreturn():
    if bookid.get == "":
        messagebox.showinfo("Error", "Please complete the required field!")
    elif book_return(str(userID), str(bookid.get())) == "Book Returned":
        messagebox.showinfo(
            "Returned", "Thankyou. May you have a good day ahead !")
        after_login_signup()
    else:
        messagebox.showinfo("Error", book_return(
            str(userID), str(bookid.get())))


def makesearch():
    clearFrame()
    mycursor.execute("select * from bookstable ")
    tv = ttk.Treeview(frame)
    tv["columns"] = ("1", "2", "3", "4")
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
        tv.insert(parent='', index='end', iid=i,
                  values=(row[0], row[1], row[2], row[6]))
        #tv.insert('', i, text='', values=(row[0], row[1], row[2], row[4]))
        i = i+1
    tv.place(x=20, y=80)


def make():
    clearFrame()
    #a = str(bookid2.get())
    mycursor.execute("select * from bookstable ")

    # book_search(int(bookid2.get()))
    tv = ttk.Treeview(frame, columns=(1, 2, 3, 4),
                      show="headings", height="15")
    tv.place(x=20, y=80)

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
    back.place(x=260, y=430, width=155)


def after_searchForbook():
    clearFrame()
    lblfrstrow = Label(frame, text="Title *")
    lblfrstrow.place(x=150, y=90)

    global bookid2
    bookid2 = Entry(frame, width=35, borderwidth=5)
    bookid2.place(x=150, y=110, width=200)

    verifysearch = Button(frame, text="SEARCH", command=make,
                          bg='yellow')
    verifysearch.place(x=165, y=150, width=155)

    back = Button(frame, text="Main Menu", bg='cyan',
                  command=after_login_signup)
    back.place(x=165, y=180, width=155)


def after_issuebtn():
    clearFrame()
    lblfrstrow = Label(frame, text="Book ID -")
    lblfrstrow.place(x=50, y=20)

    global bookid
    bookid = Entry(frame, width=35, borderwidth=5)
    bookid.place(x=150, y=20, width=200)

    verifyissuebtn = Button(frame, text="ISSUE",
                            bg='yellow', command=verifyissue)
    verifyissuebtn.place(x=160, y=80, width=155)

    back = Button(frame, text="Main Menu", bg='cyan',
                  command=after_login_signup)
    back.place(x=160, y=110, width=155)


def after_returnbtn():
    clearFrame()
    lblfrstrow = Label(frame, text="Book ID -")
    lblfrstrow.place(x=50, y=20)

    global bookid
    bookid = Entry(frame, width=35, borderwidth=5)
    bookid.place(x=150, y=20, width=200)

    verifyissuebtn = Button(frame, text="RETURN",
                            bg='yellow', command=verifyreturn)
    verifyissuebtn.place(x=160, y=80, width=155)

    back = Button(frame, text="Main Menu", bg='cyan',
                  command=after_login_signup)
    back.place(x=160, y=110, width=155)
    return


def account():
    l = Label(frame, text="hello")
    l.place(x=0, y=0)


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
                      width=35, command=after_issuebtn)
    issuebtn.place(x=150, y=50)
    returnbtn = Button(frame, text="RETURN BOOKS",
                       width=35, command=after_returnbtn)
    returnbtn.place(x=150, y=80)
    searchbtn = Button(frame, text="SHOW ALL BOOKS",
                       width=35, command=make)
    searchbtn.place(x=150, y=110)


def signup_click():
    error = new_user(str(Username2.get()), str(password2.get()),
                     str(contact2.get()), str(address2.get()))

    if error != True:
        messagebox.showinfo("Error", error)
        Username2.delete(0, END)
        password2.delete(0, END)
        contact2.delete(0, END)
        address2.delete(0, END)

    elif Username2.get() == "" or password2.get() == "" or contact2.get() == "" or address2.get() == "":
        messagebox.showinfo("Error", "Please complete the required field!")

    elif error:
        messagebox.showinfo(
            "Success", "User Created Succesfully. Use Your Phone number as your username.")
        mainpro()
    else:
        messagebox.messagebox.showinfo("Error", "User cant be created")


def signup():
    clearFrame()

    lblfrstrow = Label(frame, text="Name -")
    lblfrstrow.place(x=50, y=20)
    global Username2
    Username2 = Entry(frame, width=35, borderwidth=5)
    Username2.place(x=150, y=20, width=200)

    lblsecrow = Label(frame, text="Password -")
    lblsecrow.place(x=50, y=50)

    global password2
    password2 = Entry(frame, width=35, borderwidth=5)
    password2.place(x=150, y=50, width=200)

    lblthrdrow = Label(frame, text="Contact Number -")
    lblthrdrow.place(x=50, y=80)

    global contact2
    contact2 = Entry(frame, width=35, borderwidth=5)
    contact2.place(x=150, y=80, width=200)

    lblthrdrow = Label(frame, text="Address -")
    lblthrdrow.place(x=50, y=110)

    global address2
    address2 = Entry(frame, width=35, borderwidth=5)
    address2.place(x=150, y=110, width=200)

    global signinbtn2
    signinbtn2 = Button(frame, text="Create Account", command=signup_click,
                        fg='yellow')
    signinbtn2.place(x=160, y=190, width=155)


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


def mainpro():
    clearFrame()
    global Username
    global password
    # setting bg
    # mylabel = Label(frame, image=bg)
    # mylabel.place(x=0, y=0, relheight=1, relwidth=1)
    lblfrstrow = Label(frame, text="Username *")
    lblfrstrow.place(x=150, y=90)

    Username = Entry(frame, width=35, borderwidth=5)
    Username.place(x=150, y=110, width=200)

    lblsecrow = Label(frame, text="Password *")
    lblsecrow.place(x=150, y=150)

    password = Entry(frame, width=35, borderwidth=5)
    password.place(x=150, y=170, width=200)

    login_btn = PhotoImage(
        file='E:/libraryMS/FRONTEND/login.png')
    submitbtn = Button(frame, image=login_btn, command=login, borderwidth=0)
    submitbtn.place(x=160, y=220, width=155)

    registerbtn = PhotoImage(file='FRONTEND/reg.png')
    register = Button(frame, image=registerbtn, command=signup, borderwidth=0)
    register.place(x=160, y=300, width=155)

    root.mainloop()


mainpro()
