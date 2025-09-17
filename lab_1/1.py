class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = list(map(int, grades.split(',')))

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def is_excellent(self):
        return self.average_grade() >= 4.5

students = []
with open('students.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = line.strip().split(';')
        students.append(Student(data[0], data[1], data[2]))

with open('excellent_students.txt', 'w', encoding='utf-8') as file:
    for student in students:
        if student.is_excellent():
            file.write(f"{student.name} - {student.group}\n")

from collections import defaultdict
group_grades = defaultdict(list)

for student in students:
    group_grades[student.group].append(student.average_grade())

for group, grades in group_grades.items():
    print(f"Группа {group}: Средний балл = {sum(grades) / len(grades):.2f}")

#Содержимое файла students.txt сгенерировал ии

