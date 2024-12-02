import json
from utils.pharses import Phrases


class Library:
    def __init__(self, filename="library.json") -> None:
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return []

    def save_book(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.books, file, indent=4, ensure_ascii=False)

    def add_book(self, author: str):
        self.books.append(author)
        self.save_book()

    def remove_books(self, title):
        book_to_remove = next(
            (book for book in self.books if book["title"].lower() == title.lower()),
            None,
        )
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_book()
            return Phrases.successful_removal_text.format(title)
        return Phrases.book_not_found.format(title)
