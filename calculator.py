# Start of mai
def main():

    x = float(input("x: "))
    y = float(input("y: "))

    z = round((x + y) / 2, 4)
    a = add_three(z)

    print(f"{z} plus 3 is {a}.")


# End of main
# Start of functions
def add_three(num):
    num += 3
    return num


main()
