def main():
    user_input = str(input("Say something quickly: "))
    slow_down(user_input)
    
def slow_down(words):
    words = words.split()
    print(*words, sep="...")
    
main()