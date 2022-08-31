import sys
import csv


students = []

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()
    
if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit()

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            first_name, last_name = row["name"].split(", ")
            house = row["house"]
            students.append({"first": first_name, "last": last_name, "house": house})
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow(student)
except FileNotFoundError:
    print(f"{sys.argv[1]} does not exist")
    sys.exit()
    
         
    
