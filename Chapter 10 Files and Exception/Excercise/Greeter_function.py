from pathlib import Path
import json



def remember_me(path):
    get_new_username_data(path)

def greet_user(name):
        print(f"Welcome back, {name}!")    


def get_stored_data (path):
    
    if path.exists():
        content = path.read_text()
        data = json.loads(content)
        return data
    else:
        return None
    
def print_data(path):
    
    if path.exists():
        content = path.read_text()
        data = json.loads(content)
        print(f"This is the data stored in the json: {data}")
        return data
    else:
        return None
    
def get_new_username_data(path):
    
    username = input("What is your name? ")
    if path.exists():
        stored_datas = get_stored_data(path)
        
        for stored_data in stored_datas:
            if stored_data == username:
                greet_user(stored_data)
                return username
        else:
            None
                    
    age = input("What is your age? ")
    sex = input("What is your gender? ")
    
    data =[username, age, sex]

    load = json.dumps(data)
    path.write_text(load)
    return username


    