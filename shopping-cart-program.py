# Shopping Cart Program
from sympy.codegen import Print

foods = []
prices= []
total = 0

while True:
    food = input("Enter a food to buy ( 'q' to quit' ): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food} : $ "))
        foods.append(food)
        prices.append(price)

print("-----YOUR FOODS-----")
for food in foods:
    print(food)

for price in prices:
    total += price


print()
print(f"Total price is ${total}")
