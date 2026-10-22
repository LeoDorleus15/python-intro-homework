age = int(input("Please enter your age: "))

if age >=65:
    print("You're a senior citizen!")
elif age >= 18 and age <= 64:
    print("You're an adult!")
elif age >= 13 and age <= 17:
    print("You're a teenager!") 
else:
    print("You're a child!")