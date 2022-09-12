# list comprehension
# dict -> list
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
    

# list -> dict
student_n = ["Hermione", "Harry", "Ron"]

main_char = [{"name": student, "house": "Gryffindor"} for student in student_n]

print(main_char)