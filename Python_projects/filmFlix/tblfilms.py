from connect import *


createTable = """
CREATE TABLE tblFilms (
    filmID INTEGER,
    title TEXT,
    yearReleased INTEGER,
    rating TEXT,
    duration INTEGER,
    Genre TEXT,
    PRIMARY KEY ("filmID" AUTOINCREMENT)
)
"""

cursor.execute(createTable)
