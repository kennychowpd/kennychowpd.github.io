def main():
    user_input = input("What is the Answer to the Great Question Of Life, the Universe and Everything? ").lower()
    correct_answer = ["42", "forty-two", "forty two"]
    if user_input in correct_answer:
        print("Yes")
    else:
        print("No")
        
        
main()