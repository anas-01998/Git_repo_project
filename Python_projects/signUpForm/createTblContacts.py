from connect import *

sqlCode = """
CREATE TABLE Contacts (
    ContactID INTEGER,
    FullName TEXT,
    Address VARCHAR(50),
    Email VARCHAR(50),
    PhoneNumber INTEGER,
    PRIMARY KEY (ContactID AUTOINCREMENT)
)
"""

cursor.execute(sqlCode)
