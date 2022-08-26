def main():
    dic_fruit = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
        }
    
    user_input = input("Item: ").lower()
    if user_input in dic_fruit:  
        print(f"Calories: {calories(user_input, dic_fruit)}")
    
    
    
def calories(fruit, dic_fruit):
        return dic_fruit[fruit]
    
main()
    
    