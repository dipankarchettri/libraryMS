import datetime
import mysql.connector as sqlt
con = sqlt.connect(host="localhost", user="root",
                   password="1234", database="library")
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
                    return "Book Issued"
                else:
                    return "Book not available"
            else:
                return "Wrong Book ID"

        else:
            return "Wrong UserId"
    except:
        return "Wrong Entry"

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
                return "Book Returned..."
            else:
                return "Wrong Book ID"

        else:
            return "Wrong Member ID"
    except:
        return "**ERROR: Wrong Entry**"
