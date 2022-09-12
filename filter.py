students = [
    {"'name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


def is_main_char(c):
    return c["house"] == "Gryffindor"


main_char = filter(is_main_char, students)

for char in main_char:
    print(char["name"])
