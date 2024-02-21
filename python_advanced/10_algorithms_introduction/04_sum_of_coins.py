def choose_coins(coins, target):
    coins.sort(reverse=True)
    index = 0
    coins_info = {}

    while target > 0 and index < len(coins):
        count = target // coins[index]
        target %= coins[index]
        if count > 0:
            coins_info[coins[index]] = count

        index += 1
    if target != 0:
        return 'Error'
    else:
        result = f"Number of coins to take: {sum(coins_info.values())}\n"
        for value, count in coins_info.items():
            result += f"{count} coin(s) with value {value}\n"

        return result


coins = list(map(int, input().split(", ")))
target = int(input())
print(choose_coins(coins, target))