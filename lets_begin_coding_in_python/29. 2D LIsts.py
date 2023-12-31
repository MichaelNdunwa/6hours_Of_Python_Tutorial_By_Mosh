
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        if item != row[-1]:
            print(f"{item}, ", end="")
        else:
            print(f"{item}", end="")
    print("")