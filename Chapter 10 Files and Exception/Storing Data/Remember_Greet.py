import greet_user as greet
import remember_me as remember
from pathlib import Path

#path = Path("Storing Data/username.json")
path = Path("username.json")

try:
    game = greet.greet_user(path)
    
except Exception as e:                           # /* This is the cheat code */
    print("Si è verificata un'eccezione!")
    print(f"Tipo: {type(e)}")
    print(f"Messaggio: {e}")

    