def main():
    user_input = str(input("How are you feeling? "))
    print(convert(user_input))
    
def convert(input):
    if ":)" in input:
        input = input.replace(":)", "🙂")
    if ":(" in input:
        input = input.replace(":(", "🙁")
    return input
    
    
main()