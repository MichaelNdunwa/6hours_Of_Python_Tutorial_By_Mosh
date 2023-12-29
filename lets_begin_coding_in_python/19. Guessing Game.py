secretNumber = 9
attempt = 3
while attempt > 0:
    guessedNumber = int(input("Guess: "))
    if guessedNumber == secretNumber:
        print("You win")
        break
    attempt -= 1

    # if attempt == 0:
    #     print("Sorry you failed!")
else:
    print("Sorry, you failed!!")
