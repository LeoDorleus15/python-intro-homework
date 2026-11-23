def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


# 1. Only a name argument (uses default greeting)
greet("Leopold")

# 2. Both a name and a custom greeting (positional arguments)
greet("Leopold", "Good morning")

# 3. Greeting passed as a keyword argument
greet("Leopold", greeting="Hello")