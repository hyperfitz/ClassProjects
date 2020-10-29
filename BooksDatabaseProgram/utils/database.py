"""
This file is probably not named well; it is the data layer for this book list app.
"""

import sqlite3


def create_book_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE books(name text primary key, author text, read integer)")  # It is worth noting that you can
                                                                                            # use the "IF NOT EXISTS" command
    connection.commit()                                                                     # here and it would negate
    connection.close()                                                                      # the need for my exception
                                                                                            # hanling approach in the app.py
                                                                                            # file for checking if the database
def add_book(name, author):                                                                 # already exists. I'm not going to
    connection = sqlite3.connect("data.db")                                                 # bother; my the exception handling
    cursor = connection.cursor()                                                            # approach is working fine.

    # cursor.execute(f"""INSERT INTO books VALUES("{name}", "{author}", 0)""")
    #
    # The above commented approach lends itself to an SQL injection attack :-O ... I'm going to not do it that way.

    cursor.execute("INSERT INTO books VALUES( ?, ?, 0)", (name, author))    # This, I am told, is the safe way to do this.

    connection.commit()
    connection.close()


def prompt_add_book():        # ask for a name and author and add the book to the list
    name = input("Enter the book title: ").title()
    author = input("Enter the author: ").title()
    add_book(name, author)


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