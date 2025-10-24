def get_formatted_name(first_name, last_name):
    """Return a formatted full name."""
    full_name = f"{first_name.strip().title()} {last_name.strip().title()}"
    return full_name

musician = get_formatted_name('jimi', 'hendrix')
print(musician)