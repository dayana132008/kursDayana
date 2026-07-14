N = int(input())
days_counter = {}
for i in range(N):
    day = input()
    if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday" or day == "saturday" or day == "sunday":
        if day in days_counter:
            days_counter[day] += 1
        else:
            days_counter[day] = 1
    else:
        print("invalid day of the week")

for day in days_counter:
    print(day + " - " + str(days_counter[day]))
