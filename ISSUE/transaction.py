import datetime
import mysql.connector as sqlt
con = sqlt.connect(host="localhost", user="root",
                   password="1234", database="library")
cursor = con.cursor()


def no(id):
    qry = "select * from usersdata where userId='{}';".format(id)
    cursor.execute(qry)
    r = cursor.fetchone()
    if r:
        nom = r[5]


# function to issue books


def book_issue(memID, bookID):
    # Exception Handling
    try:
        q1 = "select * from usersdata where userId={};".format(memID)
        cursor.execute(q1)
        r = cursor.fetchone()
        nom = r[5]

        if nom < 4:
            nom2 = nom+1
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
                        q5 = "update usersdata set booksissued={} where userid='{}';".format(
                            nom2, memID)
                        cursor.execute(q5)
                        con.commit()

                        return "Book Issued"
                    else:
                        return "Book not available"
                else:
                    return "Wrong Book ID"

            else:
                return "Wrong UserId"
        else:
            return "Maximun limit exceed"
    except:
        return "Wrong Entry"

# function to return books


def book_return(memID, bookID):
    # Exception Handling
    try:
        q1 = "select * from usersdata where userId={};".format(memID)
        cursor.execute(q1)
        r = cursor.fetchone()
        nom = r[5]

        if nom > 0:
            nom2 = nom-1
            if r:
                q2 = "select bookId, NoOfCopiesLeft from bookstable where bookId={};".format(
                    bookID)
                cursor.execute(q2)
                r = cursor.fetchone()

                if r:
                    dt_str = str(datetime.datetime.now())
                    NoOfCopiesLeft = r[1]+1
                    q3 = "insert into issuetable(bookId,userId,DateIssued) values('{}','{}','{}');".format(
                        bookID, memID, dt_str)
                    cursor.execute(q3)
                    q4 = "update bookstable set NoOfCopiesLeft={} where bookId='{}';".format(
                        NoOfCopiesLeft, bookID)
                    cursor.execute(q4)
                    q5 = "update usersdata set booksissued={} where userid='{}';".format(
                        nom2, memID)
                    cursor.execute(q5)
                    con.commit()

                    return "Book Returned"

                else:
                    return "Wrong Book ID"

            else:
                return "Wrong UserId"
        else:
            return "You dont have any books issued"
    except:
        return "Wrong Entry"


print(book_return("779531", "224674"))
