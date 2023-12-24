import datetime

age = int(input("How old are you? "))
today = datetime.date.today()
birth_year = today.year - age
print("You were born in the year " + str(birth_year))
print(type(age))
print(type(today))
print(type(birth_year))