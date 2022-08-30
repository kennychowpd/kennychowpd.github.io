def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str):
    digit_counter = 0
    # contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if 2 <= len(str) <= 6:
        # must start with at least two letters.
        if str[0].isalpha() and str[1].isalpha():
            # No periods, spaces, or punctuation marks are allowed.
            lst_not_allowed = [".", " ", ","]
            for i in str:
                if i in lst_not_allowed:
                    return False
                # The first number used cannot be a ‘0’.”
                elif i.isdigit():
                    i = int(i)
                    if i != 0:
                        digit_counter += 1
                    elif i == 0 and digit_counter == 0:
                        return False
            # “Numbers cannot be used in the middle of a plate; they must come at the end.
            # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
            end_char = list(str).pop()
            if digit_counter > 0 and not end_char.isdigit():
                return False
            return True    
                
    else:
        return False


if __name__ == "__main__":    
    main()
