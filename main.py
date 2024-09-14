from model import Library, Book
from view import View
from controller import Controller

library = Library()
view = View()
controller = Controller(view, library)


if __name__ == "__main__":
    controller.menu()