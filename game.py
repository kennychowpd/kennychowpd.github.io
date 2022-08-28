import random

while True:
    try:
        level = int(input("Level: "))
        if level > 1:
            correct_num = random.randrange(1, level)
            while True:
                guess = int(input("Guess: "))
                if guess > correct_num:
                    print("Too large!")
                elif guess < correct_num:
                    print("Too small!")
                else:
                    break
        print("Just right!")
        break
    except ValueError:
        pass