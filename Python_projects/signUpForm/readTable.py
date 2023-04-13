from connect import *
from time import sleep


def read():

    cursor.execute("SELECT * FROM Contacts")
    selectAll = cursor.fetchall()

    if selectAll == []:
        print("The database is empty")
        return 0

    else:
        print("\nContacts details: ")
        for query in selectAll:
            print(query)
        print("\n")
        return 1


if __name__ == "__main__":
    read()
