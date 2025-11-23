def take_order(menu):
    cart = {}
    while True:
        food = input("\nEnter item name(press done to finish): ").title()  

        if food == "Done":  
            break
        
        if food not in menu:
            print("Item not available. Try again!")
            continue

        qty= int(input("Enter quantity: "))

        cart[food] = cart.get(food, 0)+ qty
        
    return cart