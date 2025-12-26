# Python Temperature Converter °

unit = input("Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the Temperature: "))
UNIT = unit.capitalize()
if UNIT == "C":
    temp = round((9*temp)/5 + 32, 1)
    print(f"Your temperature is: {temp} °F")
elif UNIT == "F":
    temp = round((temp - 32)* 5 / 9, 1)
    print(f"Your temperature is: {temp} °C")
else:
    print(f"{UNIT} isn't a valid unit")
