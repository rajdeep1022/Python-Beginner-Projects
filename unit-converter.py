# Python Weight Converter

weight = float(input("Enter your weight?: "))
unit = input("Kilograms or Pounds? (kg or lb): ")

if unit == "kg":
    weight = weight * 2.205
    unit = "lbs."
elif unit == "lb":
    weight = weight / 2.205
    unit = "kgs."
else:
    print("Enter a valid unit")

print(f"Your weight is: {round(weight, 1)} {unit}")
