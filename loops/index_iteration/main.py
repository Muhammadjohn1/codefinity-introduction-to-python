prices = [29.99, 45.50, 12.75, 38.20]

for i in range(len(prices)):
    if i == 0:
        discount = 0.10
    elif i == 1:
        discount = 0.20
    elif i == 2:
        discount = 0.15
    elif i == 3:
        discount = 0.05
    new_price = prices[i] * (1 - discount)
    prices[i] = new_price
    print(f"Updated price for item {i}: ${new_price:.2f}")
