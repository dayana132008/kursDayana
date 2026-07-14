sum = float(input())
country = input()

if country == "България":
    print("Крайна цена: ", sum + 0.02 * sum, "лева")
elif country == "Австрия" or country == "Албания" or country == "Андора" or country == "Беларус" or country == "Белгия" or country == "Босна и Херцеговина" or country == "Ватикан" or country == "Великобритания" or country == "Германия" or country == "Гърция" or country == "Дания" or country == "Естония" or country == "Ирландия" or country == "Исландия" or country == "Испания" or country == "Италия" or country == "Кипър" or country == "Латвия" or country == "Литва" or country == "Лихтенщайн" or country == "Люксембург" or country == "Малта" or country == "Молдова" or country == "Монако" or country == "Нидерландия" or country == "Норвегия" or country == "Полша" or country == "Португалия" or country == "Румъния" or country == "Русия" or country == "Сан Марино" or country == "Северна Македония" or country == "Словакия" or country == "Словения" or country == "Сърбия" or country == "Турция" or country == "Украйна" or country == "Унгария" or country == "Финландия" or country == "Франция" or country == "Хърватия" or country == "Черна гора" or country == "Чехия" or country == "Швейцария" or country == "Швеция":
    print("Крайна цена: ", sum + 0.05 * sum, "лева")
else:
    print("Крайна цена: ", sum + 0.1 * sum, "лева")