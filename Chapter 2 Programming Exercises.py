

#Male and Female Percentages

male=int(input("How many males ? "))
female=int(input("How many females ? "))

class_total=(male + female)

male_ratio=(male / class_total) * 100
female_ratio=(female / class_total) * 100

print(f"The class is {male_ratio}% male and {female_ratio}% female.")


#Ingredient Adjuster

cookies=float(input("How many cookies do you want ? "))
sugar=(cookies * 1.5) /48
butter=(cookies * 1) /48
flour= (cookies * 2.75) /48

print(f"For {cookies}, you need {sugar} cups of sugar, {butter} cups of butter and {flour} cups of flour.")



#1. Personal Information
name="Wolfio"
address="117 Clews street, Pawtucket RI 02861"
cellnum="401 660 6586"
major="Computer Science"

print(f"{name}, {address}, {cellnum}, {major}")


#Sales Prediction
projected=float(input("What is the projected amount of total sales ?"))
profit= projected * 0.23
print(profit)

#Land Calculation
totalLand = input("Enter land calculation: ")
landCal = float(totalLand) / 43560
print(landCal)

#Total Purchase

item_1=float(input("What is the price of item 1 ? "))
item_2=float(input("What is the price of item 2 ? "))
item_3=float(input("What is the price of item 3 ? "))
item_4=float(input("What is the price of item 4 ? "))
item_5=float(input("What is the price of item 5 ? "))

subtotal=(item_1 + item_2 + item_3 + item_4 + item_5)
print(f"Subtotal is {subtotal}")

print("Sub total is taxed at 7% ")

total=subtotal - subtotal * 0.07
print(f"Total is {total}")

#Distance Traveled

six_hours= 70 * 6
ten_hours= 70 * 10
fifteen_hours= 70 * 15

print(f"The car will drive {six_hours} miles in 6 hours .")
print(f"The car will drive {ten_hours} miles in 10 hours .")
print(f"The car will drive {fifteen_hours} miles in 15 hours .")

#Sales Tax

purchase=input(float(" What is the purchase amount ?"))
state_tax= purchase * 0.05
county_tax= purchase * 0.025

print(purchase)
print(state_tax)
print(county_tax)
print (state_tax + county_tax)
print(purchase + state_tax + county_tax)

#7 miles per gallon

miles=input("How far have you driven ? ")
gas=input("How much gas have you used ? ")
miles_per_gas= miles / gas

print(miles_per_gas)

#Tip, Tax and Total

charged=input("How much was the food ?")

tip=charged * 0.18
tax=charged * 0.07
total=charged + tax + tip
print(f" Tip amount = {tip}")
print(f" Tax amount = {tax}")
print(f" Subtotal = {charged}")
print(f" Total = {total}")


#Celsius to Fahrenheit Temperature Converter
celsius= input("What is the temperature in Celsius ?")
fahrenheit= celsius * 9 / 5 + 32
print(f"The temperature in Fahrenheit is {fahrenheit}")




