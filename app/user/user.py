from library import Library
from services import LibraryService
from utils.handlers import InputHandler
from utils.pharses import (
    MainMenu,
    Phrases,
    SearchSelectionMenu,
)


class User:
    def __init__(self, library_service: LibraryService) -> None:
        self.library_service = library_service

    def add_book_command(self) -> None:
        validated_details = InputHandler.get_book_details()
        self.library_service.add_book(details=validated_details)

    def delete_book_command(self) -> None:
        validated_id = InputHandler.validate_book_details(
            text=Phrases.ask_book_id, only_numeric=True
        )
        self.library_service.delete_book(book_id=validated_id)

    def search_type_author_commmand(
        self,
        search_type: str,
        prompt: str,
        numeric_only: bool = False,
        allow_numeric: bool = False,
    ) -> None:
        validated_value = InputHandler.validate_book_details(
            text=prompt,
            only_numeric=numeric_only,
            allow_numeric=allow_numeric,
        )
        self.library_service.get_books_by_search_type(
            search_type=search_type,
            value=validated_value,
        )

    def change_status_command(
        self,
    ) -> None:
        validated_id = InputHandler.validate_book_details(
            text=Phrases.ask_book_id,
            only_numeric=True,
        )
        correct_status = InputHandler.check_for_correct_status()
        self.library_service.set_new_status_by_id(
            book_id=validated_id,
            status=correct_status,
        )

    def show_all_books_command(self):
        self.library_service.get_all_books()


def main_menu():
    library = Library()
    library_service = LibraryService(library=library)
    user = User(library_service=library_service)

    while True:
        print(MainMenu.menu_text)
        command = input("> ")

        if command == "1":
            user.add_book_command()
        if command == "2":
            search_menu()
        if command == "3":
            user.delete_book_command()
        if command == "4":
            user.change_status_command()
        if command == "5":
            user.show_all_books_command()


def search_menu():
    library = Library()
    library_service = LibraryService(library=library)
    user = User(library_service=library_service)

    while True:
        print(SearchSelectionMenu.selection_text)
        command = input("> ")

        if command == "1":
            user.search_type_author_commmand(
                search_type="author",
                prompt=Phrases.ask_for_author,
            )
        if command == "2":
            user.search_type_author_commmand(
                search_type="year",
                prompt=Phrases.ask_for_year,
                numeric_only=True,
            )
        if command == "3":
            user.search_type_author_commmand(
                search_type="title",
                prompt=Phrases.ask_for_title,
                allow_numeric=True,
            )
        if command == "4":
            main_menu()


if __name__ == "__main__":
    main_menu()
