import mysql.connector
from pandas import *
from tabulate import tabulate
current_user = []
userexists = False


mycon = mysql.connector.connect(
    host="localhost", user="root", password="1234", database="library")
if not mycon:
    print("Error in connecting")
mycursor = mycon.cursor()


# create a new user
def new_user(name, password, phoneNo, address):
    # Exception Handling

    global mycursor
    global current_user
    Initial_issue = 0
    credentials = [name, password, address, phoneNo, Initial_issue]
    if phoneNo.isdigit() and len(phoneNo) == 10 and len(password) > 5:
        mycursor.execute("insert into usersdata(Name,Password,PhoneNo,Address,BooksIssued) values('{}','{}','{}','{}',{})".format(
            name, password, phoneNo, address, Initial_issue))
        mycon.commit()
        current_user.extend(credentials)
        current_user.append(0)

        return True
    else:
        if not phoneNo.isdigit():
            return "Invalid phoneNo"
        else:
            return "Password too short"

    return False


# logging in a existing user
def existing_user(userId_phn, password):
    global mycursor
    global userexists
    global current_user
    credentials = [userId_phn, password]
    mycursor.execute("select * from usersdata")
    data = mycursor.fetchall()
    for i in data:
        list(i)
        entered_credentials = [str(i[2]), i[1]]
        if entered_credentials == credentials:
            userexists = True
            current_user = list(i)
            break
        entered_credentials2 = [str(i[3]), str(i[1])]
        if entered_credentials2 == credentials:
            userexists = True
            x = list(i)
            current_user = list(i)
            break

    if userexists == True:
        return True
    else:
        return False


# function to edit phone number
def phno_edit(memID, phoneNo):
    # Exception Handling
    try:
        qry = "select * from usersdata where userId='{}';".format(memID)
        mycursor.execute(qry)
        r = mycursor.fetchone()
        if r:
            qry1 = "update usersdata set PhoneNo='{}' where userId='{}';".format(
                phoneNo, memID)
            mycursor.execute(qry1)
            mycon.commit()
            return True
        else:
            return "Wrong userId"
    except:
        return False


# function to edit address
def ad_edit(memID, address):
    # Exception Handling
    try:
        qry = "select * from usersdata where userId='{}';".format(memID)
        mycursor.execute(qry)
        r = mycursor.fetchone()
        if r:
            qry1 = "update usersdata set address='{}' where userId={};".format(
                address, memID)
            mycursor.execute(qry1)
            mycon.commit()
            return True
        else:
            return "Wrong userId"
    except:
        return "False"


# function to change password
def pwd_edit(memID, password):
    # Exception Handling
    try:
        qry = "select * from usersdata where userId='{}';".format(memID)
        mycursor.execute(qry)
        r = mycursor.fetchone()
        if r:

            qry1 = "update usersdata set Password='{}' where userId='{}';".format(
                password, memID)
            mycursor.execute(qry1)
            mycon.commit()
            return True

        else:
            return "Wrong userId"
    except:
        return False


def member_delete(memID):  # function to delete a member
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


def member_search(memID):  # funtion to search for a member
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


# function returns an array with the information of the current user
def current_users():
    return current_user


# function returns the userID of the current user after taking in the name
def current_user_id(Name):
    mycursor.execute("select * from usersdata")
    data = mycursor.fetchall()
    for i in data:
        list(i)
        if Name == str(i[0]):
            return str(i[2])
            break
