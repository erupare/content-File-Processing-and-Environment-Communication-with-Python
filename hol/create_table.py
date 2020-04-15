# create_table.py

import sqlite3
from connect import get_database_connection

DB_NAME = "author_contracts.db"

contract_list = [
    ["author", "title", "pages", "due date"],
    ["Thompson, Keith", "Oh Python! My Python!", 1200, "2029-11-15"],
    ["Fritts, Larry", "Fun with Django", 150, "2021-06-23"],
    ["Applegate, John", "When Bees Attack! The Horror!", 550, "2020-12-10"],
    ["Brown, James", "Martin Buber's Philosophies", 700, "0221-07-12"],
    ["Smith, Jackson", "The Sun Also Orbits", 400, "2020-10-31"],
    ["Smith, Jackson", "The Sun Also Orbits", 600, "2029-10-31"]
]
  

def create_table():
    """
    Create a table populated with the given data.
    """
    
    create_table = """ CREATE TABLE authors(
        ID          INTEGER PRIMARY KEY     AUTOINCREMENT,
        author      TEXT                NOT NULL,
        title       TEXT                NOT NULL,
        pages       INTEGER             NOT NULL,
        due_date    CHAR(15)            NOT NULL
    )   
    """
    
    # get connection and cursor to db

    
    # send sql query to request
    
        
    # close database connection.


        
def test_table_created():
    """ 
    Test table was created.
    """
    
    test_stmt = ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='authors'; '''
    
    # get connection and cursor to db
    cxn, cur = get_database_connection()
        
    # send sql query to request
    cur.execute(test_stmt)
    cxn.commit()
    
    assert cur.fetchone()[0] == 1, 'table does not exist.'

    # close database connection.
    cur.close()
    cxn.close()
           
def populate_table():

    add_data_stmt = ''' INSERT INTO authors(author,title,pages,due_date) VALUES(?,?,?,?); '''
    
    # get connection and cursor to db
    
    # send sql query to request
    # remove header row from contract_list


    # use executemany to load data

    # close database connection.


def test_populate_table():
    # Get connection and cursor to db
    cxn, cur = get_database_connection()
    cur.execute("select * from authors;")
    results = cur.fetchall()

    assert len(results) == 6, 'The table does not have six rows.'

def main():
    create_table()
    test_table_created()
    populate_table()
    test_populate_table()
           
if __name__ == "__main__":
    main()