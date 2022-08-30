def main():
    
    user_input = input("Greet me! ").strip().lower()
    
    promise = value(user_input)
    
    print(promise)
    

def value(greeting):
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"
        
if __name__ == "__main__":
    main()