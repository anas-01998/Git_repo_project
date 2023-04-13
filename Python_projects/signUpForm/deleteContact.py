from connect import *
from readTable import read


def delete():
    program = True
    while program:

        if read() == 0:
            print("\nThere is nothing to delete")
            program = False
            return program

        else:
            contactID = input("\nselect the ID you would like to delete: ")
            confirmation = input(
                "Are you sure if you want to delete this record? (y/n): ")

            if confirmation == "n" or confirmation == "N" or confirmation == "no" or confirmation == "No" or confirmation == "NO":
                cont = input("Do you want to continue with this operation? ")

                if cont == "n" or cont == "N" or cont == "no" or cont == "No" or cont == "NO":
                    program = False
                    return program

            else:
                if confirmation == "y" or confirmation == "Y" or confirmation == "yes" or confirmation == "Yes" or confirmation == "YES":

                    sqlCode = f"""
                    DELETE FROM Contacts
                    WHERE ContactID = "{contactID}"
                    """

                    cursor.execute(sqlCode)
                    conn.commit()
                    print(
                        f"You have successfully deleted record with the Contact ID of: {contactID}")
                    program = False
                    return program


if __name__ == "__main__":
    delete()
