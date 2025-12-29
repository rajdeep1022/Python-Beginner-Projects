# Python Compound Interest Calculator

while True:
    principle = float(input("Enter the principle: "))
    if principle < 0:
        print("Principle cannot be negative")
    else:
        break
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate cannot be negative")
    else:
        break
while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time cannot be negative")
    else:
        break


total = principle * pow((1 + rate/100), time)
print(f"Total interest is: {round (total)}")
