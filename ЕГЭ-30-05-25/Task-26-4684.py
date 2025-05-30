with open('26_4684.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices)
shop = sum(prices) - sum(prices[:N // 6]) / 2

prices = sorted(prices, reverse=True)
customer = sum(prices) - sum(prices[5::6]) / 2

print(customer, shop)