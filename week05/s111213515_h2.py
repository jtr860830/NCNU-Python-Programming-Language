import sys

try:
    n: int = int(input("Input number of students: "))
    scores: list[int] = [int(s) for s in input("Input scores: ").split(" ")]
    if n != len(scores):
        raise ValueError
except ValueError:
    print("Invalid input.")
    sys.exit(1)

scores.sort()
print(*scores, sep=" ")

max_failed_score: int | None = max(list(filter(lambda s: s < 60, scores)), default=None)
if max_failed_score == None:
    print("best case")
else:
    print(max_failed_score)

min_passed_score: int | None = min(
    list(filter(lambda s: s >= 60, scores)), default=None
)
if min_passed_score == None:
    print("worst case")
else:
    print(min_passed_score)
