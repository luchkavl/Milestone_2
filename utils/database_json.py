"""
Storing and retrieving data about books using JSON
"""
import sqlite3

FILE_NAME = 'books.json'


def create_json_if_need():
    con = sqlite3.connect('data.db')
    cur = con.cursor()

    cur.execute("create table books(name text primary key, author text, read integer)")

    con.commit()
    con.close()

    #try:
        #with open(FILE_NAME, 'r'):
           # pass
   # except FileNotFoundError:
       # with open(FILE_NAME, 'w') as file:
           # json.dump([], file)


def read_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)


def write_json(file_name, content):
    with open(file_name, 'w') as file:
        json.dump(content, file)


def add_book(name, author):
    content = read_json(FILE_NAME)

    book = {'name': name, 'author': author, 'read': False}
    content.append(book)

    write_json(FILE_NAME, content)


def list_books():
    content = read_json(FILE_NAME)
    return content


def read_book(name):
    content = read_json(FILE_NAME)

    for book in content:
        if book['name'] == name:
            book['read'] = True

    write_json(FILE_NAME, content)


def delete_book(name):
    content = read_json(FILE_NAME)

    iter_books = [book for book in content if book['name'] != name]

    if iter_books != content:
        content = iter_books

    write_json(FILE_NAME, content)
