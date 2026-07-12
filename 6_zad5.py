n = int(input())
sum = 0
sum1 = 0
diff = 0
for i in range(1,n+1):
    num = int(input())
    if i % 2 == 1:
        sum1 += num
    else:
        sum += num
if sum == sum1:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    if sum > sum1:
        diff = sum - sum1
        print(f"Diff = {diff}")
    else:
        diff = sum1 - sum
        print(f"Diff = {diff}")