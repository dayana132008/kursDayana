numbersNiz = input().split(" ")
def even(num):
    return num % 2 == 0
numbers = []
for n in numbersNiz:
    numbers.append(int(n))
result = filter(even, numbers)
for n in result:
    print(n, end=" ")