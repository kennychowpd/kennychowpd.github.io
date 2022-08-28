lst_name = []
while True:
    try:
        user_input = input("Name: ")
        lst_name.append(user_input)
    except EOFError:
        if len(lst_name) == 1:
            print(f"\nAdieu, adieu to {lst_name[0]}")
        elif len(lst_name) >= 2:
            except_last_input = ", ".join(lst_name[:-1])
            print(f"\nAdieu, adieu to {except_last_input} and {lst_name[-1]}")
        break