#Chapter 4: Working with Lists
#4.1 Looping Through an Entire List
magicians = ["Houdini", "Copperfield", "Blaine", "Angel", "Penn", "Teller", "Devant", "Thurston", "Blackstone", "Henning"]

squares=[]

for value in range(0,11):
    squares.append(value**2)

print(squares)

numbers = list(range(0,11))

print(min(numbers))
print(max(numbers))
print(sum(numbers))