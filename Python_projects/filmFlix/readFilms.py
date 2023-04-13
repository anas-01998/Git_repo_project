from connect import *
from time import sleep


def readFilm():
    cursor.execute("SELECT * FROM tblFilms")
    query = cursor.fetchall()

    if query == []:
        print("Your Database is empty")

    else:
        print("\nThese are the films in the Database:")
        for film in query:
            print(film)


if __name__ == "__main__":
    readFilm()
