
# If Statements

# Temperature,°C	- What might be at this temperature	- How it feels
# 15		        -                                   - Cool
# 20	            - Room indoors	                    - Warm
# 25	            - Warm room	                        - Warm to hot
# 30	            - Hot day	                        - Feeling hot
temperature = float(input("What's the temperature: "))
if temperature > 30:
    print("""It's a hot day \nDrink plenty of water.""")
elif temperature < 15:
    print("""It's a cold day \nWear warm clothes.""")
else:
    print("It's a lovely day.")