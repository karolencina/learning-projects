# Basic class definitions

# TODO: create a basic class
class Book:
    def __init__(self, title):
        self.title = title
        print(f"Initialised a new Book instance: \"{self}\" with the "
              f"title \"{self.title}\".")

# TODO: create an instance of the class
book1 = Book("His Dark Materials")
book2 = Book("100 Years of Solitude")

# TODO: print the class and property
print(book1)
print(book1.title)