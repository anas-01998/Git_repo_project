# Connecting to a database with SQLite

import sqlite3 as sql

# connect the database

conn = sql.connect(
    r"C:\Users\Anas\OneDrive\JustIT\Python\databaseoperations\datasbase.db")


cursor = conn.cursor()  # makes it easier to execute code when you need to
# you just have to  type cursor.execute()


# CRUD Operations create, read, update and delete
