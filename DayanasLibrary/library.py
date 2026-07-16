import json
import os

from elements import LibraryItem, Book, EBook, Reader


def get_title_key(item):
    return item.title.lower()


def get_year_key(item):
    return item.year


class Library:

    def __init__(self):
        self.items = []
        self.readers = []
        self._next_item_id = 1
        self._next_reader_id = 1

    def __len__(self):
        return len(self.items)

    def add_book(self, title, author, year, isbn, pages):
        if LibraryItem.validate_year(year) == False:
            raise ValueError("Невалидна година на издаване.")

        if Book.validate_isbn(isbn) == False:
            raise ValueError("Невалиден ISBN (трябва да е 10 или 13 цифри).")

        new_book = Book(self._next_item_id, title, author, int(year), isbn, int(pages))
        self.items.append(new_book)
        self._next_item_id = self._next_item_id + 1
        return new_book

    def add_ebook(self, title, author, year, file_format, file_size):
        if LibraryItem.validate_year(year) == False:
            raise ValueError("Невалидна година на издаване.")

        new_ebook = EBook(self._next_item_id, title, author, int(year), file_format, float(file_size))
        self.items.append(new_ebook)
        self._next_item_id = self._next_item_id + 1
        return new_ebook

    def add_reader(self, name):
        new_reader = Reader(self._next_reader_id, name)
        self.readers.append(new_reader)
        self._next_reader_id = self._next_reader_id + 1
        return new_reader

    def show_all_items(self):
        if len(self.items) == 0:
            print("Няма добавени ресурси.")
            return

        for item in self.items:
            print(item)

    def show_all_readers(self):
        if len(self.readers) == 0:
            print("Няма регистрирани читатели.")
            return

        for reader in self.readers:
            print(reader)

    def show_borrowed_items(self):
        borrowed_list = []

        for item in self.items:
            if isinstance(item, EBook):
                if len(item.borrowers) > 0:
                    borrowed_list.append(item)
            else:
                if item.is_available() == False:
                    borrowed_list.append(item)

        if len(borrowed_list) == 0:
            print("Няма заети ресурси.")
            return

        for item in borrowed_list:
            print(item)

    def search_by_title(self, title):
        # линейно търсене - времева сложност O(n)
        found = None
        for i in self.items:
            if i.title.lower() == title.lower():
                found = i
                break
        return found

    def sort_items(self, sort_by = "title"):
        if sort_by == "year":
            self.items = sorted(self.items, key=get_year_key)
        else:
            self.items = sorted(self.items, key=get_title_key)
        return self.items

    def find_item_by_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def find_reader_by_id(self, reader_id):
        for reader in self.readers:
            if reader.reader_id == reader_id:
                return reader
        return None

    def edit_item(self, item_id, title=None, author=None, year=None):
        item = self.find_item_by_id(item_id)

        if item is None:
            raise ValueError(f"Няма ресурс с номер {item_id}.")

        if title is not None and title != "":
            item.title = title

        if author is not None and author != "":
            item.author = author

        if year is not None and year != "":
            if LibraryItem.validate_year(year) == False:
                raise ValueError("Невалидна година на издаване.")
            item.year = int(year)

        return item

    def delete_item(self, item_id):
        item = self.find_item_by_id(item_id)

        if item is None:
            raise ValueError(f"Няма ресурс с номер {item_id}.")

        if isinstance(item, EBook):
            if len(item.borrowers) > 0:
                raise ValueError(f"Ресурсът '{item.title}' е зает от читатели и не може да бъде изтрит.")
        else:
            if item.is_available() == False:
                raise ValueError(f"Ресурсът '{item.title}' е зает и не може да бъде изтрит.")

        self.items.remove(item)
        return item

    def borrow_item(self, reader_id, item_id):
        reader = self.find_reader_by_id(reader_id)
        item = self.find_item_by_id(item_id)

        if reader is None:
            raise ValueError(f"Няма читател с номер {reader_id}.")

        if item is None:
            raise ValueError(f"Няма ресурс с номер {item_id}.")

        item.borrow(reader)
        return item

    def return_item(self, reader_id, item_id):
        reader = self.find_reader_by_id(reader_id)
        item = self.find_item_by_id(item_id)

        if reader is None:
            raise ValueError(f"Няма читател с номер {reader_id}.")

        if item is None:
            raise ValueError(f"Няма ресурс с номер {item_id}.")

        item.return_item(reader)
        return item

    def save_to_json(self, filename):
        items_as_dicts = []
        for item in self.items:
            items_as_dicts.append(item.to_dict())

        readers_as_dicts = []
        for reader in self.readers:
            readers_as_dicts.append(reader.to_dict())

        data = {
            "items": items_as_dicts,
            "readers": readers_as_dicts,
            "next_item_id": self._next_item_id,
            "next_reader_id": self._next_reader_id,
        }

        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Запазено във '{filename}'.")
        except OSError as e:
            print(f"Грешка при запис: {e}")

    def load_from_json(self, filename):
        if os.path.exists(filename) == False:
            print(f"Файл '{filename}' не е намерен, започваме с празна библиотека.")
            return

        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"Файлът е повреден ({e}), започваме с празна библиотека.")
            return

        self.items = []
        self.readers = []

        try:
            items_data = data.get("items", [])
            for item_data in items_data:
                item_type = item_data.get("type")

                if item_type == "Book":
                    new_book = Book(
                        item_data["item_id"],
                        item_data["title"],
                        item_data["author"],
                        item_data["year"],
                        item_data.get("isbn", ""),
                        item_data.get("pages", 0),
                    )
                    new_book._available = item_data.get("available", True)
                    self.items.append(new_book)

                elif item_type == "EBook":
                    new_ebook = EBook(
                        item_data["item_id"],
                        item_data["title"],
                        item_data["author"],
                        item_data["year"],
                        item_data.get("file_format", ""),
                        item_data.get("file_size", 0),
                        borrowers=item_data.get("borrowers", []),
                    )
                    self.items.append(new_ebook)

            readers_data = data.get("readers", [])
            for reader_data in readers_data:
                new_reader = Reader(
                    reader_data["reader_id"],
                    reader_data["name"],
                    borrowed_items=reader_data.get("borrowed_items", []),
                    regular_books=reader_data.get("regular_books", []),
                )
                self.readers.append(new_reader)

            if "next_item_id" in data:
                self._next_item_id = data["next_item_id"]
            else:
                max_item_id = 0
                for item in self.items:
                    if item.item_id > max_item_id:
                        max_item_id = item.item_id
                self._next_item_id = max_item_id + 1

            if "next_reader_id" in data:
                self._next_reader_id = data["next_reader_id"]
            else:
                max_reader_id = 0
                for reader in self.readers:
                    if reader.reader_id > max_reader_id:
                        max_reader_id = reader.reader_id
                self._next_reader_id = max_reader_id + 1

            print(f"Заредено от '{filename}'.")

        except (KeyError, TypeError, ValueError) as e:
            print(f"Невалидни данни във файла ({e}), започваме с празна библиотека.")
            self.items = []
            self.readers = []