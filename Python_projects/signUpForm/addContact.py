from connect import *
from time import sleep


def addContact():
    program = True
    while program:

        dataEntered = list()

        name = input("Enter your full name: ")
        address = input("Enter your address: ")
        email = input("Enter your email: ")
        phoneNum = input("Enter your phone number: ")
        confirmation = input("Is the information correct? ")

        if confirmation == "n" or confirmation == "N" or confirmation == "no" or confirmation == "No" or confirmation == "NO":
            cont = input("Do you want to continue with this operation? ")
            if cont == "n" or cont == "N" or cont == "no" or cont == "No" or cont == "NO":
                program = False
                return program

        else:
            if confirmation == "y" or confirmation == "Y" or confirmation == "yes" or confirmation == "Yes" or confirmation == "YES":
                dataEntered.append(name)
                dataEntered.append(address)
                dataEntered.append(email)
                dataEntered.append(phoneNum)

                sqlCode = f"INSERT INTO Contacts VALUES (NULL, '{name}', '{address}', '{email}', '{phoneNum}')"

                cursor.execute(sqlCode)
                conn.commit()
                sleep(1.5)
                print(
                    f"\nYou have successfully added:")
                print(dataEntered)
                program = False
                return program


if __name__ == "__main__":
    addContact()
