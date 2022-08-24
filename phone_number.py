def main():
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(create_phone_number(n))

def create_phone_number(n):
    print(n)
    a = ''.join(map(str, str(n)))
    print(a)
    phone_number = f"({n[0:3]}) {n[3:6]}-{n[6:]}"
    return phone_number

main()