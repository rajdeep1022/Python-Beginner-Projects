# Python Temperature Converter °

unit = input("Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the Temperature: "))
Unit = unit.capitalize()
if Unit == "C":
    temp = round((9*temp)/5 + 32, 1)
    print(f"Your temperature is: {temp} °F")
elif Unit == "F":
    temp = round((temp - 32)* 5 / 9, 1)
    print(f"Your temperature is: {temp} °C")
else:
    print(f"{Unit} isn't a valid unit")
