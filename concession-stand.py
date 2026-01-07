#Concession stand program

menu = {"pizza" : 300,
        "nachos" : 150,
        "popcorn" : 300,
        "fries" : 250,
        "chips" : 100,
        "pretzel" : 350,
        "soda" : 110,
        "lemonade" : 150 }
cart = []
total = 0

print("---------Menu---------")
for key, value in menu.items():
    print(f"{key:10} : {value}")
print("------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("--------- YOUR ORDER -------------")
for food in cart:
    total += menu.get(food)
    print(food.upper(), end="\n")

print()
print(f"Your total is: {total} ")
