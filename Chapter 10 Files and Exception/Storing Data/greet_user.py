from pathlib import Path
import json


def greet_user(path):
    
    var_path = path
    username = get_stored_username(var_path)
    if username:
        print(f"Welcome back, {username}!")    
    else:
        username = get_new_username(var_path)
        print(f"We will remember you when you come back, {username}!")

def get_stored_username(path):
    
    if path.exists():
        content = path.read_text()
        username = json.loads(content)
        return username
    else:
        return None
    
def get_new_username(path):
    
    username = input("What is your name? ")
    load = json.dumps(username)
    path.write_text(load)
    return username
