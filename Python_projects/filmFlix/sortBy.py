from connect import *
from time import sleep


def find():

    listFormat = ("filmID", "title",
                  "yearReleased", "rating", "duration", "Genre")
    print("The list format is ", listFormat, "\n")
    sleep(1.5)

    try:
        columnName = input("What column would you like to sort by? ")
        showRecord = input("What criteria would you like to show by? ")

        cursor.execute(f"""SELECT * FROM tblFilms
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
        print("Either the column name or criteria is incorrect please try again.")


if __name__ == "__main__":
    find()
