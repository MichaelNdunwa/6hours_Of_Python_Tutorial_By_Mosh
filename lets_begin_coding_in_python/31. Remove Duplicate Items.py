numbers = [5, 1, 5, 5, 2, 3, 2, 4, 4, 1]


def remove_duplicate(numbers):
    for number in numbers:
        if numbers.count(number) > 1:
            numbers.remove(number)
    print(numbers)


def remove_duplicate2(numbers):
    new_numbers = []
    for number in numbers:
        if number not in new_numbers:
            new_numbers.append(number)
    print(new_numbers)

remove_duplicate(numbers)
remove_duplicate2(numbers)

print("")
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
remove_duplicate2(numbers)
remove_duplicate(numbers)
