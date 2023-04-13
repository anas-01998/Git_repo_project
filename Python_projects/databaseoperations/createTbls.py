# you need to connect to the page called connect and import

from connect import *

tableGen = """
CREATE TABLE Songs (
    "SongID" INTEGER NOT NULL UNIQUE,
    "Title" TEXT,
    "Artist" TEXT,
    "Genre" TEXT,
    PRIMARY KEY("SongID" AUTOINCREMENT)
)

"""

cursor.execute(tableGen)
