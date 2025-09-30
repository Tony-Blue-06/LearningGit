#An immutable list is called a tuple. Tuples are defined by enclosing the elements in parentheses ().
# Tuples are faster than lists because they are immutable.  

rectangle = (100, 50)


#rectangle[0] = 200
# The above line will throw an error

for dimension in rectangle:
    print(dimension)

#Writing over a tuple
rectangle = (200, 100)
for dimension in rectangle:
    print(dimension)

#Exercise 4.13
first_menu = ('pizza', 'burger', 'hotdog', 'sandwich', 'pasta')

for item in first_menu:
    print(item.title())

first_menu = ('chicken', 'toast', 'salad', 'potato', 'cheese')

for item in first_menu:
    print(item.title())

