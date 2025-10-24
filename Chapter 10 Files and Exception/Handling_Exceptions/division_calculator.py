from pathlib import Path

#print("Give me two numbers, and I'll divide them.")
#print("Enter 'q' to quit.")


game = False

while game:

    first_number = input("\n First number: ")
    if first_number == 'q':
        break
    second_number = input(" Second number: ")
    if second_number == 'q':
        break
    try: 
        ansewer = int(first_number) / int(second_number)

    except Exception as e:
        print("Si è verificata un'eccezione!")
        print(f"Tipo: {type(e)}")
        print(f"Messaggio: {e}")
