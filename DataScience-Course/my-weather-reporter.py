city = input("Enter the city name: ")
temperature = float(input("Enter the temperature in Celsius: "))

if temperature > 35:
    print("Warning: It is very hot outside")

if temperature > 25:
    print("Great day to go outside")
else:
    print("Grab a jacket before you go out")

if temperature > 35:
    print("Scorching Hot")
elif temperature > 25:
    print("Warm and Sunny")
elif temperature > 15:
    print("Cool and Breezy")
else:
    print("Cold")

import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Current Date and Time:", now)

print(calendar.calendar(now.year))