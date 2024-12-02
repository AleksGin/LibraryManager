from library import Library
from services import LibraryService
from utils.pharses import MainMenu


class User:
    def __init__(self, library_service: LibraryService) -> None:
        self.library_service = library_service

    def add_book(self):
        author = input("Введите название автора: ")
        message = self.library_service.add_book(author=author)
        print(message)


def main_menu():
    library = Library()
    library_service = LibraryService(library=library)
    user = User(library_service=library_service)

    while True:
        print(MainMenu.menu_text)
        command = input("> ")

        if command == "1":
            user.add_book()


if __name__ == "__main__":
    main_menu()
