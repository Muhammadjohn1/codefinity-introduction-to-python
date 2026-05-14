#Returns the price after applying the discount
def apply_discount(price, discount =0.05):
    discount_price = price * (1 - discount)
    return discount_price
#Returns the price after adding the tax
def apply_tax(price, tax=0.07):
    after_add_tax = price * (1+tax)
    return after_add_tax

#return the total price with both discount and tax applied.
def calculate_total(price, discount=0.05, tax=0.07):
    total = price * (1+tax) * (1-discount)
    return total

total_price_default = calculate_total(120, discount=0.05, tax=0.07)
print(f"Total cost with default discount and tax: ${total_price_default:.2f}")
total_price_custom = calculate_total(100, discount = 0.10, tax = 0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom:.2f}")