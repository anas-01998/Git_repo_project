from connect import *
from readSongs import read
from time import sleep


def delete():
    if read() == 0:
        print("There are no songs to delete")
        return

    else:
        sure = False

        while sure == False:
            songID = input("Enter the ID of the song you want to delete: ")
            confirm = input("Are you sure you want to delete this?\n (y/n):")
            if confirm == "Y" or confirm == "y" or confirm == "yes":
                sure = True

        deleteSQL = f"""
        DELETE FROM Songs WHERE SongID = "{songID}"
        """
        cursor.execute(deleteSQL)
        conn.commit()

        print(f"The song of ID {songID} has been removed")
        sleep(2)
        read()


if __name__ == "__main__":
    delete()
