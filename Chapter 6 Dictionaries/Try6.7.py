person1 = {
    'first_name': 'Anton',
    'second_name': 'Shkreli',
    'city':'Utrecht'
    }

person2 = {
    'first_name': 'Sinisa',
    'second_name': 'Tatalovic',
    'city':'Parma'
    }

person3 = {
    'first_name': 'Nikola',
    'second_name': 'Jokic',
    'city':'Denver'
    }

people = [person1, person2, person3]

for person in people:
    print(f"\n Name: {person['first_name']} {person['second_name']}")
    print(f" City: {person['city']}")