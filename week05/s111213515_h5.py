import sys

try:
    sides: list[int] = [
        int(s) for s in input("input three numbers a, b, c (c is the max): ").split(" ")
    ]
    sides.sort()
    a, b, c = sides
    if a > 30000 or b > 30000 or c > 30000:
        raise ValueError
except ValueError:
    print("Invalid input.")
    sys.exit(1)

print(*sides, sep=" ")

if a + b <= c:
    print("No")
    sys.exit(0)

if a * a + b * b < c * c:
    print("Obtuse")
elif a * b * b > c * c:
    print("Acute")
else:
    print("Right")
