students = [
    {"id": 1, "name": "Alice", "class": "Grade 9", "subject": "Math"},
    {"id": 2, "name": "Bob", "class": "Grade 10", "subject": "Science"},
    {"id": 3, "name": "Charlie", "class": "Grade 9", "subject": "Math"},
    {"id": 1, "name": "Alice", "class": "Grade 9", "subject": "Math"},
    {"id": 4, "name": "David", "class": "Grade 11", "subject": "English"},
    {"id": 2, "name": "Bob", "class": "Grade 10", "subject": "Science"},
    ]
unique_set = set()
unique_students = []
for student in students:
    student_tuple = tuple(student.items())
    if student_tuple not in unique_set:
        unique_set.add(student_tuple)
        unique_students.append(student)
print("Unique student entries:")
for student in unique_students:
    print(student)