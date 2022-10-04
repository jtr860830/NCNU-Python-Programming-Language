import sys

input_from_user: list[str] = input("input two numbers (>0): ").split(" ")
x: int = int(input_from_user[0])
n: int = int(input_from_user[1])

try:
    if x <= 0 or n <= 0:
        raise ValueError
except ValueError:
    print("Invalid input.")
    sys.exit(1)

s: int = sum([i**x for i in range(1, n + 1)])
print(f"result: {s**0.5}")
