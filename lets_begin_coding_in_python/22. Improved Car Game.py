def start_car():
    global car_started
    if not car_started:
        car_started = True
        return "Car started.."
    else:
        return "Car is already started!"


def stop_car():
    global car_started
    if car_started:
        car_started = False
        return "Car stopped."
    else:
        return "Car is stopped already."


def print_help():
    return """
    start --> to start the car.
    stop --> to stopp the car.
    quit --> to exit.
    """


def quit_game():
    print("Thank you for playing! Goodbye.")
    exit()


print("Welcome to Car Game!!")
print("To get the manual, type: Help")

car_started = False

commands = {
    'help': print_help,
    'start': start_car,
    'stop': stop_car,
    'quit': quit_game
}

while True:
    user_input = input("> ").lower()

    if user_input in commands:
        print(commands[user_input]())
    else:
        print("I don't understand that...")
