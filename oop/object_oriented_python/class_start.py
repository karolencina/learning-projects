class Book:
    #TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    #TODO: double underscore properties are hidden from other classes
    __booklist = None

    #TODO: create a class method
    @classmethod
    def get_booktypes(cls):
        return cls.BOOK_TYPES

    #TODO: create a static method
    def get_booklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    #instance methods receive a specific object instance as an argument and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f'{booktype} is not a valid booktype.')
        else:
            self.booktype = booktype

# TODO: access the class attribute
print(f"Book types: {Book.get_booktypes()}")

# TODO: create some book instances
b1 = Book("The Vorrh", "PAPERBACK")
b2 = Book("Diary of an oxygen thief", "PAPERBACK")

# TODO: use the static method to access a singleton object
thebooks = Book.get_booklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)