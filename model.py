# Library - is a collection of books (Object)
# Book - title, author (Object)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_details(self):
        return f"{self.title} - {self.author}"
    

class Library:
    def __init__(self):
        self.books = []
    
    # Add a book
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Added {book.title} - {book.author} to library.")
    
    # Show all books
    def show_books(self):
        if len(self.books) > 0:
            print("Available Books:")
            for book in self.books:
                print(book.get_details())
        else:
            print("No books stored.")

    def edit_book(self, title, new_title, new_author):
        for i in self.books:
            if title == i.title:
                i.title = new_title
                i.author = new_author
                print("Book has been successfully edited")


    def delete_book(self, title):
        for i,j in enumerate(self.books):
            if title == j.title:
                del self.books[i]
                print("Book successfully deleted")

                