message = input("To determine the cost of your movie ticket, please enter your age: ")

if message != 'quit':
    message = int(message)

while message != 'quit':
    if message < 3:
        print("\nYour ticket is free!")
    elif message < 13:
        print("\nYour ticket is $10.")
    elif message >= 100:
        print("You take me for a fool!")
        #message == "quit" #This need a break statement to work
    else:
        print("\nYour ticket is $15.")
    message = input("To determine the cost of your movie ticket, please enter your age: ")
    if message == 'quit':
        break
    else:
        message = int(message) #This part if quit is written will give an error
    