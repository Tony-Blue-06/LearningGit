my_foods=['pizza','falafel','carrot cake']
#Slicing is essential to create a different lis, otherwise the list will be the same so when working with one list we are working with the other also
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('banana')

print(my_foods)
print(friend_foods)

#Exercise 4.10
pizzas = ['margherita', 'pepperoni', 'hawaiian', 'bbq chicken', 'buffalo', 'veggie', 'meat lovers', 'supreme', 'cheese', 'mushroom']
first_three_msg = "The first three items in the list are: "
middle_three_msg = "The middle three items in the list are: "
last_three_msg = "The last three items in the list are: "

print(first_three_msg)
for pizza in pizzas[:3]:
    print(pizza.title())
print(middle_three_msg)
for pizza in pizzas[3:6]:
    print(pizza.title())
print(last_three_msg)
for pizza in pizzas[-3:]:
    print(pizza.title())

#Exercise 4.11
my_pizzas = pizzas[:]
friend_pizzas = my_pizzas[:]

my_pizzas.append('salame piccante')
friend_pizzas.append('gorgonzola')

print("My favorite pizzas are:")
for mypizza in my_pizzas:
    print(mypizza.title())

print("My friend's favorite pizzas are:")
for friendpizza in friend_pizzas:
    print(friendpizza.title())
#Used a pop to prove that list are the same without last element
my_pizzas.pop()
friend_pizzas.pop()

if my_pizzas == friend_pizzas:
    print("The lists are the same")
else:
    print("The lists are different")
