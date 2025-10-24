
#ex 8.9 

print(f"Exercise 8.9\n")

messages = [
    "Hey, what's up?",
    "Call me when you're free.",
    "Don't forget the meeting at 3.",
    "Lunch later?",
    "Can you send the files?",
    "See you soon!",
    "Happy birthday!",
    "Running late, sorry!",
    "Let's catch up this weekend.",
    "Congrats on your promotion!"
]

def show_messages(messages):
    """Print each message from the list."""
    for message in messages:
        print(message)

def sent_messages(messages):

    sent_messages = []
    print("\nThe following messages have been sent:")
    show_messages(messages)
  

    #Sposta nell a lista sent_messages gli elementi della lista messages
    while messages:
        current_message = messages.pop(0)
        sent_messages.append(current_message)
    return sent_messages

messaggi_mandati = sent_messages(messages[:])

print("\nLista dei messaggi inviati:")
show_messages(messaggi_mandati)

print("\nLista orgininale:")
show_messages(messages)