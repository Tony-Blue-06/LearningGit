from pathlib import Path
import json
#    path = Path("Storing Data/username.json")

def remember_me(path):
    
    if path.exists():
        return 
    else:
        username = input("Enter your name: ")
        load = json.dumps(username)
        path.write_text(load)
        print("We will remember you when you come back" )
    return 
