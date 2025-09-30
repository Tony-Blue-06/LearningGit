#Exercise 5.8
# List of 5 names including 'admin'
usernames = ['admin', 'john', 'sarah', 'mike', 'anna']

#Clearing list for exercise 5.9
while usernames:
    usernames.pop()
skip = 0
# Check if the list is empty
if skip:
    if usernames:
        for user in usernames:
            if user == 'admin':
               print(f"Hello {user.title()}, would you like to see a status report?")
            else:
                print(f"Hello {user.title()}, thank you for logging in again.")
    else:
        print("We need to find some users!")
#Exercise 5.10

current_users = ['admin', 'john', 'sarah', 'mike', 'anna', 'tony']
new_users = ['marco', 'alberto', 'francesco', 'anna', 'tony']
#Adding skip to avoid running this exercise while working on 5.11
if current_users and new_users and skip:
    for new_user in new_users:
        if new_user in current_users:
            print(f"Sorry, {new_user.title()} is already taken. Please choose another username.")
        else:
            print(f"Congratulations, {new_user.title()} is available.")

#Exercise 5.11

ordinated_numbers = list(range(1,10))
print(ordinated_numbers)
for number in ordinated_numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
#Output