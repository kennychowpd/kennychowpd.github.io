def main():
    
    print(calculate_fuel("Fuel(in fraction): "))
    

def calculate_fuel(prompt):
    while True:
        try:
            user_input = input(prompt)
            f = fraction = user_input.split("/")
            percentage = round(int(f[0]) / int(f[1]) * 100)
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{percentage}%"
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except IndexError:
            pass
        
main()
            
        
        