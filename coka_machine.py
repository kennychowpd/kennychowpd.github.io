acceptable_coins = [5, 10, 25]
price_coke = 50
inserted_coins = 0
while True:
    user_input = int(input("🪙 Please insert a coin(in cents): "))
    if user_input in acceptable_coins:
        inserted_coins += user_input
        if inserted_coins >= 50:
            change = inserted_coins - price_coke
            print(
                f"Change owed: {change}\n
                🥤 Here is your Coke!"
                )
            break
        if inserted_coins < 50:
            due = price_coke - inserted_coins
            print(
                f"Amount due: {due}\n
                🖕🏼 We got no Coke for you yet, you poor bastard!"
                )
            continue
    elif user_input == 50:
        print(
            f"🔫 HAHA, you think you funny chingga? Ain't no one fuck with {user_input}CENTS"
            )
    else:
        print(
            f"🤬 There is no {user_input} cents, are you out of your damn mind?"
            )