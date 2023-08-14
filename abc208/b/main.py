P = int(input())

coins = [1]

for i in range(0, P - 1):
    coin = (i + 2) * coins[i]
    if coin > P:
        break
    coins.append(coin)

count = 0

for j in range(len(coins) - 1, -1, -1):
    if P >= coins[j] and P > 0:
        paidNum = P // coins[j]
        count += paidNum
        P -= paidNum * coins[j]

    elif P <= 0:
        break

print(count)
