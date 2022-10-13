import sys

try:
    m, n = [int(s) for s in input().split(" ")]
    picked_nums: list[int] = []
    for _ in range(m):
        picked_nums.append(max([int(s) for s in input().split()[0:n]]))
except ValueError:
    print("Invalid input.")
    sys.exit(1)

s: int = sum(picked_nums)
print(f"{s}")
divisible_nums: list[int] = list(filter(lambda x: s % x == 0, picked_nums))
if divisible_nums:
    print(*divisible_nums, sep=" ")
else:
    print(-1)
