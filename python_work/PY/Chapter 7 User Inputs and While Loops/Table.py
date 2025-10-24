dinner = input("How many people are in your dinner group? ")

dinner = int(dinner)

if dinner > 8:
    print("\nYou will have to wait a bit before seating.")
else:
    print("\nYour table is ready!")