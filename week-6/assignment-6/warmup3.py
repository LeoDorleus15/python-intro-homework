# 1. A variable created inside a function stays in that function's local scope:
def make_note():
    note = "Only inside make_note"


# Trying to print `note` outside raises:
# NameError: name 'note' is not defined
# print(note)


# 2. Returning a value lets you capture it outside the function:
def get_note():
    note = "Returned from get_note"
    return note


saved_note = get_note()
print(saved_note)