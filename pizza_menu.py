import sys
import csv
from tabulate import tabulate


def main():
    table = []
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    if not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit()
        
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
                
            print(tabulate(table, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()
    
            
    
            
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()