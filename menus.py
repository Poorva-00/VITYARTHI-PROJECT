menu = {
    "Pizza"  : 150 , 
    "Fries"  : 120 , 
    "Pasta"  : 130 , 
    "Momos"  : 100 , 
    "Rolls"  : 100 , 
    "Latte"  : 100 ,  
    "Mocha"  : 120 
    }

def food_menu():

    print("--------------------------------")
    print("|   ITEMS      |     PRICE     |")
    print("--------------------------------")

    for item, price in menu.items():       
        print("|",item ,"       |" ,   price, "          |")
    
    print("--------------------------------")


