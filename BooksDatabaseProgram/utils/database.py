"""
For storing and retrieving books.
"""

books = []

def addBook(name, author):
    books.append({"name": name, "author": author, "read": "False"})