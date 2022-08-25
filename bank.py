def main():
    
    user_input = input("Greet me! ").strip().lower()
    
    promise = payout(user_input)
    
    print(promise)
    

def payout(text):
    if text.startswith("hello"):
        return "$0"
    elif text.startswith("h"):
        return "$20"
    else:
        return "$100"
        
        
main()