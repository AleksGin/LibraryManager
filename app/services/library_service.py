from library import Library
from utils.pharses import Phrases


class LibraryService:
    def __init__(self, library: Library) -> None:
        self.library = library

    def add_book(self, details: dict):
        self.library.add_book(details=details)
        print(Phrases.successful_add_test.format())
        
    @staticmethod
    def _check_for_duplicate(library: Library):
        ...
    
