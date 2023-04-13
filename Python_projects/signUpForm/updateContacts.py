from connect import *
from time import sleep
from readTable import read


def update():

    program = True

    while program == True:

        if read() == 0:
            print("\nThere is nothing to delete")
            program = False
            return program

        else:

            print("\nWelcome to the Update section of the database\n")
            contactID = input(
                "Enter the id of the contact you would like to update: ")
            name = input("Enter the full name you would like to update to: ")
            address = input("Enter the address you would like to update to: ")
            email = input(
                "Enter the email address you would like to update to: ")
            phoneNumber = input(
                "Enter the phone number you would like to update to: ")
            confirmation = input(
                "Are you sure you want to change this record? ")

            if confirmation == "n" or confirmation == "N" or confirmation == "no" or confirmation == "No" or confirmation == "NO":
                cont = input("Would you like to continue updating records")
                if cont == "n" or cont == "N" or cont == "no" or cont == "No" or cont == "NO":
                    program = False
                    return program

            else:
                result = []
                result.append(name)
                result.append(address)
                result.append(email)
                result.append(phoneNumber)

                sqlCode = f"""
                UPDATE Contacts
                SET FullName = "{name}", Address = "{address}", Email = "{email}", PhoneNumber = "{phoneNumber}"
                WHERE ContactID = "{contactID}"
                """

                cursor.execute(sqlCode)
                conn.commit()
                sleep(1.5)
                print(
                    f"\nYou have successfully updated contactID {contactID} to: ")
                print(result, "\n")
                program = False
                return program


if __name__ == "__main__":
    update()
