
try:
    age = int(input("Age: "))
    income = 2000
    risk = income / age
    print(age)
except ArithmeticError:
    print("Math Error.")
except ValueError:
    print("Invalid value.")
    