balance = 0

def main():
    print(balance)
    deposit(100)
    withdraw(50)
    print(balance)
    
def deposit(b, n):
    global balance
    balance += n


def withdraw(b, n):
    global balance
    balance -= n
    
    
if __name__ == "__main__":
    main()