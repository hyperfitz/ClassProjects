"""
For storing and retrieving books.
"""

import json

books = []

def add_book(name, author):
    books.append({"name": name, "author": author, "read": "False"})

def prompt_add_book():        # ask for a name and author and add the book to the list
    name = input("Enter the book title: ").title()
    author = input("Enter the author: ").title()
    add_book(name, author)
    with open("utils/books.txt", "w") as data_books:
        json.dump(books, data_books)


def list_books():            # show all books in the list
    for n in books:
        if n["read"] == "False":
            print(f"""Book: "{n["name"]}" written by "{n["author"]}" has not yet been read.""")
        else:
            print(f"""Book: "{n["name"]}" written by "{n["author"]}" has been read.""")


def prompt_read_book():      # ask for book name and change it to "read"
    book_name = input("Enter the title you read: ").title()
    message = f"""The "{book_name}" name does not exist in the database."""
    for n in books:
        if book_name == n["name"]:
            n["read"] = "True"
            message = f"""The book "{book_name}" has been changed to read."""
        else:
            pass
    with open("utils/books.txt", "w") as data_books:
        json.dump(books, data_books)
    print(message)


def prompt_delete_book():    # ask for book name and remove it from the list
    global books
    user_input = input("Enter book title to remove from the list: ").title()
    books = [book for book in books if book["name"] != user_input]
    with open("utils/books.txt", "w") as data_books:
        json.dump(books, data_books)