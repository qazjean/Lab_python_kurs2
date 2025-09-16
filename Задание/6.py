student = {
    "name": "Лиза",
    "age": 19,
    "course": 2,
    "grades": [4, 5, 5, 5, 4]
}

print(f"Имя: {student['name']}, Курс: {student['course']}")

average_grade = sum(student['grades']) / len(student['grades'])
print(f"Средний балл: {average_grade:.2f}")

student['grades'].append(5)
print("Обновленный словарь:", student)