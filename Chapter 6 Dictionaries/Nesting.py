alien_0 = {'color' : 'green',
        'points' : 5
        }
alien_1 = {'color' : 'yellow',
        'points' : 10
        }
alien_2 = {'color' : 'red',
        'points' : 15
        }

aliens = [alien_0, alien_1, alien_2]

skip = True

if not skip:
    for alien in aliens:
        print(alien.values())

#Generating 30 aliens 

#Nesting a dictionary inside a list
aliens = []
if not skip:
    for alien_number in range(30):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)

    for alien in aliens[:5]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10
        elif alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed'] = 'fast'
            alien['pints'] = 15

    for alien in aliens[:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10
        elif alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed'] = 'fast'
            alien['points'] = 15

    for alien in aliens[:6]:
        print(alien)

    print(len(aliens))

#Nesting a list inside a dictionary

favourite_languages = {
    'jen': ['python', 'rust'],
    'sarah': 'c',
    'edward': ['ruby', 'rust'],
    'phil': ['python', 'c'],
    }
if not skip:
    for name, languages in favourite_languages.items():
        if len(languages) >1:
            print(f"\n{name.title()}'s favourite languages are: ")
        else:
            print(f"\n{name.title()}'s favourite language is: ")

#Nesting a dictionary inside a dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")