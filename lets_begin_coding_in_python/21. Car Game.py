
print("Welcome to Car Game!!")
print("To get the manual type: Help")
car_started = False
while True:
    user_input = input(">").lower()
    if user_input == "help":
        print("start --> to start the car.")
        print("stop --> to stop the car.")
        print("quit --> to exit.")

    elif user_input == "start":
        if not car_started:
            car_started = True
            print("Car started...")
        else:
            print("Car is already started!")

    elif user_input == "stop":
        if car_started:
            car_started = False
            print("Car stopped.")
        else:
            print("Car is already stopped!!")

    elif user_input == "quit":
        print("Thank you for playing! Goodbye.")
        break

    else:
        print("I don't understand that...")
