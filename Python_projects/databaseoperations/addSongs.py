from connect import *
from readSongs import read
from time import sleep


def insertSong():
    # insert into value
    song = []
    title = input("insert a name of a song: ")
    artist = input("enter artist's name: ")
    genre = input("Enter artist's genre: ")

    song.append(title)
    song.append(artist)
    song.append(genre)

    print(song)

    sqlCode = f"""
    INSERT INTO Songs VALUES(NULL, "{song[0]}", "{song[1]}", "{song[2]}")
    """

    cursor.execute(sqlCode)
    conn.commit()
    print(f"{title} has been successfully added to the database.")
    sleep(2.5)
    read()


if __name__ == "__main__":
    insertSong()
