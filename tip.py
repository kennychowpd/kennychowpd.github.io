def main():
    meal_cost = str(input("How much was the meal? "))
    percent_tip = str(input("What percentage would you like to tip? "))
    tip = dollar_to_float(meal_cost) * percent_to_float(percent_tip) / 100
    print(f"Leave: ${tip:.2f}")
    
def dollar_to_float(dollar):
    dollar = float(dollar.strip("$"))
    return dollar
    
def percent_to_float(percent):
    percent = float(percent.strip("%"))
    return percent


main()