import sqlite3
from connect import get_database_connection

DB_NAME = "author_contracts.db"

def add_column_to_db():
    """
    Delete selected data from database.
    """
    
    sql_query = ''' ALTER TABLE authors ADD COLUMN genre CHAR(15); '''
    
    # make connection to db

    # send sql query to request

    # close database connection.   

def test_add_column_to_db():
    sql_query = ''' SELECT sql FROM sqlite_master WHERE name='authors'; '''
    
    # make connection to db
    cxn = sqlite3.connect(DB_NAME)

    # create a cursor to db
    cur = cxn.cursor()
        
    # send sql query to request
    cur.execute(sql_query)
    results = cur.fetchall()
    
    assert "genre CHAR(15)" in results[0][0], "column was not added properly"

    # close database connection.
    cur.close()
    cxn.close()  

def add_data_to_column():

    sql_stmt = ''' UPDATE authors SET genre = ? WHERE title = ? '''

    genre_data = [
        ["genre", "title"],
        ["biography", "Oh Python! My Python!"],
        ["satire", "Fun with Django"],
        ["horror", "When Bees Attack! The Horror!"],
        ["guide", "Martin Buber's Philosophies"],
        ["mystery", "The Sun Also Orbits"]
    ]
    
    # get connection and cursor to db
    
    # send sql query to request
    # remove header row from contract_list


    # use executemany to load data


    # close database connection.
    cur.close()
    cxn.close() 

def test_add_data_to_column():
    sql_query = ''' SELECT genre FROM authors; '''
    
    # make connection to db
    cxn = sqlite3.connect(DB_NAME)

    # create a cursor to db
    cur = cxn.cursor()
        
    # send sql query to request
    cur.execute(sql_query)
    results = cur.fetchall()

    expected = [('biography',), ('satire',), ('horror',), ('guide',), ('mystery',)]
    assert results == expected, "genre did not populate correctly"

    # close database connection.
    cur.close()
    cxn.close()  

def main():
    add_column_to_db()
    test_add_column_to_db()
    add_data_to_column()
    test_add_data_to_column()


           
if __name__ == "__main__":
    main()