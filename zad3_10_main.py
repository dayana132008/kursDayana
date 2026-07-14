from zad3_10 import Calculator
calculator = Calculator()
a = int(input())
b = int(input())
print(f"{a} + {b} = {calculator.add(a, b)}")
print(f"{a} - {b} = {calculator.subtract(a, b)}")
print(f"{a} * {b} = {calculator.multiply(a, b)}")
print(f"{a} / {b} = {calculator.divide(a, b)}")
