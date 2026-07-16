from datetime import datetime

class LibraryItem:

    def __init__(self, item_id, title, author, year):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.year = year
        self._available = True

    @staticmethod
    def validate_year(year):
        try:
            year_number = int(year)
        except (ValueError, TypeError):
            return False

        current_year = datetime.now().year

        if year_number > 0 and year_number <= current_year:
            return True
        else:
            return False

    def is_available(self):
        return self._available

    def borrow(self, reader):
        if self._available == False:
            raise ValueError(f"Ресурсът '{self.title}' вече е зает.")

        self._available = False
        reader.borrowed_items.append(self.item_id)

    def return_item(self, reader=None):
        if self._available == True:
            raise ValueError(f"Ресурсът '{self.title}' не е бил зает.")

        self._available = True

        if reader is not None:
            if self.item_id in reader.borrowed_items:
                reader.borrowed_items.remove(self.item_id)

    def show_info(self):
        print(self)

    def __str__(self):
        if self._available:
            status = "наличен"
        else:
            status = "зает"

        return f"[{self.item_id}] {self.title} ({self.year}) - {self.author} - {status}"

    def to_dict(self):
        result = {
            "type": "LibraryItem",
            "item_id": self.item_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "available": self._available,
        }
        return result


class Book(LibraryItem):
    max_books = 3

    def __init__(self, item_id, title, author, year, isbn, pages):
        super().__init__(item_id, title, author, year)
        self.isbn = isbn
        self.pages = pages

    @staticmethod
    def validate_isbn(isbn):
        isbn_text = str(isbn).replace("-", "")

        if isbn_text.isdigit() == False:
            return False

        if len(isbn_text) == 10 or len(isbn_text) == 13:
            return True
        else:
            return False

    def borrow(self, reader):
        if len(reader.regular_books) >= Book.max_books:
            raise ValueError(
                f"Читателят '{reader.name}' вече е заел максималния брой "
                f"книги ({Book.max_books})."
            )

        super().borrow(reader)
        reader.regular_books.append(self.item_id)

    def return_item(self, reader=None):
        super().return_item(reader)

        if reader is not None:
            if self.item_id in reader.regular_books:
                reader.regular_books.remove(self.item_id)

    def __str__(self):
        if self._available:
            status = "налична"
        else:
            status = "заета"

        return (
            f"[Книга #{self.item_id}] '{self.title}' от {self.author} "
            f"({self.year}), ISBN: {self.isbn}, {self.pages} стр. - {status}"
        )

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Book"
        data["isbn"] = self.isbn
        data["pages"] = self.pages
        return data


class EBook(LibraryItem):

    def __init__(self, item_id, title, author, year, file_format, file_size, borrowers=None):
        super().__init__(item_id, title, author, year)
        self.file_format = file_format
        self.file_size = file_size

        if borrowers is None:
            self.borrowers = []
        else:
            self.borrowers = borrowers

    def is_available(self):
        return True

    def borrow(self, reader):
        if reader.reader_id in self.borrowers:
            raise ValueError(
                f"Читателят '{reader.name}' вече е заел електронната книга '{self.title}'."
            )

        self.borrowers.append(reader.reader_id)
        reader.borrowed_items.append(self.item_id)

    def return_item(self, reader=None):
        if reader is None or reader.reader_id not in self.borrowers:
            raise ValueError("Тази електронна книга не е заета от този читател.")

        self.borrowers.remove(reader.reader_id)

        if self.item_id in reader.borrowed_items:
            reader.borrowed_items.remove(self.item_id)

    def __str__(self):
        broi_chitateli = len(self.borrowers)
        return (
            f"[Е-книга #{self.item_id}] '{self.title}' от {self.author} "
            f"({self.year}), формат: {self.file_format}, "
            f"размер: {self.file_size} MB, заета от {broi_chitateli} читател(и)"
        )

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "EBook"
        data["file_format"] = self.file_format
        data["file_size"] = self.file_size
        data["borrowers"] = self.borrowers
        return data


class Reader:

    def __init__(self, reader_id, name, borrowed_items=None, regular_books=None):
        self.reader_id = reader_id
        self.name = name

        if borrowed_items is None:
            self.borrowed_items = []
        else:
            self.borrowed_items = borrowed_items

        if regular_books is None:
            self.regular_books = []
        else:
            self.regular_books = regular_books

    def __str__(self):
        cnt_borrowed = len(self.borrowed_items)
        cnt_books = len(self.regular_books)
        return (
            f"[Читател #{self.reader_id}] {self.name} - "
            f"заети ресурси: {cnt_borrowed} (от които {cnt_books} обикновени книги)"
        )

    def to_dict(self):
        result = {
            "reader_id": self.reader_id,
            "name": self.name,
            "borrowed_items": self.borrowed_items,
            "regular_books": self.regular_books,
        }
        return result
