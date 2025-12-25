from mylibrary.library import Library

def menu():
    print("Home Page\n" \
    "\n1.Add Book" \
    "\n2.Remove Book" \
    "\n3.Search Book" \
    "\n4.Show Books" \
    "\n5.Exit\n\n")

if __name__ == "__main__":
    lib = Library()

    is_continue = True
    while(True):
        menu()
        while(True):
            try:
                user_choice = int(input("Enter your desired option number: "))

                match user_choice:
                    case 1:
                        title = input("\nEnter the book title: ")
                        author = input("Enter the book author: ")
                        print()
                        lib.add_book(title, author)
                        break

                    case 2:
                        title = input("Enter the book title: ")
                        print()
                        lib.remove_book(title)
                        break

                    case 3:
                        title = input("Enter the book title: ")
                        print()
                        lib.search_book(title)
                        break

                    case 4:
                        print()
                        lib.show_books()
                        break

                    case 5:
                        is_continue = False
                        break

                    case _:
                        print("You entered an invalid option!\nPlease enter a number between 1 to 5...\n\n")



            except ValueError: 
                print("You entered an invalid option!\nPlease enter a number between 1 to 5...\n\n")
        
        if not is_continue:
            break