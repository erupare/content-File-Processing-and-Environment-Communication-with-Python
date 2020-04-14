import sqlite3

DB_NAME = "author_contracts.db"

def delete_data_from_db():
    """
    Delete selected data from database.
    """
    
    sql_query = ''' DELETE FROM authors WHERE (author="Smith, Jackson" AND pages=400); '''
    
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

def test_delete_data():
    sql_query = ''' SELECT count(author) FROM authors WHERE author="Smith, Jackson"; '''
    
     # Make connection to db
    cxn = sqlite3.connect(DB_NAME)

    # Create a cursor to db
    cur = cxn.cursor()
        
    # Send sql query to request
    cur.execute(sql_query)
    results = cur.fetchall()

    assert results[0][0] == 1, "the number of Smith Jackson rows is incorrect"

    #closing database connection.
    if(cxn):
        cur.close()
        cxn.close()  

def update_data():
    sql_query = ''' UPDATE authors SET due_date="2020-10-31" WHERE author="Smith, Jackson"; '''
    
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

def test_update_data():
    sql_query = ''' SELECT due_date FROM authors WHERE author="Smith, Jackson"; '''
    
     # Make connection to db
    cxn = sqlite3.connect(DB_NAME)

    # Create a cursor to db
    cur = cxn.cursor()
        
    # Send sql query to request
    cur.execute(sql_query)
    results = cur.fetchall()

    assert results[0][0] == "2020-10-31", "due date not updated correctly"

    #closing database connection.
    if(cxn):
        cur.close()
        cxn.close()  

def main():
    delete_data_from_db()
    test_delete_data()
    update_data()
    test_update_data()


           
if __name__ == "__main__":
    main()