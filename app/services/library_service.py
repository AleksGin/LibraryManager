from library import Library
from utils.pharses import (
    ErrorPhrases,
    Phrases,
    ParseForm,
)


class LibraryService:
    def __init__(self, library: Library) -> None:
        self.library = library
        self.current_id = max((book["id"] for book in self.library.books), default=0)

    def add_book(self, details: dict) -> None:
        details_with_id_and_status = self._add_id_and_status(details=details)
        self.library.append_book(details=details_with_id_and_status)
        self._notification(Phrases.successful_add_test)

    def delete_book(self, book_id: int) -> None:
        book_to_remove = self._check_for_available_book_by_id(book_id=book_id)

        if book_to_remove:
            self.library.remove_book(book_to_remove=book_to_remove)
            self._notification(
                Phrases.successful_removal.format(book_id, book_to_remove["title"])
            )
        else:
            self._notification(ErrorPhrases.book_not_found.format(book_id))

    def get_books_by_search_type(self, search_type: str, value: int | str) -> None:
        books_by_search_type = [
            book for book in self.library.books if book[search_type] == value
        ]
        if books_by_search_type:
            self._parse(books=books_by_search_type, value=value)
        else:
            self._notification(
                phrase=ErrorPhrases.books_by_search_type_not_found.format(value)
            )

    def set_new_status_by_id(self, book_id: int, status: str) -> None:
        book = self._check_for_available_book_by_id(book_id=book_id)

        if book:
            book["status"] = status
            self.library.save_book()
            self._notification(phrase=Phrases.successful_set_new_status)
        else:
            self._notification(ErrorPhrases.book_not_found.format(book_id))

    def get_all_books(self) -> None:
        books = [book for book in self.library.books]

        if books:
            self._parse(books=books, value="Все книги")
        else:
            self._notification(phrase=ErrorPhrases.library_is_empty)

    def _check_for_available_book_by_id(self, book_id: int) -> dict | None:
        book = next(
            (book for book in self.library.books if book["id"] == book_id), None
        )
        return book

    def _add_id_and_status(self, details: dict) -> dict:
        self.current_id += 1

        add_form = {
            "id": self.current_id,
            **details,
            "status": "В наличии",
        }

        return add_form

    def _notification(self, phrase: str) -> None:
        print(phrase)

    def _parse(
        self,
        books: list,
        value: str | int,
    ) -> None:
        print(ParseForm.search_type_string.format(value))
        for book in books:
            print(
                ParseForm.response_form_with_search_type.format(
                    book["id"],
                    book["title"],
                    book["author"],
                    book["year"],
                    book["status"],
                )
            )
