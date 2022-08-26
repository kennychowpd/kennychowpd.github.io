def main():
    grocery()
    
def grocery():
    print("Shopping List -- leave blank and press enter to exit & print")
    sl = shopping_lst = {}
    while True:
        try:
            item = input().upper()
            if item == "":
                print("Shopping List\n-------------\nUnit | Item    ")
                for key, value in sl.items():
                    print(f"{value}      {key}")                     
                print("-------------")
                break
            else:
                sl[item] += 1
        except KeyError:
            sl[item] = 1
            
            
main()