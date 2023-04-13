from connect import *
from time import sleep


def read():
    cursor.execute("SELECT * FROM songs")
    query = cursor.fetchall()

    if query == []:
        sleep(2.5)
        print("Database is empty.")
        return 0
    else:
        print("\nSongs List:")
        for record in query:
            print(record)
        return 1


if __name__ == "__main__":
    read()                      # way to not execute if file is imported as a module
