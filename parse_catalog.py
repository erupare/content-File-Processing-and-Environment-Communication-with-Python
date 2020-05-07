import sqlite3
import sys
import defusedxml.ElementTree as ET

def update_db(isbn_data_list):
    """ 
    add code to execute each sql_stmt in the order given
    results from sql_query_3 should be assigned to results
    """
    
    sql_query_1 = ''' ALTER TABLE authors ADD COLUMN isbn CHAR(20); '''

    sql_query_2 = "UPDATE authors SET isbn = ? WHERE title = ?;"

    sql_query_3 = ''' SELECT isbn FROM authors;'''

    pass # student code goes here


    # test code
    expected_results = [('000-1-000000-00-1',), ('000-2-000000-00-2',), ('000-3-000000-00-3',), ('000-4-000000-00-4',), ('000-5-000000-00-5',)]

    assert results == expected_results

# using 'isbn.xml'
# loop through "book" in file and append isbn and title as a list object to isbn_data_list
# send isbn_data_list to function update_db

pass # student code goes here
