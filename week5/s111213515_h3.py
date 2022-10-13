import sys

try:
    n: int = int(input("Input number of segment: "))
    segments: list[tuple[int, int]] = []
    for _ in range(n):
        p1, p2 = input().split(" ")
        segments.append((int(p1), int(p2)))
except ValueError:
    print("Invalid input.")
    sys.exit(1)

segments.sort(key=lambda s: s[0])

result: int = 0
i: int = 0
while i < len(segments):
    start, end = segments[i]
    tmp_i: int = i + 1
    while tmp_i < len(segments) and segments[tmp_i][0] <= segments[i][1]:
        end = (
            segments[tmp_i][1]
            if segments[tmp_i][1] > segments[i][1]
            else segments[i][1]
        )
        tmp_i += 1
    result += end - start
    i = tmp_i

print(f"result: {result}")
