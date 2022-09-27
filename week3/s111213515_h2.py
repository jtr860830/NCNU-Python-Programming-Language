input_from_user: str = input("input a number from 1 to 9: ")
num: int = int(input_from_user)

try:
    if num < 1 or num > 9:
        raise ValueError
except ValueError:
    print("Invalid input.")

line_num: int = num * 2 - 1
for i in range(line_num, 0, -1):
    space_num: int = i % num if i >= num else num - i
    print(" " * space_num * 2, end="")
    print(*range(space_num + 1, num + 1), sep=" ")
