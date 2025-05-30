with open('26_4660 (1).txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices)
shop= sum(prices) - sum(prices[:N // 4]) / 2

prices = sorted(prices, reverse=True)
customer = sum(prices) - sum(prices[3::4]) / 2

print(customer, shop)