"""
This program is a database program for storing books which can be marked as read or not read for the
purpose of keeping track of what books I have and which of them I've already read.

This project was started on October 20, 2020.

As of 10/20/2020 I am still working on this project. (That is a silly thing to say at the moment.) :-)
"""

from BooksDatabaseProgram.utils import database

USER_CHOICE = """
Enter:
- "a" to add a new book
- "l" to list all books
- "r" to mark a book as read
- "d" to delete a book
- "q" to quit

Your choice:"""

def menu():
    while True:
        user_input = input(USER_CHOICE)
        if user_input == "q":
            quit()
        if user_input == "a":
            continue
        elif user_input == "l":
            continue
        elif user_input == "r":
            continue
        elif user_input == "d":
            continue
        else:
            print("""
            
            Please enter a valid option.
            """)
            continue

# def promptAddBook() ask for a name and author and add the book to the list
# def listBooks() show all books in the list
# def promptReadBook() ask for book name and change it to "read"
# def promptDeleteBook() ask for book name and remove it from the list

menu()