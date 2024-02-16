# Using instance methods and attributes

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
    # TODO: create instance methods

    def get_price(self):
        return self.price


# TODO: create an instance of the class
book1 = Book("His Dark Materials", "Phillip Pullman", 954, 29.99)
book2 = Book("100 Years of Solitude", "Gabriel Garcia Marquez", 412, 12.99)

# TODO: print the class and property

# TODO: print the price of the book
print(book1.get_price())

# TODO: try setting the discount
