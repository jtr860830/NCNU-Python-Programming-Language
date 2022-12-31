input_from_user: str = input("input an integer: ")
num: int = int(input_from_user)

result: float = 0
for i in range(num):
    result += 1 / (i + 1)
print(round(result, 5))
