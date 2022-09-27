import math
import sys

input_from_user: str = input("input a number: ")
n: int = int(input_from_user)

try:
    if n <= 0 or (n % 2) == 0:
        raise ValueError
except ValueError:
    print("Invalid input.")
    sys.exit(1)

sqaure_matirx: list[list[int]] = [[0 for _ in range(n)] for _ in range(n)]
row, col = (0, math.ceil(n / 2) - 1)
sqaure_matirx[row][col] = 1

for i in range(2, n * n + 1):
    tmp_row = row - 1 if row != 0 else row + n - 1
    tmp_col = col - 1 if col != 0 else col + n - 1
    if sqaure_matirx[tmp_row][tmp_col] != 0:
        tmp_row = row + 1 if row != 4 else 0
        tmp_col = col
    col = tmp_col
    row = tmp_row
    sqaure_matirx[row][col] = i

for i in range(n):
    print(*sqaure_matirx[i], sep=" | ")
