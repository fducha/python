def get_avg(grade_list: list) -> float:
    return sum(grade_list) / len(grade_list)


def get_math_grade(student: str) -> int:
    return int(student.split(';')[1])


def get_phis_grade(student: str) -> int:
    return int(student.split(';')[2])


def get_rus_grade(student: str) -> int:
    return int(student.split(';')[3])


math_grades = []
phis_grades = []
rus_grades = []
avg_grades = []

with open('dataset_3363_4.txt', ) as file:
    for s in file:
        if s != '\n':
            math_gr = get_math_grade(s)
            math_grades.append(math_gr)
            phis_gr = get_phis_grade(s)
            phis_grades.append(phis_gr)
            rus_gr = get_rus_grade(s)
            rus_grades.append(rus_gr)
            avg_grades.append((math_gr + phis_gr + rus_gr) / 3)


with open('dataset_3363_4.txt', 'a') as file:
    for gr in avg_grades:
        print(gr, file=file)
    print(get_avg(math_grades), get_avg(phis_grades), get_avg(rus_grades), end=' ', file=file)
