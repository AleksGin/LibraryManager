from exceptions import (
    EmptyValueError,
    InvalidTypeError,
)

from utils.pharses import (
    ErrorPhrases,
    Phrases,
)


class InputHandler:
    @staticmethod
    def get_book_details() -> dict[str, str]:
        try:
            title = InputHandler._validate_book_details(
                text=Phrases.ask_for_title,
                allow_numeric=True,
            )
            author = InputHandler._validate_book_details(
                Phrases.ask_for_author,
                allow_numeric=False,
            )
            year = InputHandler._validate_book_details(
                Phrases.ask_for_year,
                only_numeric=True,
            )
        except ValueError as e:
            print(f"Ошибка: {e}")
        return {"title": title, "author": author, "year": year}

    @staticmethod
    def _validate_book_details(
        text: str,
        allow_numeric: bool = False,
        only_numeric: bool = False,
    ) -> str:
        while True:
            value = input(text)
            try:
                InputHandler._check_for_empty(value=value)
                if only_numeric:
                    return InputHandler._check_is_only_numeric(value=value)
                elif allow_numeric:
                    return InputHandler._check_allow_numeric(
                        value=value, allow_numeric=True
                    )
                else:
                    return InputHandler._check_allow_numeric(
                        value=value, allow_numeric=False
                    )
            except InvalidTypeError:
                print(ErrorPhrases.wrong_input_value)
            except EmptyValueError:
                print(ErrorPhrases.empty_value_error)

    @staticmethod
    def _check_for_empty(value: str) -> str:
        if not value.strip():
            raise EmptyValueError()
        return value.strip().title()

    @staticmethod
    def _check_is_only_numeric(value: str) -> str:
        if value.isdigit():
            return value.strip()
        else:
            raise InvalidTypeError()

    @staticmethod
    def _check_allow_numeric(value: str, allow_numeric: bool) -> str:
        if allow_numeric:
            if value.isdigit():
                return value.strip()
            else:
                return value.strip().capitalize()
        else:
            if value.isdigit():
                raise InvalidTypeError()
