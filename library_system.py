# library_system.py

class Book:
    def __init__(self, isbn, title, author, quantity):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.quantity = quantity


class Member:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


class Borrowing:
    def __init__(self, id, isbn, member_id, borrow_date, return_date=None):
        self.id = id
        self.isbn = isbn
        self.member_id = member_id
        self.borrow_date = borrow_date
        self.return_date = return_date


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowings = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def borrow_book(self, isbn, member_id):
        for book in self.books:
            if book.isbn == isbn:
                if book.quantity > 0:
                    book.quantity -= 1
                    print("Book borrowed successfully")
                    return
                else:
                    print("Book is out of stock")
                    return
        print("Book not found")


def main():
    lib = Library()

    while True:
        print("\n1. Add book")
        print("2. Borrow book")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            isbn = input("ISBN: ")
            title = input("Title: ")
            author = input("Author: ")
            quantity = int(input("Quantity: "))
            book = Book(isbn, title, author, quantity)
            lib.add_book(book)

        elif choice == "2":
            isbn = input("ISBN: ")
            member_id = input("Member ID: ")
            lib.borrow_book(isbn, member_id)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
