def main():

    name = input("name: ")
    hello()
    hello(name)
    


def hello(name="World"):
    print(f"hello, {name}")
    
    
main()
        