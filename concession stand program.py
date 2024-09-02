# concession stand program
import time
menu = {"pizza": 3.00, "hamburger": 2.00, "fries": 1.50, "soda": 1.00, "popcorn": 5.00}

cart = []
total = 0


print("----- WELCOME TO THE CONCESSION STAND -----")
for key, value in menu.items():
    print(f"{key:10}: ${value}")   
print("---------------------------------------------")

while True:
    food = input ("enter a food item (q to quit): ")

    if food.lower() == "q":
        print("quitting...")
        break
    elif menu.get (food) is not None:
        cart.append(food)
    else:
        print("that item is not on the menu")
        continue


output_width = 35


print ("----- YOUR CART -----")
for food in cart:
    total= total + menu.get(food)
    print(food, end= " ")
time.sleep(3)
print()
print("----------- YOUR TOTAL ----------")
total_amount = f"${total:.2f}"
print(total_amount.center(output_width))

quit()



     