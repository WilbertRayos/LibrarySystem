class Controller:
    def __init__(self, view, library):
        self.view = view
        self.library = library

    def menu(self):
        while True:
            try:
                choice = int(self.view.menu())
                options = {
                    1:self.add_book,
                    2:self.show_books,
                    3:self.edit_book,
                    4:self.delete_book,
                }
                if choice in options:
                    options[choice]()
            except ValueError:
                print("Invalid Input")

    def add_book(self):
        title, author = self.view.add_book()
        self.library.add_book(title, author)
    
    def show_books(self):
        self.library.show_books()
    
    def edit_book(self):
        title, new_title, new_author = self.view.edit_book()
        self.library.edit_book(title, new_title, new_author)
        
    def delete_book(self):
        title = self.view.delete_book()
        self.library.delete_book(title)