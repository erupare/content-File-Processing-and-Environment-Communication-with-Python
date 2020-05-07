import io

def copy_book(input, output):
    """
    write the input to the output
    """

    pass # student code here


if __name__ == "__main__":

    # author's novel is stored in file `book.txt`
    # create a copy of the book for the editing department
    # append _text to the end of the name of the copy
    # student input needed, please use book_input and book_copy
    # as the handles to the files
    pass # student code needed here


    # send to function `copy_book(input, output)`
    # make sure the cursor is at the start of each file
    pass # student code needed here

    # to test return each file to the head of the file
    pass # student code needed here

    # test file exists
    try:
        f = open("book_edit.txt", "r+b")
    except FileNotFoundError:
        print("book_edit.txt does not exist")
    finally:
        f.close()
    
    # test file contents are the same
    assert book_input.read() == book_copy.read()


    # write book to a BytesIO object using function copy_book
    # make sure the cursor is at the start of each file (memory file also)
    # send to copy function
    pass  # student code needed here
    

    # to test return each file to the head of the file
    pass # student input needed
    
    # test file exists
    if not book_stream.readable():
        print("book_stream does not exist")
        exit(1)

    # test
    assert book_input.read() == book_stream.getvalue()

    # close all open files
    pass # student input needed

    # test
    assert book_input.closed == True
    assert book_copy.closed == True
    assert book_stream.closed == True


