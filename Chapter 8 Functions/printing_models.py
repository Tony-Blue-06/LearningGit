unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []



#Reordering using two functions 

def print_original(originials):

    print("\nLista originale")
    for originial in originials:
        print(originial)

def print_models(unprinted_designs, completed_models):

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    return completed_models

def show_completed_models(completed_models):

    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

#print_models(unprinted_designs, completed_models)
#show_completed_models(completed_models)

show_completed_models(print_models(unprinted_designs[:], completed_models))
print_original(unprinted_designs) 

