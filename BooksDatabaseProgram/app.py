"""
This program is a database program for storing books which can be marked as read or not read for the
purpose of keeping track of what books I have and which of them I've already read.

This project was started on October 20, 2020.

As of 10/22/2020 I am still working on this project.
"""

import json
from BooksDatabaseProgram.utils import database


def promptAddBook():        # ask for a name and author and add the book to the list
    name = input("Enter the book title: ").title()
    author = input("Enter the author: ").title()
    database.addBook(name, author)
    data_books = open("utils/books.txt", "w")
    json.dump(database.books, data_books)
    data_books.close()


def listBooks():            # show all books in the list
    for n in database.books:
        if n["read"] == "False":
            print(f"""Book: "{n["name"]}" written by "{n["author"]}" has not yet been read.""")
        else:
            print(f"""Book: "{n["name"]}" written by "{n["author"]}" has been read.""")

def promptReadBook():      # ask for book name and change it to "read"
    book_name = input("Enter the title you read: ").title()
    message = f"""The "{book_name}" name does not exist in the database."""
    for n in database.books:
        if book_name == n["name"]:
            n["read"] = "True"
            message = f"""The book "{book_name}" has been changed to read."""
        else:
            pass
    print(message)


# def promptDeleteBook()    # ask for book name and remove it from the list


def menu():
    try:
        data_test = open("utils/books.txt", "r")
        data_test.close()
    except FileNotFoundError:
        data = open("utils/books.txt", "w")
        data.write("[]")
        data.close()
#        data = open("books.txt", "r")
#        database.books = json.load(data)
#        data.close()
    finally:
        data = open("utils/books.txt", "r")
        database.books = json.load(data)
        data.close()
    while True:
        user_input = input(USER_CHOICE)
        if user_input == "q":
            quit()
        elif user_input == "a":
            promptAddBook()
        elif user_input == "l":
            listBooks()
        elif user_input == "r":
            promptReadBook()
        elif user_input == "d":
            continue
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