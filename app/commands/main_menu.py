from abc import ABC, abstractmethod
from utils.pharses import Phrases


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class AddBookCommand(Command):
    def __init__(self, user) -> None:
        self.user = user

    def execute(self) -> None:
        self.user.add_book_command()


class DeleteBookCommand(Command):
    def __init__(self, user) -> None:
        self.user = user

    def execute(self) -> None:
        self.user.delete_book_command()


class SearchMenuCommand(Command):
    def __init__(self, app) -> None:
        self.app = app

    def execute(self) -> None:
        self.app.search_menu()


class ChangeStatusCommand(Command):
    def __init__(self, user) -> None:
        self.user = user

    def execute(self) -> None:
        self.user.change_status_command()


class ShowAllBooksCommand(Command):
    def __init__(self, user) -> None:
        self.user = user

    def execute(self) -> None:
        self.user.show_all_books_command()


class ExitCommand(Command):
    def execute(self):
        print(Phrases.bye_bye_phrase)
        return False
