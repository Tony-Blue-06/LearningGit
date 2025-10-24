#Passing an arbirtrary number of arguments to a function
def make_pizza(*toppings):
    "Print the list of toppings that have been requested."
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        #print("x")
        print(f"- {topping}") 

toppings1 = ['pepperoni', 'mushrooms', 'onions', 'green peppers']
toppings2 = ['sausage', 'bacon', 'olives', 'tomatoes']

make_pizza('pepperoni')
make_pizza(*toppings1)
make_pizza(*toppings2)