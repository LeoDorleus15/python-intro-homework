#Traceback (most recent call last):
#  File "/Users/yvettealexandre/Desktop/CodeTheDream/python-intro-homework/week-2/assignment-2/warmup4.py", line 2, in <module>
#    current_year = 2026 - age
#                   ~~~~~^~~~~
#TypeError: unsupported operand type(s) for -: 'int' and 'str'
#yvettealexandre@Yvettes-MBP assignment-2 % 
#I converted the input to an integer to fix the error. The code now works as expected.
age = input("What year were you born? ")
current_year = 2026 - int(age)
print("This year you will be", current_year)