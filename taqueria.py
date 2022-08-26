def main():
    dic_menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    order(dic_menu)
    
    
def order(menu):
    order_value = 0
    ordered_items = []
    while True:
        try:
            print(
                "Enter item name to add item to the cart.\nLeave blank to finish order."
                )
            order = input("Item: ").title()
            if order == "":
                print("Your Order:")
                for i in ordered_items:
                    print(i)
                print(
                    f"Your Grand Total is: ${order_value}\nPlease insert your student ID card for payment."
                    )
                break
            else:
                order_value += menu[order]
                ordered_items.append(order)
        except KeyError:
            pass
        else:
            print(f"Total: ${order_value}")
        
        
main()