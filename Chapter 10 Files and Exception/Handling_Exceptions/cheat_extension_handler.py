try:
    print(10 / 0)
except Exception as e:                           # /* This is the cheat code */
    print("Si è verificata un'eccezione!")
    print(f"Tipo: {type(e)}")
    print(f"Messaggio: {e}")