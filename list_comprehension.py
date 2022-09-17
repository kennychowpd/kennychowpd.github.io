# list comprehension
# list of dict -> list
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    ]

good_students = [
    student["name"] for student in students if student["house"] == "Gryffindor"
    ]

for student in sorted(good_students):
    print(student)
    
# list comprehension
# list -> list of dict
student_n1 = ["Hermione", "Harry", "Ron"]

main_char1 = [{"name": student, "house": "Gryffindor"} for student in student_n1]

print(main_char1)


# dict comprehension
# list -> dict
student_n2 = ["Hermione", "Harry", "Ron"]

main_char2 = {student: "Gryffindor" for student in student_n2}

print(main_char2)
