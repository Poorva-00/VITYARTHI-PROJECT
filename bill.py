def billing(name,address,cart,menu,delivery,total,total_price):
    
    print("----------- ORDER SUMMARY------------------")
    print("Customer name: ",name)
    print("Address: ",address)
    for food,qty in cart.items():
        print(f"{food} X {qty} = {menu[food]*qty}" )
    print("Delivery charge: ",delivery)
    print("Total amount: ",total_price)
    print("--------------------------------------------")


