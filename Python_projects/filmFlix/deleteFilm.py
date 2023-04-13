from connect import *
from time import sleep
from readFilms import readFilm


def deleteFilm():
    readFilm()
    sleep(1.5)
    answer = True

    while answer:
        filmID = input("\nEnter the ID of the film you want to Delete: ")
        confirmation = input("\nAre you sure you want to delete this film?")

        if confirmation == "y" or "Y" or "yes" or "Yes" or "YES":
            sqlCode = f"""DELETE FROM tblFilms
            WHERE filmID= "{filmID}"
            """

            cursor.execute(sqlCode)
            conn.commit()
            sleep(2.5)
            print("You have successfully deleted the film")
            answer = False

        return answer


if __name__ == "__main__":
    deleteFilm()
