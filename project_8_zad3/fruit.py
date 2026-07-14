from project_8_zad3.food import Food
class Fruit:
    def __init__(self, name: str, expiration_date: str):
        super().__init__(expiration_date)
        self.name = name
