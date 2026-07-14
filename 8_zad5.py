class Vehicle:
    gadgets = []
    def __init__(self, mileage):
        self.max_speed = 150
        self.mileage = mileage
car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)