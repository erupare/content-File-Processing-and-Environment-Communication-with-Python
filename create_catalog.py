import sqlite3
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, ElementTree

DB_NAME = "author_contracts.db"

def get_db_data():
    """
    write a code to execute the sql script and return the results
    """

    sql_query = """SELECT author, title, genre FROM authors"""
    
    pass # student code goes here


def create_book_entry(author, title, genre):
    """
    create the book entry as defined and return book
    """

    pass # student code goes here
    


# using the information from get_db_data()
# write code to create a root and then
# add each book to it, finally write
# data to "catalog.xml"

pass # student code goes here

# test code
expected_catalog = b"<?xml version='1.0' encoding='UTF-8'?>\n<catalog><book><author>Thompson, Keith</author><title>Oh Python! My Python!</title><genre>biography</genre><isbn /></book><book><author>Fritts, Larry</author><title>Fun with Django</title><genre>satire</genre><isbn /></book><book><author>Applegate, John</author><title>When Bees Attack! The Horror!</title><genre>horror</genre><isbn /></book><book><author>Brown, James</author><title>Martin Buber's Philosophies</title><genre>guide</genre><isbn /></book><book><author>Smith, Jackson</author><title>The Sun Also Orbits</title><genre>mystery</genre><isbn /></book></catalog>"

try:
    with open("catalog.xml", "rb") as f:
        catalog = f.read()
except FileNotFoundError:
    catalog = ""

assert catalog == expected_catalog
