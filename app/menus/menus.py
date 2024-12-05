from commands import Command
from utils.pharses import (
    ErrorPhrases,
    Phrases,
)


class Menu:
    def __init__(
        self,
        options: dict[str, tuple[str, Command]],
    ) -> None:
        self.options = options

    def show_menu(self):
        while True:
            print("\n")
            for key, (description, _) in self.options.items():
                print(f"{key}. {description}")
            command = input(f"{Phrases.choice_command}> ")

            if command in self.options:
                _, action = self.options[command]
                action.execute()
            else:
                print(ErrorPhrases.wrong_command)
