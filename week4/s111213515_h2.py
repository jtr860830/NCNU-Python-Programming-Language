import sys

input_from_user: str = input("input an integer: ")
n: int = int(input_from_user)

try:
    if n < 2:
        raise ValueError
except ValueError:
    print("Invalid input.")
    sys.exit(1)

result1: int = sum([(i - 1) * (i + 1) for i in range(2, n + 1)])
result2: float = sum([1 / (i + 1) for i in range(1, n + 1)])

print(f"f(n) = {result1}")
print(f"f(n) = {result2}")
