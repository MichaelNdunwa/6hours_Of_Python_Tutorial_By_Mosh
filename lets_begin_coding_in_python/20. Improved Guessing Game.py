import random


# Getting the user input:
def get_user_guess():
    while True:
        try:
            return int(input("Guess a number between 0 and 10: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Feedback message:
def provide_feedback(guess, secret_number):
    if guess == secret_number:
        print("You win!")
    elif guess < secret_number:
        print("Tool low! Try again.")
    else:
        print("Too high! Try again.")


def guessing_game():
    print("Welcome to Guessing Game! \nTry to guess the secret number.")
    secret_number = random.randint(1, 10)
    attempts = 3
    while attempts > 0:
        user_guess = get_user_guess()

        if user_guess == secret_number:
            provide_feedback(user_guess, secret_number)
            break
        else:
            provide_feedback(user_guess, secret_number)
        attempts -= 1

        if attempts == 0:
            print(f"Sorry, you failed! The correct number was {secret_number}")


if __name__ == "__main__":
    guessing_game()
