from readSongs import read
from addSongs import insertSong
from updateSong import update
from deleteSongs import delete


def menu():
    menuUI = """
    Welcome to Music Database

    Please select one of the following options below:
    1. Display songs in a database
    2. Add a new song to the database
    3. Update an existing song
    4. Delete a song
    5. Exit and application
    """

    options = ["1", "2", "3", "4", "5"]
    choice = ""

    while choice not in options:
        print(menuUI)
        choice = input("Enter a choice: ")
        if choice not in options:
            print(choice, "is not a valid choice")
        return choice


if __name__ == "__main__":
    mainProgram = True
    while mainProgram:
        userChoice = menu()
        if userChoice == "1":
            read()
        elif userChoice == "2":
            insertSong()
        elif userChoice == "3":
            update()
        elif userChoice == "4":
            delete()
        else:
            mainProgram = False
    print("Thanks for using this application")
    input("Press enter to exit...")
