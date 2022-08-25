def main():
    user_input = input("What time is it?: ")
    c_time = convert(user_input)
    ck_time(c_time)

    
    
def convert(time):
    time = time.split(":")
    return float(".".join(time))
    
    
def ck_time(c_time):
    if c_time % 1 > 0.60 or c_time > 24:
        print("Are you Dumb or a time manipulator?")
    else:
        if 8 >= c_time >= 7:
            print("It's BREAKFAST TIME!!!") 
        elif 13 >= c_time >= 12:
            print("It's LUNCH TIME!!") 
        elif 19 >= c_time >= 18:
            print("It's DINNER TIME!") 
            
main()