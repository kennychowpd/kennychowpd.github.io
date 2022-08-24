name = input("What is your car? ")

match name:
    case "Tesla Model S" | "Tesla Model 3" | "Tesla Model X" | "Tesla Model Y":
        print("Good Choice.")
    case_:
        print("Think about you life decisions again.")