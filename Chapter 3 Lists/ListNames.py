# Exe 3.4 Guest List
person_of_interest = ['napoleone','giulio cesare','cleopatra']
pre_message = "Hello, "
post_message = ", would you like to haver dinner with me?"

for i in range(len(person_of_interest)):
    print(f"{pre_message}{person_of_interest[i].title()}{post_message}")

person_of_interest_not_coming = [person_of_interest.pop(1)]
print(f"{person_of_interest_not_coming[0].title()} is not coming to dinner.")

#Exe 3.5 Changing Guest List

person_of_interest.insert(1,'marco polo')
person_of_interest.append('genghis khan')

for i in range(len(person_of_interest)):
    print(f"{pre_message}{person_of_interest[i].title()}{post_message}")

#Exe 3.6 More Guests
print("I found a bigger table, so I can invite more people to dinner.")

person_of_interest.insert(0, 'christopher nolan')
person_of_interest.insert(3, 'silvio berlusconi')
person_of_interest.append("ilaria d'amico")


for i in range(len(person_of_interest)):
    print(f"{pre_message}{person_of_interest[i].title()}{post_message}")

# Exe 3.7 Shrinking Guest List
sorry_message = "Sorry, I can only invite two people to dinner."
print(sorry_message)

for i in range(len(person_of_interest)-2):
    removed_person = [person_of_interest.pop()]
    print(f"Sorry, {removed_person[0].title()} I can't invite you to dinner.")

present_message = "will come to dinner."
for i in range(len(person_of_interest)):
    print(f"{person_of_interest[i].title()} {present_message}")

while len(person_of_interest) >= 1:
    del person_of_interest[0]

print(person_of_interest)