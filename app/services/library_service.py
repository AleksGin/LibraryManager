from library import Library
from utils.pharses import Phrases


class LibraryService:
    def __init__(self, library: Library) -> None:
        self.library = library

    def add_book(self, author: str):
        self.library.add_book(author=author)
        return Phrases.successful_add_test.format(author)
