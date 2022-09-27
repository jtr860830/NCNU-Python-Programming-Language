from functools import reduce

input_from_user: str = input("input an integer: ")
num = int(input_from_user)

print(round(reduce(lambda sum, n: sum + 1 / n, range(1, num + 1)), 5))
