a = int(input())
b = int(input())
c = int(input())
def minNumber(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c
    elif a==b and c==b:
        return a
    else:
        if a==b and a < c:
            return a
        elif b==c and b < a:
            return b
        else:
            return c
print(minNumber(a, b, c))