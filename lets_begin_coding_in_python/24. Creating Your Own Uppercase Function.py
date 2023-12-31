def uppercase(str):
    str = str + '\n'
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            print(f"{chr(ord(str[i]) - 32)}", end="")
        else:
            print(f"{str[i]}", end="")


uppercase("michael")
