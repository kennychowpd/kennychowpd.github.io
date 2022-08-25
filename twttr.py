def main():
    user_input = input("Type something: ")
    lst_vowels = ["a", "e", "i", "o", "u"]
    lst_vowels.extend(list("".join(lst_vowels).upper()))
    omit_vowels(user_input, lst_vowels)

def omit_vowels(text, omit_letters):
    for letter in text:
        if letter in omit_letters:
            text = text.replace(letter, "")
    print(text)
    
main()
    