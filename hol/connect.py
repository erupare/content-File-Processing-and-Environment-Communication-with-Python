import sqlite3

DB_NAME = "author_contracts.db"

def get_database_connection():

    # Make connection to db called cxn
    cxn = sqlite3.connect(DB_NAME)

    # Create a cursor to db named cur
    cur = cxn.cursor()

    # return them both
    return cxn, cur

