# Countdown Timer Program
import  time


my_time = int(input("Enter the time in seconds: "))

for i in range(my_time, 0, -1):
    sec = i % 60
    minute = int (i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minute:02}:{sec:02}")
    time.sleep(1)

print("Times Up!")
