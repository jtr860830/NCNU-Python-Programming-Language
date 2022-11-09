import sys
from s111213515_h1 import hw1

try:
    x: int = int(input())
    y: int = int(input())
    if y < x:
        raise ValueError
except ValueError:
    print("Invalid input.")
    sys.exit(1)

results: list[tuple[int, int, int]] = []
for i in range(x, y + 1):
    results.append(hw1(i))

results.sort(key=lambda r: r[1])
for result in results:
    print(
        f"Original number is {result[0]}. Palindromic number is {result[1]}. Execution time is {result[2]}"
    )
