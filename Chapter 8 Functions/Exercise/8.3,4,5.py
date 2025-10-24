
i=3
print(f"Ex 8.{i}")



#Ex 8.3

def make_shirt (size, message):
    """Display a message about the shirt size and the printed message."""
    size = {size.upper()}
    message = message.title()
    print(f"The shirt size is {size}.")
    print(f'The message on the shirt is: "{message}"')

make_shirt('m', 'keep calm and code on')
i+=1
print(f"\nEx 8.{i}")


#ex 8.4

def make_shirt_fixed (size ):
    """Display a message about the shirt size and the printed message."""
    size = {size.upper()}
    message = "I love Python"
    print(f"The shirt size is {size}.")
    print(f'The message on the shirt is: "{message}"')

make_shirt_fixed('l')

i+=1
print(f"\nEx 8.{i}")

#Ex 8.5
def describe_city(cityname, country):
    """Display information in which country the city is located."""
    print(f"{cityname.title()} is in {country.title()}.")

describe_city('rome', 'italy')
