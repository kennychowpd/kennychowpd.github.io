def main():
    fraction = input("Fuel(in fraction): ")
    percentage = convert(fraction)
    
def convert(fraction):
    while True:
            f = fraction.split("/")
            percentage = round(int(f[0]) / int(f[1]) * 100)
            if percentage > 100:
                raise ValueError
                break
            return percentage
        

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
    

if __name__ == "__main__": 
    main()
