
while True:
    with open('coin.txt', 'r') as file:
        coin = file.readlines()

        user_input = input("Throw the coin and enter head or tail here: ") + "\n"
        coin.append(user_input)

        with open('coin.txt', 'w') as file:
            file.writelines(coin)

    heads = coin.count('head\n')
    tails = coin.count('tail\n')
    percentage_h = heads / len(coin)*100
    percentage_t = tails / len(coin)*100

    print(f"Heads: {round(percentage_h, 2)}%")
    print(f"Tails: {round(percentage_t, 2)}%")

