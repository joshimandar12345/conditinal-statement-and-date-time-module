city = input("enter your city name:")
temp = float(input("enter today's temperature in C:"))

if temp > 35:
    print("warning: it is very hot today!")  

if temp > 25:
    print("great day to go outside!")



if temp > 35:
        print("weather: scorching hot")
elif temp > 25:
        print("weather: warm and sunny")
elif temp > 15:
        print("weather: cool and breezy")
else:
        print("weather: cold - stay warm!")


import datetime
import calendar

now = datetime.datetime.now()
print("city:", city)
print("current date and time:", now)

print(calendar.calendar(now.year))
