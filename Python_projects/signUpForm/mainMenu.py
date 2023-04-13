from connect import *
from readTable import read
from addContact import addContact
from updateContacts import update
from deleteContact import delete
from sortBy import find


def menu():
    menuID = """
        Welcome to form database 101

        Pick from the following Options:

        1. Display all name and details
        2. Add an entry
        3. Update an entry
        4. Delete an Entry
        5. Sort by
        6. Exit Program

    """

    possibleOpt = ["1", "2", "3", "4", "5", "6"]
    choice = ""

    while choice not in possibleOpt:
        print(menuID)
        choice = input("Enter a number: ")

        if choice in possibleOpt:
            return choice
        else:
            print("Your number is not valid, try again")


if __name__ == "__main__":
    program = True
    while program:
        userChoice = menu()
        if userChoice == "1":
            read()
        elif userChoice == "2":
            addContact()
        elif userChoice == "3":
            update()
        elif userChoice == "4":
            delete()
        elif userChoice == "5":
            find()
        else:
            program = False
            print("Thanks for using our services, see you next time !")
