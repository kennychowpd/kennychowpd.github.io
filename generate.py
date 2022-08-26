import random

coin = random.choice(["Head", "Tail"])
print(coin)
num = random.randint(1, 100)
print(num)
cards = ["Jack", "Queen", "King"]
for _ in range(10):
    random.shuffle(cards)
    print(cards[0])
