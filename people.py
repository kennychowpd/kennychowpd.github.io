import csv

people = []

with open("people.csv", "a") as file:
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    home = (input("Where do your live? "))

    file.write(f"{name},{age},{home}\n")
    
with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        person = {"name": row["name"], "age": row["age"], "home": row["home"]}
        people.append(person)
        
def get_name(person):
    return person["name"]


for person in sorted(people, key=lambda person: person["name"]):
    print(f"{person['name']} is {person['age']} years old and lives in {person['home']}.")