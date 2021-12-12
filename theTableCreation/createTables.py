import mysql.connector as sq
mycon = sq.connect(host="localhost", user="root",
                   password="1234", database="library")
if not mycon:
    print("Error in connecting")

mycursor = mycon.cursor()


def userTable():
    global mycursor
    mycursor.execute(
        "create table usersData(Name varchar(30), Password varchar(20),userId int auto_increment,\
              PhoneNo varchar(20), Address varchar(100), BooksIssued int, primary key(userId))")
    mycursor.execute("alter table usersData auto_increment=779531")


def bookTable():
    global mycursor
    mycursor.execute(
        "create table Bookstable(bookId int auto_increment, Title varchar(100), Author varchar(50), Genre varchar(100),\
             Publisher varchar(100),NoOfCopies int, NoOfCopiesLeft int, primary key(bookId))")
    mycursor.execute("alter table Bookstable auto_increment=224672")


def issuetable():
    global mycursor
    mycursor.execute(
        "create table IssueTable(issueId int auto_increment, bookId varchar(30), userId varchar(20), DateIssued varchar(100),no_of_copies int, primary key(issueId))")
    mycursor.execute("alter table Issuetable auto_increment=171216")


def returnTable():
    global mycursor
    mycursor.execute(
        "create table ReturnTable(returnId int auto_increment, bookId varchar(30), userId varchar(20), DateReturned varchar(100),no_of_copies int, primary key(returnId))")
    mycursor.execute("alter table ReturnTable auto_increment=567889")


userTable()
bookTable()
issuetable()
returnTable()
