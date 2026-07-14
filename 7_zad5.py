numbersNiz = input().split(" ")
min = 999999
max = 0
sum = 0
for n in numbersNiz:
    if int(n) > max:
        max = int(n)
    if int(n) < min:
        min = int(n)
    sum += int(n)
print(f"The minimum number is {min}")
print(f"The maximum number is {max}")
print(f"The sum number is: {sum}")