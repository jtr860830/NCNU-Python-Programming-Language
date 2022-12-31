input_from_user: list[str] = input("input two integers: ").split(" ")
x: int = int(input_from_user[0])
y: int = int(input_from_user[1])

big: int = x if x > y else y
reverse: int = int(str(big)[::-1])
digit: int = len(str(big))
odd: int = 0
even: int = 0
s: int = 0
for c in str(big):
    if int(c) % 2 == 0:
        even += 1
    else:
        odd += 1
    s += int(c)

print(f"{big} is the bigger one")
print(f"{odd} odds and {even} evens")
print(f"sum is {s}")
print(f"{big} + {reverse} = {big + reverse}")
