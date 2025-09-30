# List comprehension
cubes = [x**3 for x in range(1, 11)]

# Print the list of cubes
for cube in cubes:
    print(cube)
#List created through a loop 
cubes1 = []

for i in range(1,11):
    cubes1.append(i**3)

#for cube1 in cubes1:
#    print(cube1)

#Slicing a list 
print(cubes1[0:3])

#printing only the first 3 elements of the list
for cube1 in cubes1[:3]:
    print(cube1)
