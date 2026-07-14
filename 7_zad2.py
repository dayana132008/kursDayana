a = int(input())
b = int(input())
c = int(input())
def sum_numbers(a, b):
    return a + b
def substract(sum, c):
    return sum - c
def add_and_subtract(a, b, c):
    sum = sum_numbers(a, b)
    return substract(sum, c)
print(add_and_subtract(a, b, c))
