# Using compostion to build complex objects

class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    # The book has a collection of chapter objects:
    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def get_book_page_count(self):
        result = 0
        for ch in self.chapters:
            result += ch.page_count

    def get_chapters_names(self):
        names = []
        for ch in self.chapters:
            names.append(ch.name)
        names = ', '.join(names)
        return names


class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Chapter:
    def __init__(self, name, page_count):
        self.name = name
        self.page_count = page_count


author = Author("David", "Mitchell")
book = Book("Cloud Atlas", 29.95, author)
book.add_chapter(Chapter("Chapter 1", 104))
book.add_chapter(Chapter("Chapter 2", 89))
book.add_chapter(Chapter("Chapter 3", 124))

print(f"Book title: {book.title}, Author: {book.author}, Chapters: "
      f" {book.get_chapters_names()})")