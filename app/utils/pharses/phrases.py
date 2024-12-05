class Phrases:
    successful_removal = (
        "\n~ Книга с id: №{} была удалена! ~\n" "~ Название книги: <<{}>> ~"
    )
    successful_add_test = "\n~ Книга успешна добавлена! ~"
    successful_set_new_status = "\n ~ Статус успешно изменен! ~"
    ask_for_author = "Введите имя автора: "
    ask_for_title = "Введите название книги: "
    ask_for_year = "Введите год издания: "
    ask_book_id = "\nВведите id книги: "
    ask_for_status = (
        '\n~ Возможные статусы: "В наличии", "Выдана" ~\n' "\nВведите статус: "
    )
    bye_bye_phrase = (
        "\nЗавершаю работу... До свидания!\n"
    )
    choice_command = (
        "\nВыберите необходимую команду: "
    )


class ErrorPhrases:
    empty_value_error = "\n<<Ошибка>>: Значение не может быть пустым!"
    wrong_input_value = (
        "\n<<Ошибка>>: Неправильный формат ввода!\n" "Ожидается корректное значение>>\n"
    )
    book_not_found = "\nКнига с id №{} не найдена :("
    books_by_search_type_not_found = '\nКниги по запросу "{}" не найдены :('
    library_is_empty = "\nВ данный момент книги отсутствуют :("
    wrong_status = '\n<<Ошибка>>: Cтатус может быть только "В наличии" или "Выдан"!'
    wrong_command = "\n<<Ошибка>>: Неправильная команда!\n"


class ParseForm:
    search_type_string = (
        "\nВсе книги по запросу: <{}>\n"
    )    
    response_form_with_search_type = (
        "______________________\n"
        "\nid: №{}\n"
        'Название: "{}"\n'
        "Автор: {}\n"
        "Год: {}\n"
        "Статус: {}\n"
        "______________________\n"
    )
