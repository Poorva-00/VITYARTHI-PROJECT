def calculate(menu,cart):
    total = 0

    for item, qty in cart.items():
        total += menu[item]*qty
        delivery_price = 30
        total_price = total + delivery_price

    return total,delivery_price,total_price

