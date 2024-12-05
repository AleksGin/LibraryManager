from commands.main_menu import (
    AddBookCommand,
    ChangeStatusCommand,
    DeleteBookCommand,
    ExitCommand,
    SearchMenuCommand,
    ShowAllBooksCommand,
)
from commands.search_menu import (
    SearchByTypeCommand,
    ToMainMenuCommand,
)
from repository.library import LibraryRepository
from services.library_service import LibraryService
from user.user import User
from utils.pharses import Phrases
from menus import Menu


class Application:
    def __init__(self) -> None:
        self.library = LibraryRepository()
        self.libary_service = LibraryService(library=self.library)
        self.user = User(library_service=self.libary_service)

    def main_menu(self):
        options = {
            "1": (
                "Добавить книгу",
                AddBookCommand(user=self.user),
            ),
            "2": (
                "Найти книгу",
                SearchMenuCommand(app=self),
            ),
            "3": (
                "Удалить книгу",
                DeleteBookCommand(user=self.user),
            ),
            "4": (
                "Изменить статус книги",
                ChangeStatusCommand(user=self.user),
            ),
            "5": (
                "Показать все книги",
                ShowAllBooksCommand(user=self.user),
            ),
            "6": (
                "Завершить работу",
                ExitCommand(),
            ),
        }

        menu = Menu(options=options)
        menu.show_menu()

    def search_menu(self):
        options = {
            "1": (
                "По автору",
                SearchByTypeCommand(
                    user=self.user,
                    search_type="author",
                    prompt=Phrases.ask_for_author,
                    allow_numeric=False,
                ),
            ),
            "2": (
                "По году",
                SearchByTypeCommand(
                    user=self.user,
                    search_type="year",
                    prompt=Phrases.ask_for_year,
                    only_numeric=True,
                ),
            ),
            "3": (
                "По названию",
                SearchByTypeCommand(
                    user=self.user,
                    search_type="title",
                    prompt=Phrases.ask_for_author,
                    allow_numeric=True,
                ),
            ),
            "4": (
                "В главное меню",
                ToMainMenuCommand(app=self),
            ),
            "5": (
                "Завершить работу",
                ExitCommand(),
            ),
        }
        menu = Menu(options=options)
        menu.show_menu()


if __name__ == "__main__":
    app = Application()
    app.main_menu()
