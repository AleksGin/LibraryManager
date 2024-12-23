from commands import Command


class SearchByTypeCommand(Command):
    def __init__(
        self,
        user,
        search_type: str,
        prompt: str,
        only_numeric: bool = False,
        allow_numeric: bool = False,
    ) -> None:
        self.user = user
        self.search_type = search_type
        self.prompt = prompt
        self.only_numeric = only_numeric
        self.allow_numeric = allow_numeric

    def execute(self) -> None:
        self.user.search_by_any_type_commmand(
            search_type=self.search_type,
            prompt=self.prompt,
            numeric_only=self.only_numeric,
            allow_numeric=self.allow_numeric,
        )


class ToMainMenuCommand(Command):
    def __init__(self, app) -> None:
        self.app = app

    def execute(self) -> None:
        self.app.main_menu()
