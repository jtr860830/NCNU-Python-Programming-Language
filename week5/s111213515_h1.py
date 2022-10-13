class Student:
    def __init__(self, name: str, math_score: int, programming_score: int) -> None:
        self.name: str = name
        self.math_score: int = math_score
        self.programming_score: int = programming_score

    def show(self) -> None:
        print(f"{self.name} {self.math_score} {self.programming_score}")


FILE_PATH: str = "./s111213515_h1_sample.txt"

with open(FILE_PATH) as file:
    lines: list[str] = file.readlines()
    data: list[list[str]] = [line.rstrip().split(" ") for line in lines]
    students: list[Student] = [
        Student(student[0], int(student[1]), int(student[2])) for student in data
    ]
    students.sort(key=lambda s: s.math_score + s.programming_score)
    [student.show() for student in students]
