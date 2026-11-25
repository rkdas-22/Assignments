# Unit 2 - Q5: Coin Change Problem (Minimum number of coins, Dynamic Programming)

def min_coins(coins, amount):
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] != INF else -1


def main():
    coins = [int(x) for x in input("Enter coin denominations (comma separated): ").split(",")]
    amount = int(input("Enter the target amount: "))
    result = min_coins(coins, amount)
    if result == -1:
        print("It is not possible to make this amount with the given coins.")
    else:
        print(f"Minimum number of coins required: {result}")


if __name__ == "__main__":
    main()
