def total(gold, silver, copper):
    return (gold * 17 + silver) * 29 + copper


coins1 = [100, 50, 25]
coins2 = {"gold": 100, "copper": 25, "silver": 50}

print(total(*coins1), "copper coins") # unpacking list with * orderly
print(total(**coins2), "copper coins")  # unpacking dict with ** with keys
