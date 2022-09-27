from functools import reduce

input_from_user: str = input("input an integer: ")
num = int(input_from_user)

it = iter(range(1, num + 1))
result: float = 0
while n := next(it, None):
    result += 1 / n
print(round(result, 5))
