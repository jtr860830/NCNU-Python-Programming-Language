def hw1(num: int, print_process_trigger: bool = False) -> tuple[int, int, int]:
    original_num: int = num
    time: int = 0
    while True:
        time += 1
        reversed_num: int = int(str(num)[::-1])
        if print_process_trigger:
            print(num)
            print(reversed_num)
            print("--------")
        if num == reversed_num:
            break
        else:
            num += reversed_num
    return original_num, num, time


if __name__ == "__main__":
    original_num, num, time = hw1(int(input()), True)
    print(
        f"Original number is: {original_num}. Palindromic number is {num}. Execution time is {time}"
    )
