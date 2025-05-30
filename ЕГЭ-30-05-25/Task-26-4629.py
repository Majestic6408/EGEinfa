with open('26_4629.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices)
shop = sum(prices) - sum(prices[:N // 4]) / 2

prices = sorted(prices, reverse=True)
customer = sum(prices) - sum(prices[:N // 4]) / 2

print(customer, shop)