input_from_user: str = input("Enter Chinese, English, math's score: ")

scores: list[int] = [int(n) for n in input_from_user.split()]
print(
    f"Chinses: {scores[0]}, English: {scores[1]}, math: {scores[2]}, total: {sum(scores)}, avg: {round(sum(scores)/len(scores), 2)}"
)
