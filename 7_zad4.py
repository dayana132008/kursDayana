numbersNiz = input().split(" ")
numbers = []
for n in numbersNiz:
    numbers.append(int(n))
result = sorted(numbers)
for n in result:
    print(n, end=" ")