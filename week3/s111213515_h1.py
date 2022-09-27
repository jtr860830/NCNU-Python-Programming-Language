input_from_user: str = input("input a number from 1 to 9: ")
num: int = int(input_from_user)

try:
    if num < 1 or num > 9:
        raise ValueError
except ValueError:
    print("Invalid input.")

[print(*range(1, i + 1), sep=" ") for i in range(1, num + 1)]
