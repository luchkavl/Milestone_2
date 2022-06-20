from utils import database


USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """


def menu():
    database.create_books_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Please try again!")

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input("Enter a book's name: ")
    author = input("Enter a book's author: ")

    database.add_book(name, author)


def list_books():
    books = database.list_books()

    for i, book in enumerate(books, start=1):
        name = book['name']
        author = book['author']
        read = 'Read' if book['read'] else 'Not read yet'

        print(f'{i}. {name}, {author}. {read}.')


def prompt_read_book():
    name = input("Enter a book's name you read: ")
    database.read_book(name)


def prompt_delete_book():
    name = input("Enter a book's name you want ot delete: ")
    database.delete_book(name)


menu()
