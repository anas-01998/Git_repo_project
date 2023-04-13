from connect import *
from time import sleep
from readFilms import readFilm


def addFilm():
    filmRecord = []

    filmName = input("What is the name of the film you want to add? ")
    filmYear = input("What year was it made in? ")
    filmRating = input("What was the rating for this film? ")
    filmDur = input("what was the duration of the film in Minutes? ")
    Genre = input("What was the genre of this film? ")

    filmRecord.append(filmName)
    filmRecord.append(filmYear)
    filmRecord.append(filmRating)
    filmRecord.append(filmDur)
    filmRecord.append(Genre)

    sqlCode = f"""
    INSERT INTO tblFilms VALUES (NULL, "{filmName}", "{filmYear}", "{filmRating}", "{filmDur}", "{Genre}");
    """

    cursor.execute(sqlCode)
    conn.commit()
    sleep(2.5)
    print(f"\nYou have added {filmRecord} in the Database")
    readFilm()


if __name__ == "__main__":
    addFilm()
