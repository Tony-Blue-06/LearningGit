i=5
print(f"Ex 8.{i}")

#Ex 8.6

def city_country(city, country):
    """Return a string of the city and country."""
    ct = f'"{city.title()}, {country.title()}"'
    return ct

timer = 0
city={}

while timer > 3:  #Girare to < per runnare questa parte

    city_name = input("\nEnter a City name: ")
    country_name = input("\nEnter a Country name: ")
    
    city[timer] = city_country(city_name, country_name)
    print(city[timer])
    timer += 1
    if timer == 3:
        print("\nYou have reached the maximum number of entries.")
  
i+=1
print(f"\nEx 8.{i}")

#Ex 8.7 In verità abbiamo fatto l'8.8
def make_album(artist_name, album_title, num_of_tracks=None):
    """Return a dictionary containing information about an album."""
    album = {'Artist': artist_name.title(), 'Title': album_title.title()}
    if num_of_tracks:
        album['tracks'] = num_of_tracks
    return album

while timer > 3:  #Girare to < per runnare questa parte

    artist = input("\nEnter the artist name: ")
    album = input("\nEnter the album title: ")
    tracks = input("\nEnter the number of tracks (or press Enter to skip): ")
    
    if tracks.isdigit(): #Controllo se inserito un valore per tracks
        album_info = make_album(artist, album, int(tracks))
    else:
        album_info = make_album(artist, album)
    
    print(album_info)
    timer += 1
    if timer == 3:
        print("\nYou have reached the maximum number of entries.")