import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
con = sqlt.connect(host="localhost", user="root",
                   password="1234", database="library")
cursor = con.cursor()

# function to display book details


def book_output():
    df = pd.read_sql("select * from bookstable", con)
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

# function to display member details


def member_output():
    df = pd.read_sql("select * from usersdata", con)
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

# function to display issue details


def issue_output():
    df = pd.read_sql("select * from issuetable", con)
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

# function to display return details


def return_output():
    df = pd.read_sql("select * from returntable", con)
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

# function to show the chart


def col_chart():
    q = "select bookId,count(no_of_copies) as totalcopies from issuetable group by bookId;"
    df = pd.read_sql(q, con)
    # print(df)
    plt.bar(df.bookId, df.totalcopies)
    plt.xlabel("Book ID")
    plt.ylabel("Copies Issued")
    plt.title("Best Reading Book")
    plt.xticks(df.bookId)
    plt.show()
