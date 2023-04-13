from connect import *
from readFilms import readFilm
from addFilm import addFilm
from deleteFilm import deleteFilm
from updateFilms import updateFilm
from time import sleep
from sortBy import find


def startProgram():
    options = ("""

    Welcome to Films Database, please choose from the following options

    1. Display films database
    2. Add a film 
    3. Delete a film 
    4. Update a film
    5. Sort by a certain column and field
    6. Exit program
    """)

    possibleChoices = ["1", "2", "3", "4", "5", "6"]
    userChoice = ""

    while userChoice not in possibleChoices:
        print(options)
        userChoice = input("Enter a choice: \n")
        if userChoice not in possibleChoices:
            print("The option you have chosen is not valid")
        return userChoice


if __name__ == "__main__":
    program = True
    while program:
        choice = startProgram()
        if choice == "1":
            sleep(2.5)
            readFilm()
        elif choice == "2":
            addFilm()
        elif choice == "3":
            deleteFilm()
        elif choice == "4":
            updateFilm()
        elif choice == "5":
            find()
        else:
            program = False
    print("Thank you for using the Film flix Database, Goodbye!!")
