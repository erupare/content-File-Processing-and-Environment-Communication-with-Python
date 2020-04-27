import sqlite3
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, ElementTree

DB_NAME = "author_contracts.db"

def get_db_data():
    
    # Make connection to db called cxn
    cxn = sqlite3.connect(DB_NAME)

    # Create a cursor to db named cur
    cur = cxn.cursor()

    cur.execute("SELECT author, title, genre FROM authors")
    results = cur.fetchall()

    # close cxn, cur
    cur.close()
    cxn.close()

    return results


def create_book_entry(author, title, genre):
    # make book element
    pass
    # add author to book element
    pass
    # add title to book element
    pass
    # add genre to book element
    pass
    # add an empty isbn
    

    return book

# create root


# get info from db
book_info = get_db_data()

for book in book_info:
    # create each book entry and add to root
    pass
# write tree to file names "catalog.xml"
pass

# test code
expected_catalog = b"<?xml version='1.0' encoding='UTF-8'?>\n<catalog><book><author>Thompson, Keith</author><title>Oh Python! My Python!</title><genre>biography</genre><isbn /></book><book><author>Fritts, Larry</author><title>Fun with Django</title><genre>satire</genre><isbn /></book><book><author>Applegate, John</author><title>When Bees Attack! The Horror!</title><genre>horror</genre><isbn /></book><book><author>Brown, James</author><title>Martin Buber's Philosophies</title><genre>guide</genre><isbn /></book><book><author>Smith, Jackson</author><title>The Sun Also Orbits</title><genre>mystery</genre><isbn /></book></catalog>"

try:
    with open("catalog.xml", "rb") as f:
        catalog = f.read()
except FileNotFoundError:
    catalog = ""

assert catalog == expected_catalog
