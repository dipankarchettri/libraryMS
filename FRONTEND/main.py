from libraryMS.BOOKS.books import *
from libraryMS.MEMBERSHIP.user import *
from libraryMS.ISSUE.transaction import *
# C:\Users\dipan\AppData\Local\Programs\Python\Python310\Lib\site-packages\libraryproject
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.iconbitmap('E:/libraryMS/FRONTEND/icon.ico')
root.geometry("500x500")
#root.attributes('-fullscreen', True)
root.title("cubra")
root.configure(background='pink')
# root.bind('<Escape>', lambda e: root.destroy()) make escape exit the program

frame = LabelFrame(root, bg="pink")
frame.pack(side="top", expand='yes', fill='both')

lblfrstrow = Label(frame, text="Username -")
lblfrstrow.place(x=50, y=20)

Username = Entry(frame, width=35, borderwidth=5)
Username.place(x=150, y=20, width=200)

lblsecrow = Label(frame, text="Password -")
lblsecrow.place(x=50, y=50)

password = Entry(frame, width=35, borderwidth=5)
password.place(x=150, y=50, width=200)

currentUser = ''


def close_window():
    root.destroy()


def clearFrame():
    for widget in frame.winfo_children():
        widget.destroy()


def login():
    if Username.get() == "" or password.get() == "":
        messagebox.showinfo("Error", "Please complete the required field!")
    elif(existing_user(str(Username.get()), str(password.get()))):
        #messagebox.showinfo("Welcome","valid username or password.")
        clearFrame()

        x = current_users()
        name = "Hello "+x[1]
        lblfrstrow = Label(frame, text=name, bg='pink')
        lblfrstrow.place(x=0, y=0)
        # lblscnrow = Label(frame, text="Welcome to the library", bg='pink')
        # lblscnrow.place(x=0, y=10)

    else:
        messagebox.showinfo("Error", "Invalid username or password.")
        Username.delete(0, END)
        password.delete(0, END)


def signup():
    clearFrame()

    lblfrstrow = Label(frame, text="Name -")
    lblfrstrow.place(x=50, y=20)

    Username = Entry(frame, width=35, borderwidth=5)
    Username.place(x=150, y=20, width=200)

    lblsecrow = Label(frame, text="Password -")
    lblsecrow.place(x=50, y=50)

    password = Entry(frame, width=35, borderwidth=5)
    password.place(x=150, y=50, width=200)

    lblthrdrow = Label(frame, text="Contact Number -")
    lblthrdrow.place(x=50, y=80)

    contact = Entry(frame, width=35, borderwidth=5)
    contact.place(x=150, y=80, width=200)

    lblthrdrow = Label(frame, text="Address -")
    lblthrdrow.place(x=50, y=110)

    address = Entry(frame, width=35, borderwidth=5)
    address.place(x=150, y=110, width=200)

    def signup_click():
        error = new_user(str(Username.get()), str(
            password.get()), str(contact.get()), str(address.get()))
        if Username.get() == "" or password.get() == "" or contact.get() == "" or address.get() == "":
            messagebox.showinfo("Error", "Please complete the required field!")
        elif error != True:
            messagebox.showinfo("Error", error)
            Username.delete(0, END)
            password.delete(0, END)
            contact.delete(0, END)
            address.delete(0, END)

        elif new_user(str(Username.get()), str(password.get()), str(contact.get()), str(address.get())):
            messagebox.showinfo("Success", "User Created Succesfully")
            clearFrame()
        else:
            messagebox.messagebox.showinfo("Error", "User cant be created")

    signinbtn = Button(frame, text="Create Account", command=signup_click,
                       fg='yellow')
    signinbtn.place(x=160, y=190, width=155)


submitbtn = Button(frame, text="Login", command=login,
                   bg='yellow')
submitbtn.place(x=160, y=135, width=155)

gosignupbtn = Button(frame, text="Not a member? SignIn Now...", command=signup,
                     fg='blue')
gosignupbtn.place(x=160, y=190, width=155)


root.mainloop()
