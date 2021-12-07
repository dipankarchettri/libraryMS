import mysql.connector
import pandas as pd
from tabulate import tabulate

mycon = mysql.connector.connect(
    host="localhost", user="root", password="1234", database="library")

if not mycon:
    print("Error in connecting")
mycursor = mycon.cursor()


def add_book(title, author, genre, publisher, noOfcopies):
    # Exception Handling
    try:
        mycursor.execute("insert into Bookstable(title,author,genre,publisher,noOfcopies,noofcopiesleft) values('{}','{}','{}','{}',{},{})".format(
            title, author, genre, publisher, noOfcopies, noOfcopies))
        mycon.commit()
        return True
    except:
        return False


def book_delete(bookID):
    # Exception Handling
    try:
        qry = "select * from bookstable where bookId='{}';".format(bookID)
        mycursor.execute(qry)
        r = mycursor.fetchone()
        if r:
            qry = "delete from bookstable where bookId='{}';".format(bookID)
            mycursor.execute(qry)
            mycon.commit()
            return True
        else:
            return False
    except:
        return False


def book_search(bookID):
    # Exception Handling
    try:
        qry = "select * from bookstable where bookId='{}';".format(bookID)
        mycursor.execute(qry)
        r = mycursor.fetchone()
        if r:
            qry = "select * from bookstable where bookId='{}';".format(bookID)
            df = pd.read_sql(qry, mycon)
            a = [str(r[0]), str(r[1]), str(r[2]), str(r[6])]
            # print(a)
            # print(r)
            #print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
            return a
        else:
            return "Wrong ID"
    except:
        return "Error"
