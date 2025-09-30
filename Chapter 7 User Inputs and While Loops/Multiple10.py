multiple10 = input("Enter a number, and I'll tell you if it's a multiple of 10: ")
multiple10 = int(multiple10)

if multiple10 % 10 == 0:
    print("\nThe number " + str(multiple10) + " is a multiple of 10.")
else:
    print("\nThe number " + str(multiple10) + " is not a multiple of 10.")
    