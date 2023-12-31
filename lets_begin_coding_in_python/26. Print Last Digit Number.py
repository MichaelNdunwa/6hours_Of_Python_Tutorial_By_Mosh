
def print_last_digit(number):
    last_digit = str(number)
    print(f"{last_digit[-1]}", end = "")
    return last_digit[-1]


print_last_digit(-12345)
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)