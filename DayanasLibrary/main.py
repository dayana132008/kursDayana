from library import Library
DATA_FILE = "data.json"

def print_menu():
    print("\nБИБЛИОТЕКА")
    print("1. Добавяне на обикновена книга")
    print("2. Добавяне на електронна книга")
    print("3. Показване на всички ресурси")
    print("4. Търсене на книга по заглавие")
    print("5. Сортиране на книгите")
    print("6. Регистриране на читател")
    print("7. Показване на читателите")
    print("8. Заемане на книга/е-книга")
    print("9. Връщане на книга/е-книга")
    print("10. Показване на заетите ресурси")
    print("11. Редактиране на книга/е-книга")
    print("12. Изтриване на книга/е-книга")
    print("0. Изход със запазване на данните")
    print()


def read_int(prompt):
    while True:
        text = input(prompt).strip()
        try:
            number = int(text)
            return number
        except ValueError:
            print("Не е число.")


def add_book_act(library):
    try:
        title = input("Заглавие: ").strip()
        author = input("Автор: ").strip()
        year = input("Година на издаване: ").strip()
        isbn = input("ISBN (10/13 цифри): ").strip()
        pages = input("Брой страници: ").strip()

        if title == "" or author == "":
            print("Заглавието и авторът не може да са празни.")
            return

        new_book = library.add_book(title, author, year, isbn, pages)
        print(f"Добавено: {new_book}")

    except ValueError as e:
        print(f"Грешка при добавяне на книга: {e}")


def add_ebook_act(library):
    try:
        title = input("Заглавие: ").strip()
        author = input("Автор: ").strip()
        year = input("Година на издаване: ").strip()
        file_format = input("Файлов формат (PDF, EPUB): ").strip()
        file_size = input("Размер на файла (MB): ").strip()

        if title == "" or author == "":
            print("Заглавието и авторът не може да са празни.")
            return

        new_ebook = library.add_ebook(title, author, year, file_format, file_size)
        print(f"Добавено: {new_ebook}")

    except ValueError as e:
        print(f"Грешка при добавяне на е-книга: {e}")


def search_act(library):
    title = input("Въведете заглавие за търсене: ").strip()
    result = library.search_by_title(title)

    if result is not None:
        print("Намерено:")
        print(result)
    else:
        print(f"Няма книга със заглавие '{title}'.")


def sort_act(library):
    print("Сортирай по: 1) заглавие  2) година")
    choice = input("Избор: ").strip()

    if choice == "2":
        library.sort_items(sort_by = "year")
    else:
        library.sort_items(sort_by = "title")

    print("Подредено:")
    library.show_all_items()


def add_reader_act(library):
    name = input("Име на читателя: ").strip()

    if name == "":
        print("Името не може да е празно.")
        return

    new_reader = library.add_reader(name)
    print(f"Регистриран: {new_reader}")


def borrow_act(library):
    try:
        reader_id = read_int("Номер на читател: ")
        item_id = read_int("Номер на ресурс: ")
        item = library.borrow_item(reader_id, item_id)
        print(f"Заето: {item}")

    except ValueError as e:
        print(f"Грешка при заемане: {e}")


def edit_act(library):
    try:
        item_id = read_int("Номер на ресурс: ")
        print("Остави празно, ако не искаш да променяш.")
        title = input("Ново заглавие: ").strip()
        author = input("Нов автор: ").strip()
        year = input("Нова година: ").strip()

        item = library.edit_item(item_id, title=title, author=author, year=year)
        print(f"Редактирано: {item}")

    except ValueError as e:
        print(f"Грешка при редактиране: {e}")


def delete_act(library):
    try:
        item_id = read_int("Номер на ресурс: ")
        item = library.delete_item(item_id)
        print(f"Изтрито: {item}")

    except ValueError as e:
        print(f"Грешка при изтриване: {e}")


def return_act(library):
    try:
        reader_id = read_int("Номер на читател: ")
        item_id = read_int("Номер на ресурс: ")
        item = library.return_item(reader_id, item_id)
        print(f"Върнато: {item}")

    except ValueError as e:
        print(f"Грешка при връщане: {e}")


def main():
    library = Library()
    library.load_from_json(DATA_FILE)

    running = True
    while running:
        print_menu()
        choice = input("Изберете опция: ").strip()

        if choice == "1":
            add_book_act(library)
        elif choice == "2":
            add_ebook_act(library)
        elif choice == "3":
            library.show_all_items()
        elif choice == "4":
            search_act(library)
        elif choice == "5":
            sort_act(library)
        elif choice == "6":
            add_reader_act(library)
        elif choice == "7":
            library.show_all_readers()
        elif choice == "8":
            borrow_act(library)
        elif choice == "9":
            return_act(library)
        elif choice == "10":
            library.show_borrowed_items()
        elif choice == "11":
            edit_act(library)
        elif choice == "12":
            delete_act(library)
        elif choice == "0":
            library.save_to_json(DATA_FILE)
            print("Излязохте от библиотеката!")
            running = False
        else:
            print("Невалидна опция.")


if __name__ == "__main__":
    main()