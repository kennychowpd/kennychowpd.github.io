def main():
    num = get_number()
    meow(num)
    return
    
    
def get_number():
    while True:
        num = int(input("how many times? "))
        if num > 0:
            return num

def meow(n):
    for _ in range(n):
        print("Meow!")
    
main()