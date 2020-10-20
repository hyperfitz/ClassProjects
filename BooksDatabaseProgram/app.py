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
    userInput = input(USER_CHOICE)
    while userInput != "q":
        pass

# def promptAddBook() ask for a name and author and add the book to the list
# def listBooks() show all books in the list
# def promptReadBook() ask for book name and change it to "read"
# def promptDeleteBook() ask for book name and remove it from the list