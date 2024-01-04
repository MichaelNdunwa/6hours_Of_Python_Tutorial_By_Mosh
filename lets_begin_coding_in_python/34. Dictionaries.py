numbers = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

# print(numbers.get(0, "not the"))
phone_number = input("Phone: ")
words = ""
for number in phone_number:
    words += numbers.get(number, "!") + " "
print(words)