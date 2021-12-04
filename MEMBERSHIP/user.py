import mysql.connector
from pandas import *
from tabulate import tabulate


mycon = mysql.connector.connect(
    host="localhost", user="root", password="", database="")

if not mycon:
    print("Error in connecting")
mycursor = mycon.cursor()


def new_user(name, password, phoneNo, address):
    # Exception Handling
    try:
        global mycursor
        Initial_issue = 0
        if phoneNo.isdigit() and len(phoneNo) == 10 and len(password) > 5:
            credentials = [name, password, address, phoneNo, Initial_issue]
            mycursor.execute("insert into usersdata(Name,Password,PhoneNo,Address,BooksIssued) values('{}','{}','{}','{}',{})".format(
                name, password, phoneNo, address, Initial_issue))
            mycon.commit()
            return True
        else:
            if not phoneNo.isdigit():
                print("error:phoneNo all digits not satsfied ")
                return False
            else:
                print("error: password too short")
                return False
    except:
        return False


def member_edit(memID, phoneNo, address):
    # Exception Handling
    try:
        qry = "select * from usersdata where userId='{}';".format(memID)
        mycursor.execute(qry)
        r = mycursor.fetchone()
        if r:
            def update():
                qry = "update usersdata set Address='{}' where userId='{}';".format(
                    address, memID)
                qry1 = "update usersdata set PhoneNo='{}' where userId='{}';".format(
                    phoneNo, memID)
                mycursor.execute(qry)
                mycursor.execute(qry1)
                mycon.commit()
                return True
            update()
        else:
            return False
    except:
        return False


def member_delete(memID):
    # Exception Handling
    try:
        qry = "select * from usersdata where userId='{}';".format(memID)
        mycursor.execute(qry)
        r = mycursor.fetchone()
        if r:
            qry = "delete from usersdata where userId='{}';".format(memID)
            mycursor.execute(qry)
            mycon.commit()
            return True
        else:
            return False
    except:
        return False


def member_search(memID):
    # Exception Handling
    try:
        qry = "select * from usersdata where userId='{}';".format(memID)
        mycursor.execute(qry)
        r = mycursor.fetchone()
        if r:
            qry = "select * from usersdata where userId='{}';".format(memID)
            df = read_sql(qry, mycon)
            print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
            return True
        else:
            False
    except:
        return False


userexists = False


def existing_user(userId_phn, password):
    global mycursor
    global userexists
    credentials = [userId_phn, password]
    mycursor.execute("select * from usersdata")
    data = mycursor.fetchall()
    for i in data:
        list(i)
        entered_credentials = [str(i[2]), i[1]]
        if entered_credentials == credentials:
            userexists = True
            break
        entered_credentials2 = [str(i[3]), str(i[1])]
        if entered_credentials2 == credentials:
            userexists = True
            break

    if userexists == True:
        return True
    else:
        return False
