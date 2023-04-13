from connect import *
from time import sleep


def find():
    listFormat = ("ContactID", "FullName",
                  "Address", "Email", "PhoneNumber")
    print("The list format is ", listFormat, "\n")
    sleep(1.5)

    columnName = input("What column would you like to sort by? ")
    showRecord = input("What criteria would you like to show by? ")

    try:
        cursor.execute(f"""SELECT * FROM Contacts
        WHERE {columnName} = "{showRecord}" 
        """)

        query = cursor.fetchall()

        if query == []:
            print("Database is empty")

        else:
            sleep(1.5)
            for film in query:
                print(film)
    except:
        print("Either the column or criteria is invalid")


if __name__ == "__main__":
    find()
