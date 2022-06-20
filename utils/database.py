"""
Storing and retrieving data about books from SQLite3
"""

from utils.db_connection import DatabaseConnection
from sqlite3 import IntegrityError
from typing import Dict, List


Book = Dict[str, str, int]


def create_books_table() -> None:
    with DatabaseConnection() as con:
        cur = con.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")


def add_book(name: str, author: str) -> None:
    with DatabaseConnection() as con:
        cur = con.cursor()

        try:
            cur.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
        except IntegrityError:
            print("The book is already exists!")


def list_books() -> List[Book]:
    with DatabaseConnection() as con:
        cur = con.cursor()

        cur.execute('SELECT * FROM books')
        books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cur.fetchall()]

    return books


def read_book(name: str) -> None:
    with DatabaseConnection() as con:
        cur = con.cursor()

        cur.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))


def delete_book(name: str) -> None:
    with DatabaseConnection() as con:
        cur = con.cursor()

        cur.execute('DELETE FROM books WHERE name = ?', (name,))
