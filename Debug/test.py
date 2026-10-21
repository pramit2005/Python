def calculate_discount(price, discount):
    discounted_price = price * discount
    return discounted_price


def calculate_total(price, quantity, discount):
    subtotal = price * quantity
    total = calculate_discount(subtotal, discount)
    return total


price = 100
quantity = 3
discount = 10

result = calculate_total(price, quantity, discount)
print(result)