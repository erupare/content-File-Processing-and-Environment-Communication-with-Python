import sqlite3

DB_NAME = "author_contracts.db"

def add_column_to_db():
    """
    Delete selected data from database.
    """
    
    sql_query = ''' ALTER TABLE authors ADD COLUMN genre CHAR(15); '''
    
     # Make connection to db
    cxn = sqlite3.connect(DB_NAME)

    # Create a cursor to db
    cur = cxn.cursor()

    # Send sql query to request
    cur.execute(sql_query)
    cxn.commit()

    #closing database connection.
    if(cxn):
        cur.close()
        cxn.close()    

def test_add_column_to_db():
    sql_query = ''' SELECT sql FROM sqlite_master WHERE name='authors'; '''
    
     # Make connection to db
    cxn = sqlite3.connect(DB_NAME)

    # Create a cursor to db
    cur = cxn.cursor()
        
    # Send sql query to request
    cur.execute(sql_query)
    results = cur.fetchall()
    
    assert "genre CHAR(15)" in results[0][0], "column was not added properly"

    #closing database connection.
    if(cxn):
        cur.close()
        cxn.close()  

def add_data_to_column():

    genre_data = [
        ["title", "genre"],
        ["Oh Python! My Python!", "biography"],
        ["Fun with Django", "satire"],
        ["When Bees Attack! The Horror!", "horror"],
        ["Martin Buber's Philosophies", "guide"],
        ["The Sun Also Orbits", "mystery"]
    ]
    
     # Make connection to db
    cxn = sqlite3.connect(DB_NAME)

    # Create a cursor to db
    cur = cxn.cursor()

    # Send sql query to request
    for row in genre_data:
        if row[0]=='title':
            next
        else:
            print(f"{row[0]}")
            cur.execute(f"UPDATE authors SET genre = \"{row[1]}\" WHERE title = \"{row[0]}\";")
    cxn.commit()


    #closing database connection.
    if(cxn):
        cur.close()
        cxn.close() 

def test_add_data_to_column():
    sql_query = ''' SELECT genre FROM authors; '''
    
     # Make connection to db
    cxn = sqlite3.connect(DB_NAME)

    # Create a cursor to db
    cur = cxn.cursor()
        
    # Send sql query to request
    cur.execute(sql_query)
    results = cur.fetchall()

    expected = [('biography',), ('satire',), ('horror',), ('guide',), ('mystery',)]
    assert results == expected, "genre did not populate correctly"

    #closing database connection.
    if(cxn):
        cur.close()
        cxn.close()  

def main():
    add_column_to_db()
    test_add_column_to_db()
    add_data_to_column()
    test_add_data_to_column()


           
if __name__ == "__main__":
    main()