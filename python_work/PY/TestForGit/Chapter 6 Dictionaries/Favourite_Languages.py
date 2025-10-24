favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


for name, language in favourite_languages.items():
    print(f"{name.title()} favourite langiage is: {language.title()} ")



def find_favourite_language(favourite_languages):
    language_count = {}
    for language in favourite_languages.values():
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

    winner = max(language_count, key=language_count.get)
    return winner

winner_language = find_favourite_language(favourite_languages)
print(f"\nThe most popular favourite language is: {winner_language.title()}")
print("\nThe following were mentioned: ")

for language in set(favourite_languages.values()):
    print(language.title())