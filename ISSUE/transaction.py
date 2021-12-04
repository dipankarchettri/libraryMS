import datetime
import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
con = sqlt.connect(host="localhost", user="root",
                   password="", database="")
cursor = con.cursor()


# function to issue books
def book_issue(memID, bookID):
    # Exception Handling
    try:
        q1 = "select * from usersdata where userId={};".format(memID)
        cursor.execute(q1)
        r = cursor.fetchone()
        if r:
            q2 = "select bookId, NoOfCopiesLeft from bookstable where bookId={};".format(
                bookID)
            cursor.execute(q2)
            r = cursor.fetchone()
            if r:
                if r[1] > 0:
                    dt_str = str(datetime.datetime.now())
                    NoOfCopiesLeft = r[1]-1
                    q3 = "insert into issuetable(bookId,userId,DateIssued) values('{}','{}','{}');".format(
                        bookID, memID, dt_str)
                    cursor.execute(q3)
                    q4 = "update bookstable set NoOfCopiesLeft={} where bookId='{}';".format(
                        NoOfCopiesLeft, bookID)
                    cursor.execute(q4)
                    con.commit()
                    print("True")
                else:
                    print("Book not available")
            else:
                print("Wrong Book ID")

        else:
            print("Wrong UserId")
    except:
        print("Error")

# function to return books


def book_return(memID, bookID):
    # Exception Handliung
    try:
        q1 = "select * from usersdata where userID='{}';".format(memID)
        cursor.execute(q1)
        r = cursor.fetchone()
        if r:
            q2 = "select bookId, NoOfCopiesLeft from bookstable where bookId='{}';".format(
                bookID)
            cursor.execute(q2)
            r = cursor.fetchone()
            if r:
                dt_str = str(datetime.datetime.now())
                remcopies = r[1]+1
                q3 = "insert into returnTable (bookId,userId,DateReturned) values('{}','{}','{}');".format(
                    bookID, memID, dt_str)
                cursor.execute(q3)
                q4 = "update booksTable set NoOfCopiesLeft={} where bookid={};".format(
                    remcopies, bookID)
                cursor.execute(q4)
                con.commit()
                print("Book Returned...")
            else:
                print("Wrong Book ID")

        else:
            print("Wrong Member ID")
    except:
        print("**ERROR: Wrong Entry**")
