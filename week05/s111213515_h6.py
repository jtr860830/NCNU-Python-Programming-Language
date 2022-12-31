import sys


def reverse(matrix: list[list[int]]) -> list[list[int]]:
    for i in range(int(len(matrix) / 2)):
        matrix[i], matrix[len(matrix) - 1 - i] = matrix[len(matrix) - 1 - i], matrix[i]
    return matrix


def rotate(matrix: list[list[int]]) -> list[list[int]]:
    result: list[list[int]] = []
    for i in range(len(matrix[0])):
        result.insert(0, [])
        for j in range(len(matrix)):
            result[0].append(matrix[j][i])
    return result


try:
    r, c, m = [int(s) for s in input().split()]
    matrix: list[list[int]] = []
    for _ in range(r):
        matrix.append([int(s) for s in input().split()[0:c]])
    actions: list[int] = [int(s) for s in input().split()[0:m]]
    actions.reverse()
except ValueError:
    print("Invalid input.")
    sys.exit(1)

for action in actions:
    match (action):
        case 0:
            matrix = rotate(matrix)
        case 1:
            matrix = reverse(matrix)

print(f"{len(matrix)} {len(matrix[0])}")
for i in range(len(matrix)):
    print(*matrix[i], sep=" ")
