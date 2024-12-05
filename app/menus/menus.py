from commands import Command
from utils.pharses import ErrorPhrases


class Menus:
    def __init__(
        self,
        options: dict[str, tuple[str, Command]],
        exit_phrase: str,
    ) -> None:
        self.options = options
        self.exit_phrase = exit_phrase

    def show_menu(self):
        while True:
            for key, (description, _) in self.options.items():
                print(f"{key}. {description}")
            command = input("> ")

            if command in self.options:
                _, action = self.options[command]
                action.execute()
            else:
                print(ErrorPhrases.wrong_command)
