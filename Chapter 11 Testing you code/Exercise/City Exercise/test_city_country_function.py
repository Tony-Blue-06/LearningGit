import city_function as ct

def test_city_country_function():

    """Assert that the city 'milano' and country 'italia' will be Milano, Italia """
   
    composed_city_country = ct.city_function('milano','italia')
    assert composed_city_country == 'Milano, Italia'

def test_city_country_population():
    
    """Assert that the city 'milano', country 'italia' and population '72000000' will be Milano, Italia """
   
    composed_city_country = ct.city_function('milano','italia', '72000000')
    assert composed_city_country == 'Milano, Italia - Population: 72000000'