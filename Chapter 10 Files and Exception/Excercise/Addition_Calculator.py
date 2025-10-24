
print("Inserire due numeri da sommare(premere q per uscire):")

def addition_calculator():

    num1 = input("Inserire il primo numero:")
    if num1.lower() == 'q':
        exit
    num2 = input("Inserire il secondo numero:")
    if num2.lower() == 'q':
        exit
    try:
        reuslt = int(num1) + int(num2)
    except ValueError as e:                           
        print("Errore: si è inserito un valore non numerico")
    except Exception as e:                           # /* This is the cheat code */
        print("Si è verificata un'eccezione!")
        print(f"Tipo: {type(e)}")
        print(f"Messaggio: {e}")
    else:
        print(f"La somma di {num1} e {num2} è {reuslt}")
        
  
while True:
    addition_calculator()