from connect import *
from time import sleep
from readFilms import readFilm


def updateFilm():
    readFilm()
    filmList = []

    filmID = input("\nWhat is the ID of the Film you want to update? ")

    filmName = input("What is the name of the film you want to update to? ")
    filmYear = input("What year was it made in? ")
    filmRating = input("What was the rating for this film? ")
    filmDur = input("what was the duration of the film in Minutes? ")
    Genre = input("What was the genre of this film? ")

    filmList.append(filmName)
    filmList.append(filmYear)
    filmList.append(filmRating)
    filmList.append(filmDur)
    filmList.append(Genre)

    sqlCode = f"""
    UPDATE tblFilms
    SET title= "{filmName}", yearReleased= "{filmYear}", rating="{filmRating}", duration="{filmDur}", Genre="{Genre}"
    WHERE filmID = "{filmID}"
    """

    cursor.execute(sqlCode)
    conn.commit()
    sleep(2.5)
    print(f"You have updated your film record to {filmList}")


if __name__ == "__main__":
    updateFilm()
