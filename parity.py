def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
def is_even(num):
    return True if num % 2 == 0 else False

main()