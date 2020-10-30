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
    try:
        cursor.execute("INSERT INTO books VALUES( ?, ?, 0)", (name, author))    # This, I am instructed, is the safe way to do this.
    except sqlite3.IntegrityError:
        print(f"""The book "{name}" already exists in this list.""")
    connection.commit()
    connection.close()


def prompt_add_book():        # ask for a name and author and add the book to the list
    name = input("Enter the book title: ").title()
    author = input("Enter the author: ").title()
    add_book(name, author)


def list_books():            # show all books in the list
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")

    books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]
    connection.close()

    for book in books:
        if book["read"] == False:
            print(f"""Book: "{book["name"]}" written by "{book["author"]}" has not yet been read.""")
        else:
            print(f"""Book: "{book["name"]}" written by "{book["author"]}" has been read.""")


def prompt_read_book():      # ask for book name and change it to "read"
    book_name = input("Enter the title you read: ").title()
    message = f"""The book "{book_name}" name does not exist in the database."""

    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE books SET read = 1 WHERE name = ?", (book_name,))
    cursor.execute("SELECT * FROM books")
    books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]
    for book in books:
        if book_name == book["name"]:
            message = f"""The book "{book_name}" has been changed to read."""
        else:
            pass

    connection.commit()
    connection.close()
    print(message)

def prompt_delete_book():    # ask for book name and remove it from the list
    book_name = input("Enter the title you want to delete: ").title()
    message = f"""The book "{book_name}" name does not exist in the database."""

    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")
    books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]
    for book in books:
        if book_name == book["name"]:
            message = f"""The book "{book_name}" has been deleted from the list."""
        else:
            pass
    cursor.execute("DELETE FROM books WHERE name = ?", (book_name,))

    connection.commit()
    connection.close()
    print(message)