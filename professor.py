import random


def main():
    lvl = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        crrct_answr = x + y
        chnc = 0
        while chnc < 3:
            answr = int(input(f"{x} + {y} = "))
            if answr == crrct_answr:
                score += 1
                break
            else:
                print("EEE")
                chnc += 1
                if chnc == 3:
                    print(f"{x} + {y} = {crrct_answr}")
                    break

    print(f"Score: {score}")


def get_level():
    while True:
        lvl = int(input("Level: "))
        if lvl not in [1, 2, 3]:
            pass
        else:
            return lvl


def generate_integer(lvl):
    uppr_rng = (10**lvl) - 1
    return random.randrange(1, uppr_rng)


if __name__ == "__main__":
    main()
