import json


class Library:
    def __init__(self, filename="library.json") -> None:
        self.filename = filename
        self.books = self.load_books()

    def load_books(self) -> list:
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return []

    def append_book(self, details: dict) -> None:
        self.books.append(details)
        self.save_book()

    def remove_book(self, book_to_remove: dict) -> None:
        self.books.remove(book_to_remove)
        self.save_book()

    def save_book(self) -> None:
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.books, file, indent=4, ensure_ascii=False)
