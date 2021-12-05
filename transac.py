import book
import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
con=sqlt.connect(host="localhost", user="root", password="sristi", database="library")
cursor=con.cursor()
#function to issue books
def book_issue():
    #Exception Handling
    try:
        q="select max(issueid) from issue;"
        cursor.execute(q)
        r=cursor.fetchone()[0]
        if r:
            issueid=r+1
        else:
            issueid=1
        n=input("Enter your name:")
        qr="select * from usersdata where Name={};".format(n)
        cursor.execute(qr)
        r=cursor.fetchone()
        if r:
            pwd=input("Enter your password:")
            qr1="select * from usersdata where Password={};".format(pwd)
            cursor.execute(qr1)
            r=cursor.fetchone()
            if r:
                ud=int(input("Enter your UserID:"))
                qr2="select * from usersdata where userId={};".format(ud)
                cursor.execute(qr2)
                r=cursor.fetchone()
                if r:
                    phn=int(input("Enter your Phone number:"))
                    qr3="select * from usersdata where PhoneNo={}".format(phn)
                    cursor.execute(qr3)
                    r=cursor.fetchone()
                    if r:
                        ad=input("Enter your Address:")
                        qr4="select * from usersdata where Address={}".format(ad)
                        cursor.execute(qr4)
                        r=cursor.fetchone()
                        if r:
                            x=int(input("Enter Member ID:"))
                            q1="select * from member where memberid={};".format(x)
                            cursor.execute(q1)
                            r=cursor.fetchone()
                            if r:
                                y= int(input("Enter Book ID:"))
                                q2="select bookid, rem_copies from book where bookid={};".format(y)
                                cursor.execute(q2)
                                r=cursor.fetchone()
                                if r:
                                    if r[1]>0:
                                        qry1="select max(BooksIssued) from usersdata;"
                                        cursor.execute(qry1)
                                        r=cursor.fetchone()[0]
                                        if r:
                                            bkissued=r+1
                                        else:
                                            bkissued=1
                                        issuedate=input("Enter Issue Date:")
                                        copies=int(input("Enter the number of copies:"))
                                        remcopies=r[1]-copies
                                        q3="insert into issue values({},'{}',{},{},{});".format(issueid,issuedate,x,y,copies)
                                        cursor.execute(q3)
                                        q4="update book set rem_copies={} where bookid={};".format(remcopies,y)
                                        cursor.execute(q4)
                                        qry2="insert into usersdata values('{}','{}',{},{},'{}');".format(n,pwd,ud,phn,ad)
                                        cursor.execute(qry2)
                                        qry3="update usersdata set BooksIssued={} where Name={};".format(bkissued,n)
                                        con.commit()
                                        print("Book Issued...")
                                    else:
                                        print("Book is Not Available")
                                else:
                                    print("Wrong Book ID")
                            else:
                                print("Wrong Member ID")
                        else:
                            print("Wrong Address")
                    else:
                        print("Wrong Phone Number")
                else:
                    print("Wrong UserID")
            else:
                print("Wrong Password") 
        else:  
            print("Wrong Name Entered")
    except:
        print("**ERROR: Wrong Entry**")
    
#function to return books
def book_return():
    #Exception Handliung
    try:
        q="select max(returnid) from returns;"
        cursor.execute(q)
        r=cursor.fetchone()[0]
        if r:
            returnid=r+1
        else:
            returnid=1
        x=int(input("Enter Member ID:"))
        q1="select * from member where memberid={};".format(x)
        cursor.execute(q1)
        r=cursor.fetchone()
        if r:
            y= int(input("Enter Book ID:"))
            q2="select bookid, rem_copies from book where bookid={};".format(y)
            cursor.execute(q2)
            r=cursor.fetchone()
            if r:            
                returndate=input("Enter Return Date:")
                copies=int(input("Enter the number of copies:"))
                remcopies=r[1]+copies
                q3="insert into returns values({},'{}',{},{},{});".format(returnid,returndate,x,y,copies)
                cursor.execute(q3)
                q4="update book set rem_copies={} where bookid={};".format(remcopies,y)
                cursor.execute(q4)
                con.commit()
                print("Book Returned...")            
            else:
                print("Wrong Book ID")

        else:
            print("Wrong Member ID")
    except:
        print("**ERROR: Wrong Entry**")
