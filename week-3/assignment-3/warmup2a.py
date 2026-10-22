year = input("Please enter the year you were born: ")
age = 2023 - int(year)

if age >= 65:
    print("You're a senior citizen!")
elif age >= 18 and age <= 64:
    print("You're an adult!")
elif age >= 13 and age <= 17:
    print("You're a teenager!") 
else:
    print("You're a child!")