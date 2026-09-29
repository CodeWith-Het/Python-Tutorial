# Q1. Accept two numbers and print the greatest between them.
# ! answer 
# num1 = int(input("Enter the number 1: "))
# num2 = int(input("Enter the number 2: "))

# if num1>num2:
#     print(f"{num1} is greatest {num2}")
# elif num2>num1:
#     print(f"{num1} is greatest {num1}")
# else:
#     print("invalid number")

# Q2. Accept the gender from the user as char and print the
# respective greeting message
# Ex - Good Morning Sir (on the basis of gender)
# ! answer
# gender = input("Enter the gender:")

# if gender=="M" or gender=="m":
#     print("Good moring sir")
# elif gender=="F" or gender=="f":
#     print("Good morning maam")
# else:
#     print("invliad gender")

# Q3. Accept an integer and check whether it is an even number
# or odd.
# ! answer
# num = int(input("Enter the number: "))

# if num%2==0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# Q4. Accept name and age from the user. Check if the user is a
# valid voter or not.
# Ex- “hello shery you are a valid voter”
# ! answer
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# if age>=18:
#     print(f"hello {name} you are a valid voter")
# else:
#     print(f"hello {name} your are not valid voter")

# Q5. Accept a year and check if it a leap year or not (google to
# find out what is a leap year)
# ! answer
# year = int(input("Enter the year: "))

# if year%100==0 and year%400==0:
#     print(f"{year} is leap year")
# elif year%100!=0 and year%4==0:
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")

# @ take the input of temperature in celsiusX
# @ Below 0°C → "Freezing Cold"
# @ 0°C to 10°C → "Very Cold"
# @ 10°C to 20°C → "Cold"
# @ 20°C to 30°C → "Pleasant"
# @ 30°C to 40°C → "Hot"
# @ Above 40°C → "Very Hot"

# temp = int(input("Enter the temp in celsius: "))

# if temp<0:
#     print("Freezing cold")
# elif temp>=0 and temp<10:
#     print("Very cold")
# elif temp>=10 and temp<20:
#     print("Cold")
# elif temp>=20 and temp<30:
#     print("Pleasnt")
# elif temp>=30 and  temp<40:
#     print("Hot")
# else:
#     print("Very Hot")