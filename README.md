# _LibraryManager 📖_

**LibraryManage** — *это система управления библиотекой, которая помогает пользователям управлять книгами в библиотеке, включая функции добавления, поиска, удаления и изменения статусов книг. Система предоставляет удобный интерфейс командной строки для взаимодействия с коллекцией библиотеки.*

## ✨ Возможности:

+ Добавить книгу: Добавить новую книгу в библиотеку с указанием названия, автора и года выпуска.
+ Поиск книг: Искать книги по названию, автору или году выпуска.
+ Удаление книги: Удалить книгу из библиотеки по её идентификатору.
+ Изменение статуса книги: Обновить статус книги (например, "В наличии" или "Выдана").
+ Управление библиотекой: Организовывать и управлять всеми аспектами библиотеки через различные команды.

## 💻 Установка

Для начала работы с **LibraryManage** следуйте этим шагам:

### Шаги установки:


+ Склонируйте репозиторий на свою локальную машину:

```bash
git clone https://github.com/AleksGin/LibraryManager.git
```

+ Перейдите в каталог проекта:

```bash
cd LibraryManage/app
```

+ Запустите приложение: 

```bash
python3 -m main
```



## 📝 Использование
После запуска приложения вы увидите главное меню с различными функциями.

Главное меню:

+ Добавить книгу: Добавьте новую книгу в библиотеку.
+ Поиск книг: Ищите книги по автору, году или названию.
+ Удалить книгу: Удалите существующую книгу.
+ Изменить статус книги: Измените статус доступности книги.
+ Показать все книги: Получите все книги в библиотеке.
+ Выход: Выйти из приложения.


Меню поиска:

+ Поиск по автору: Введите имя автора, чтобы найти его книги.
+ Поиск по году: Введите год, чтобы найти книги, изданные в этот год.
+ Поиск по названию: Ищите книги по названию.
+ Главное меню: Переход в главное меню
+ Выход: Выйти из приложения.


## 🔧 Структура кода
Проект организован в разные модули для удобства поддержки и расширения:

### Application: Главная точка входа в программу, управляющая навигацией и взаимодействием с пользователем.

```python
class Application:
    def __init__(self) -> None:
        self.library = LibraryRepository()
        self.libary_service = LibraryService(library=self.library)
        self.user = User(library_service=self.libary_service)

    def main_menu(self) -> None:
        options = {
            "1": (
                "Добавить книгу",
                AddBookCommand(user=self.user),
            ),
            "2": (
                "Найти книгу",
                SearchMenuCommand(app=self),

    ...


```


### Команды: Содержит классы для выполнения действий, таких как добавление книг, поиск и изменение статусов.


```python 
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class AddBookCommand(Command)
    ...

class DeleteBookCommand(Command)
    ...

class SearchMenuCommand(Command)
    ...

...
```
### Модели: Определяет основные объекты, такие как Book, Library и User.

```python
class User:
    def __init__(self, library_service: LibraryService) -> None:
        self.library_service = library_service

    ...
```

```python
class LibraryRepository:
    def __init__(self, filename="filename.json") -> None:
        self.filename = filename
        self.books = self.load_books()
    
    ...
```



### Сервисы: Содержит бизнес-логику и обработку данных книг.

```python
class LibraryService:
    def __init__(self, library: LibraryRepository) -> None:
        self.library = library
        self.current_id = max((book["id"] for book in self.library.books), default=0)
    
    ...
```
### Меню: Обрабатывает логику отображения меню.

```python
class Menu:
    def __init__(
        self,
        options: dict[str, tuple[str, Command]],
    ) -> None:
        self.options = options
    
    ...
```


## _Спасибо за внимание!_







