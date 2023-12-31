# for x in range(2):
#     print("XXXXX")
#     for y in range(1):
#         print("XX")
# print("XX")

numbers = [5, 2, 5, 2, 2]
numbers = [2, 2, 2, 2, 5]
for number in numbers:
    for i in range(number):
        print("X", end="")
    print("")

# numbers = [5, 2, 5, 2, 2]
# for number in numbers:
#     x = ""
#     for i in range(number):
#         x += "X"
#     print(x)