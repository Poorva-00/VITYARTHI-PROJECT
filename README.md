# VITYARTHI-PROJECT

---

PROJECT TITLE: ONLINE FOOD DELIVERY SYSTEM

---

OVERVIEW OF PROJECT:

In the digital era, food delivery applications have become increasingly popular due to convenience and time-saving features. This project aims to design a simple, user-friendly console-based Food Delivery System generator using Python.

---

FEATURES:

The system allows users to:
* Enter the name and address of the user
* View the menu
* Place an order
* Calculate bill
* Track delivery status
  
---

TECHNOLOGIES USED/TOOLS USED:

Programming Language: Python 3.x

Libraries Used: time

IDE/Environment: VS Code

---

STEPS TO INSTALL AND RUN THE PROJECT:

1. Install Python

* Go to the official Python website: https://www.python.org/downloads/
* Download the latest Python version (3.x).
* During installation, tick the checkbox: Add Python to PATH
* Complete the installation.


2. Create a Project Folder

* Create a new folder on your computer
* Inside this folder, create the following Python files:

main.py,
menus.py,
order.py,
cart.py,
details.py,
order_status.py,
bill.py,
exit.py,

3. Open the Project in VS CODE

4. Verify All Files Are in the Same Folder

5. Run the Project by opening main.py and Click the Run button at top right or press Ctrl + F5

---

INSTRUCTIONS FOR TESTING:

To verify that the Online Food Ordering System works correctly, follow the steps below. These steps ensure every module, input, and output is tested properly.


1. Launch the Program

Open the project folder in VS CODE and run main.py

Expected Result:
The system should display the header “ONLINE FOOD DELIVERY INVOICE” and show the full food menu in tabular format.


2. Test Customer Details

Enter any name and address.

Expected Result:
System must save both and proceed to order status simulation.


3. Test Menu Display

Verify that:

All items (Pizza, Pasta, Momos, etc.) appear in the menu, All prices are correct, Formatting is aligned

If any item is missing, the menu dictionary may be incorrect.


4. Test Order Input

Case A: Entering a valid food item

Type:
Pizza

Enter a quantity (e.g., 2)

Expected Result:
Item should be added to the cart.

Case B: Entering an invalid food item

Type:
Burger

Expected Result:
System should show: “Item not available. Try again!”
No crash should occur.

Case C: Multiple items

Enter 3 or more items one by one.

Expected Result:
All items must be stored in the cart.


5. Test Completing the Order

Type: done

Expected Result:
It should stop taking input 


6. Test Order Status Simulation

Verify the program prints these messages with a short delay:

Order placed

Order prepared

Out for delivery

Expected Result:
Messages appear one by one with 1-second gaps.


7. Test Billing Calculation

Check whether:

Each ordered item is printed with quantity, Delivery charge is added, Total amount is correct


8. Test Empty Cart Handling

Start the program again and immediately type:

done

Expected Result:
System should display:
“No items ordered. Exiting”
and close safely without errors.

9. Verify Final Output

Check that the final Order Summary shows:

✔ Customer name
✔ Address
✔ All ordered items with quantities
✔ Item total
✔ Delivery charge
✔ Final bill amount

---

SCREENSHORTS OF OUTPUT:

<img width="740" height="436" alt="image" src="https://github.com/user-attachments/assets/d8199b2c-9c9d-4309-a843-26e7a645e74c" />
<img width="740" height="208" alt="image" src="https://github.com/user-attachments/assets/e3e629fa-5ae4-4fc8-8913-f2368966ad38" />

---


