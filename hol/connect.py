import sqlite3

DB_NAME = "author_contracts.db"

def get_database_connection():
    # Make connection to db
    cxn = sqlite3.connect(DB_NAME)

    # Create a cursor to db
    cur = cxn.cursor()

    return cxn, cur