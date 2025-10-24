class Restaurant:
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"The restaurant's cuisine type is {self.cuisine_type}.\n")
    
    def open_restaurant(self):
        """Simulate opening the restaurant."""
        print(f"{self.restaurant_name} is now open!\n")

    def update_number_served(self, number):
        """Set the number of customers that have been served."""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("Error0001: You can't roll back the number of served customers!")
            
    def print_number_served(self):
        """Print the number of customers that have been served."""
        print(f"{self.number_served} customers have been served.\n")

    def increment_number_served(self, additional_customers):
        """Add the given amount to the number of served customers."""
        if additional_customers >= 0:
            self.number_served += additional_customers
        else:
            print("Error0002: You can't decrease the number of served customers!")

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f"User's first name is {self.first_name}.")
        print(f"User's last name is {self.last_name}.\n")
    
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!\n")
        