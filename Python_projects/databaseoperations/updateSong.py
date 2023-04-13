from connect import *
from readSongs import read
from time import sleep


def update():
    if read() == 0:
        print("There is nothing to update")
        return

    else:
        sleep(2.5)
        songID = input("Enter the id of the song you would like to update: ")

        title = input("Enter the new title: ")
        artist = input("Enter the new artist: ")
        genre = input("Enter the new genre: ")

        updateSQL = f"""
        UPDATE Songs
        SET Title = "{title}", Artist = "{artist}", Genre = "{genre}"
        WHERE SongID = {songID};
        """

        cursor.execute(updateSQL)  # executes the action
        conn.commit()  # commits the change
        print(f"Song ID: {songID} has been updated")
        sleep(2.5)  # delay before the data is read
        read()


if __name__ == "__main__":
    update()
