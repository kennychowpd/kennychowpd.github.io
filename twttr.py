def main():
    user_input = input("Type something: ")
    shorten(user_input)

def shorten(word):
    lst_vowels = ["a", "e", "i", "o", "u"]
    lst_vowels.extend(list("".join(lst_vowels).upper()))
    for letter in word:
        if letter in lst_vowels:
            word = word.replace(letter, "")
    print(word)

if __name__ == "__main__":    
    main()
    