a = int(input())
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
else:
    print("No")