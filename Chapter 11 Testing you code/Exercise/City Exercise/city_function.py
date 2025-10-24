def city_function(city, country, population=''):
    """Return the name of a city and a coutry in the format City, Country"""
    if population:
        city_country = f"{city}, {country} - population: {population}"
    else:
        city_country = f"{city}, {country}"
        
    return city_country.title()