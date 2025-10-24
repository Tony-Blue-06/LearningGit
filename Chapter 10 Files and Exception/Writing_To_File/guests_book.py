from pathlib import Path


path = Path('guest_book.txt')


def write_guest_book(path):
    guest_book_content = ''   
    guest_name = ''
    while guest_name != '0' :
            guest_name = input("Enter your name (or enter 0 to quit): ")
            if guest_name != '0':
                guest_book_content += guest_name +'\n'

    path.write_text(guest_book_content)
    read_guest_book(path)
    return 0

def read_guest_book(path):
    contents = path.read_text()
    print("Guest Book Entries:")
    print(contents)




run = 1
#while run != 0:
 #print("Add Guest book(or enter 0 to quit):")
 #run = guest_book = write_guest_book(path)
