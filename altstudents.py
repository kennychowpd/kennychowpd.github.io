students = [
    {"name": "Adore", "house": "B house", "color": "red"},
    {"name": "Kenny", "house": "A house", "color": "blue"},
    {"name": "Ron", "house": None, "color": "darkness"}
]

for student in students:
    print(student["name"], student["house"], student["color"], sep=",")