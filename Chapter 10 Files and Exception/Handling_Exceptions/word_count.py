from pathlib import Path


def count_words(path):
    
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    except OSError:
        print("Si è verificato un errore durante la lettura del file. Controllare backlash e frontslash nel percorso del file.")
    except Exception as e:                           # /* This is the cheat code */
        print("Si è verificata un'eccezione!")
        print(f"Tipo: {type(e)}")
        print(f"Messaggio: {e}")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"Il file {path} contiene circa {num_words} parole.")

filenames = ['alice.txt', 'frankenstein.txt','moby_dick.txt','pride.txt', 'C:/Users/Big_T/Desktop/python_work/PY/Chapter 10 Files and Exception/Handling_Exceptionsfrankenstein.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)


    
    