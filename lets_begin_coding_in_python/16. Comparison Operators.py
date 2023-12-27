
# if name is less than 3 characters long
#     name must be at least 3 characters
# otherwise if it's more than 50 characters long
#     name can be a maximum of 50 characters
# otherwise
#     name looks good!

name = input("What's your name? ")
name_length = len(name)
if name_length <= 3:
    print(f"'{name}' must be at least 3 characters")
elif name_length >= 50:
    print(f"'{name}' can be a maximum of 50 characters.")
else:
    print(f"'{name}' looks good!")