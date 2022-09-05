class Vault:
    def __init__(self, gold=0, silver=0, copper=0):
        self.gold = gold
        self.silver = silver
        self.copper = copper
    
    def __str__(self):
        return f"{self.gold} golds, {self.silver} silver, {self.copper} copper"

    def __add__(self, other):
        gold = self.gold + other.gold
        silver = self.silver + other.silver
        copper = self.copper + other.copper
        return Vault(gold, silver, copper)
    
    
citi = Vault(100, 150, 250)
print(citi)

sc = Vault(20, 33, 560)
print(sc)

total = citi + sc
print(total)