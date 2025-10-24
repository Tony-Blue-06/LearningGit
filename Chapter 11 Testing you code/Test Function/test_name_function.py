import name_function as nm

def test_first_last_name():
    
    """Do all the names like 'Anton Shkreli' works ?"""
    
    formatted_name = nm.get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin' 
    
def test_first_middle_last_name():

    """Do all the names like 'Sarah Michelle Pfizer' works ?"""
    
    formatted_name = nm.get_formatted_name('sarah', 'pfizer', 'michelle')
    assert formatted_name == 'Sarah Michelle Pfizer' 