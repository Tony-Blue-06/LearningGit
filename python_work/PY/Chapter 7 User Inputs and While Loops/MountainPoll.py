responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is you name? ")
    response = input("\nWhich mountain will you like to climb someday? ")

    #Store the responses
    responses[name] = response

    #Find out if someone else want to do the poll
    repeat = input("Would you like to let another person take the pool? Press No to quit ")
    if repeat.lower() == 'no'
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} will like to climb in {response}")