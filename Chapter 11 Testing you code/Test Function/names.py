import name_function as nm

print("Enter 'q' at any time to quit")

while True:

    first  = input("Enter a first name: ")
    if first == 'q':
        break
    
    last  = input("Enter a last name: ")
    if last == 'q':
        break
    
    formatted_name = nm.get_formatted_name(first, last)
    print(f"\nNeatly formatted name : {formatted_name}")
    