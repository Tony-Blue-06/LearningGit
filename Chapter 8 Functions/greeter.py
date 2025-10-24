#Function without parameters and without return value

def greet_user():
    """Display a simple greeting."""
    print("Hello! Welcome to the program.")

greet_user()

#Function with parameters and without return value

def greet_user_by_name(username):
    """Display a personalized greeting."""
    print(f"hello, {username.title()}! Welcome to the program. ")

greet_user_by_name('alice')

def get_formatted_name(first_name, last_name):
    """Return a formatted full name."""
    full_name = f"{first_name.strip().title()} {last_name.strip().title()}"
    return full_name

while True:
    print("\nPlease tell me your name:")
    f_name = input("First Name: ")
    f_last = input("Last Name: ")

    if f_name.lower() == 'q' or f_last.lower() == 'q':
        break
    

    formatted_name = get_formatted_name(f_name, f_last)
    print(f"\nHello, {formatted_name}!")