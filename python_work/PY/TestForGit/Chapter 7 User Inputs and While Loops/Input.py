#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)
try:
    height = input("How tall are you, in inches? ")
    height = int(height)
except EOFError:
    height = 50

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")