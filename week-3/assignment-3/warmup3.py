print(not True and False)           # False   # not True is False; False and False is False
print(True or False and False)      # True    # False and False evaluates first to False; True or False is True
print(not (5 > 3))                  # False   # 5 > 3 is True; not True is False
print(10 == 10 and 4 != 4)          # False   # 10 == 10 is True, but 4 != 4 is False; True and False is False
print(not False or not True)        # True    # not False is True; True or anything is True