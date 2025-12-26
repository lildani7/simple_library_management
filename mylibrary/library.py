class Library():

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})
        print(f'Book "{title}" added!\n\n')

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f'Book "{title}" removed!\n\n')
                return None
        
        print("The desired book was not found!\n\n")

    def search_book(self, title):
        for book in self.books:
            if book['title'] == title:
                print(f'Book "{title}" was found!\n\n')
                return None

        print("The desired book was not found!\n\n")

    def show_books(self):
        for book in self.books:
            print(book, sep="\n")
        
        print("\n\n")