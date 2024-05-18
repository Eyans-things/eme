#abstractioners
class Book:
    def __init__(self, title, author, book_id):
        self._title = title  # Protected member
        self._author = author  # Protected member
        self.__book_id = book_id  # Private member

    # Getter methods
    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_book_id(self):
        return self.__book_id


class EnglishBook(Book):
    def __init__(self, title, author, book_id, location):
        super().__init__(title, author, book_id)
        self.location = location

    def get_book_info(self):
        print(f"Title: {self.get_title()}, Author: {self.get_author()}, ID: {self.get_book_id()}, Location: {self.location}")

#Polymorphismers
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, book_id, location):
        self.books.append(EnglishBook(title, author, book_id, location))

    def get_library_books(self):
        for book in self.books:
            book.get_book_info()

    # Additional method 1: Delete a book by ID
    def delete_book(self, book_id):
        for book in self.books:
            if book.get_book_id() == book_id:
                self.books.remove(book)
                print(f"Book with ID {book_id} deleted successfully.")
                return
        print("Book not found.")

    # Additional method 2: Borrow a book
    def borrow_book(self, book_id):
        for book in self.books:
            if book.get_book_id() == book_id:
                print(f"Book with ID {book_id} has been borrowed.")
                return
        print("Book not found.")

    # Additional method 3: Search for a book by title
    def search_book_by_title(self, title):
        found_books = [book for book in self.books if book.get_title().lower() == title.lower()]
        if found_books:
            print("Books found with title", title)
            for book in found_books:
                book.get_book_info()
        else:
            print("No books found with title", title)

    # Additional method 4: Count total books in the library
    def count_books(self):
        print("Total books in the library:", len(self.books))

    # Additional method 5: View books by a specific author
    def view_books_by_author(self, author):
        author_books = [book for book in self.books if book.get_author().lower() == author.lower()]
        if author_books:
            print("Books by author", author)
            for book in author_books:
                book.get_book_info()
        else:
            print("No books found by author", author)

    def transaction_menu(self):
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Delete a Book")
        print("4. Borrow a Book")
        print("5. Search for a Book by Title")
        print("6. Count Total Books")
        print("7. View Books by Author")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            book_id = input("Enter Book ID: ")
            location = input("Enter location/shelf: ")

            self.add_book(title, author, book_id, location)
        elif choice == "2":
            self.get_library_books()
        elif choice == "3":
            book_id = input("Enter Book ID to delete: ")
            self.delete_book(book_id)
        elif choice == "4":
            book_id = input("Enter Book ID to borrow: ")
            self.borrow_book(book_id)
        elif choice == "5":
            title = input("Enter Book Title to search: ")
            self.search_book_by_title(title)
        elif choice == "6":
            self.count_books()
        elif choice == "7":
            author = input("Enter Author Name to view books: ")
            self.view_books_by_author(author)
        elif choice == "8":
            exit()


# Main
library = Library()
while True:
    library.transaction_menu()
