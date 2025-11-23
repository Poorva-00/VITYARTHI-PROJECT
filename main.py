from menus import food_menu,menu
from order import take_order
from cart import calculate
from details import details
from order_status import status
from bill import billing
from exit import empty

name, address = details()
print("          MENU          ")
food_menu()
cart = take_order(menu)
empty(cart)
total, delivery, total_price = calculate(menu, cart)
billing(name,address,cart,menu,delivery,total,total_price)
status()
