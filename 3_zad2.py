age = int(input())
gender = input()
if gender == "m" or gender == "f":
    if age >= 16:
        if gender == "m":
            print("Mr.")
        else:
            print("Ms.")
    else:
        if gender == "m":
            print("Master.")
        else:
            print("Miss.")
else:
    print("invalid gender")
