import sys

loc = 0

try:
    with open (sys.argv[1], "r") as file:
        if len(sys.argv) > 2:
                print("Too many command-line arguments")
                sys.exit()
        if not sys.argv[1].endswith(".py"):
                print("Not a Python file")
                sys.exit()
        for row in file:
                if not row.strip().startswith("#") and row != "\n":
                    loc += 1
except FileNotFoundError:
    print("File does not exist")
    sys.exit()
except IndexError:
    print("Too few command-line arguments")
    sys.exit()
    
print(loc)