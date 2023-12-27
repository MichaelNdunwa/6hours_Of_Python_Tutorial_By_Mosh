
weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ").lower()
if unit == "l":
    kg = weight * 0.45
    print(f"You're {kg} kilos.")
elif unit == "k":
    pounds = weight / 0.45
    print(f"You're {pounds} pounds.")
