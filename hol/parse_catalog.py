import sqlite3
import sys
import defusedxml.ElementTree as ET

def update_db(isbn_data_list):
    # Make connection to db called cxn
    cxn = sqlite3.connect("author_contracts.db")

    # Create a cursor to db named cur
    cur = cxn.cursor()
    
    sql_query = ''' ALTER TABLE authors ADD COLUMN isbn CHAR(20); '''

    # Send sql query to request
    cur.execute(sql_query)
    cxn.commit()

    sql_query = "UPDATE authors SET isbn = ? WHERE title = ?;"
    cur.executemany(sql_query, isbn_data_list)
    cxn.commit()

    sql_query = ''' SELECT isbn FROM authors;'''
    cur.execute(sql_query)
    results = cur.fetchall()

    #closing database connection.
    cur.close()
    cxn.close()  

    expected_results = [('000-1-000000-00-1',), ('000-2-000000-00-2',), ('000-3-000000-00-3',), ('000-4-000000-00-4',), ('000-5-000000-00-5',)]

    assert results == expected_results

file_name = "isbn.xml"

try:
    # parse file
    pass
except:
    print(f"File not found: {file_name}")
    sys.exit(1)

isbn_data_list = []
# loop through "book" in file and append isbn and title as a list object to isbn_data_list


# update db and test for accuracy
update_db(isbn_data_list)
