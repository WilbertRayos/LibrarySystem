class View:
    def __init__(self):
        pass

    def menu(self):
        print("*"*10)
        print("1. Add Book")
        print("2. Show Books")
        print("3. Edit Book Information")
        print("4. Delete Book")

        choice = input("Enter the number: ")

        return choice
    
    def add_book(self):
        print("*"*10)
        print("ADD BOOK")
        
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")

        return [title, author]
    

    def edit_book(self):
        title = input("Enter book title to edit: ")
        new_title = input("Enter new title: ")
        new_author = input("Enter new author: ")

        return [title, new_title, new_author]

    def delete_book(self):
        title = input("Enter book title to delete: ")

        return title