import csv

people = []
name = input("What is your name? ")
age = int(input("What is your age? "))
home = (input("Where do your live? "))

with open("people.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "home"])
    writer.writerow({"name": name, "age": age, "home": home})
    
with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        people.append(row)

for person in sorted(people, key=lambda person: person["name"]):
    print(f"{person['name']} is {person['age']} years old and lives in {person['home']}.")