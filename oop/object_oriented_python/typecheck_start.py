class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


b1 = Book("His Dark Materials")
b2 = Book("100 Years of Solitude")
n1 = Newspaper("The Verge")
n2 = Newspaper("Wired")


# TODO: use type() to inspect the object type
print(type(b1))
print(type(n2))

# TODO: compare two types together
print(type(b1) == type(b2))
print(type(b1) == type(n1))

# TODO: use isinstance to compare a specific instance to a known type
print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n1, object))