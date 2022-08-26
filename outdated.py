
def main():
    
    print(frmat_date())
    
def frmat_date():
    lst_month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]
    while True:
        try:
            user_input = input("Date: ")
        except ValueError:
            pass
        else:
            if "/" in user_input:
                date = user_input.split("/")
                if int(date[0]) > 12 or int(date[1]) > 31:
                    print("Wrong input, try again with the US style.")
                    continue
                if len(date[0]) == 1:
                    date[0] = "0" + date[0]
                if len(date[1]) == 1:
                    date[1] = "0" + date[1]
                return f"{date[2]}-{date[0]}-{date[1]}"
            if "," in user_input:
                date = user_input.replace(",", "").split(" ")
                if date[0] not in lst_month or int(date[1]) > 31:
                    
                    print("Wrong input, try again with the US style.")
                    continue
                return f"{date[2]}-{lst_month.index(date[0])+ 1}-{date[1]}"
        

main()