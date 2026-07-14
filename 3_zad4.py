day = input().lower()
match day:
    case "monday" | "tuesday" | "friday":
        print(12)
    case "wednesday" | "thursday":
        print(14)
    case "saturday" | "sunday":
        print(16)
    case _:
        print("Invalid input")
