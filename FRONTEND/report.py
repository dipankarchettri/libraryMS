import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
con = sqlt.connect(host="localhost", user="root",
                   password="1234", database="library")
cursor = con.cursor()


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
