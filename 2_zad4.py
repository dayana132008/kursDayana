date1 = input()
parts = date1.split(".")
year2 = int(parts[2]) + 1
date2 = parts[0] + "." + parts[1] + "." + str(year2)
print(date2)