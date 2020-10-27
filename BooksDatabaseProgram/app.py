"""
This program is a database program for storing books which can be marked as read or not read for the
purpose of keeping track of what books I have and which of them I've already read.

This project was started on October 20, 2020.

As of 10/27/2020 I am still working on this project.
"""

import json
from BooksDatabaseProgram.utils import database

def menu():
    try:
        data_test = open("utils/books.txt", "r")
        data_test.close()
    except FileNotFoundError:
        data = open("utils/books.txt", "w")
        data.write("[]")
        data.close()
    finally:
        data = open("utils/books.txt", "r")
        database.books = json.load(data)
        data.close()
    while True:
        user_input = input(USER_CHOICE)
        if user_input == "q":
            quit()
        elif user_input == "a":
            database.prompt_add_book()
        elif user_input == "l":
            database.list_books()
        elif user_input == "r":
            database.prompt_read_book()
        elif user_input == "d":
            database.prompt_delete_book()
        else:
            print("\n\nPlease enter a valid option.")
            continue


USER_CHOICE = """
Enter:
- "a" to add a new book
- "l" to list all books
- "r" to mark a book as read
- "d" to delete a book
- "q" to quit

Your choice:"""

menu()