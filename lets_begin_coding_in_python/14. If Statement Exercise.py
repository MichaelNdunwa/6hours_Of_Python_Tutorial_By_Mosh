# Price of a house is $1M
# If buyer has good credit,
#   they need to put down 10%
# Otherwise
#   they need to put down 20%
# Print the down payment.

goodCredit = input("Do you have good credit, Yes(Y) or No(N): ").upper()
# yes =
if goodCredit == "Y":
    goodCredit = True
else: goodCredit = False

# Calculation time:
price = 1_000_000
if goodCredit:
    down_payment = "{:,}".format(price * 0.1)
else:
    down_payment = "{:,}".format(price * 0.2)
print(f"Down payment: ${down_payment}")