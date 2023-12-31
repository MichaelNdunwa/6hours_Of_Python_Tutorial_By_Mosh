def find_largest_number(numbers):
    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return largest_number


print(find_largest_number([1, 2, 5, 5, 9, 2]))
