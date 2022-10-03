class Book:
    def __init__(self, name, publish_date, category, publisher, author):
        self.name = name
        self.publish_date = publish_date
        self.category = category
        self.publisher = publisher
        self.author = author


class Author:
    def __init__(self, author_name, author_birth_date, author_death_date=None):
        self.author_name = author_name
        self.author_birth_date = author_birth_date
        self.author_death_date = author_death_date


class Publisher:
    def __init__(self, publisher_name, publisher_birth_date=None, publisher_death_date=None):
        self.publisher_name = publisher_name
        self.publisher_birth_date = publisher_birth_date
        self.publisher_death_date = publisher_death_date


class Student:

    def __init__(self, name, card_id):
        self.name = name
        self.card_id = card_id
        self.books = []



class Librarian:
    @staticmethod
    def get_book(student, book_name):
        if len(student.books) >= 5:
            raise "Maximum books"
        else:
            student.books.append(book_name)

    @staticmethod
    def book_back_in (student, book_name):
        student.books.remove(book_name)

author_1 = Author(author_name="Scott Fitzgerald", author_birth_date=1896, author_death_date=1940)
publisher_1 = Publisher(publisher_name="Charles Scribner's",)
book_1 = Book(name="The Great Gatsby",
              publish_date=1925,
              category="Tragedy",
              publisher=publisher_1,
              author=author_1)

student_1 = Student("John", 123558)

Librarian.get_book(student=student_1, book_name="The Great Gatsby")

Librarian.book_back_in(student=student_1, book_name="The Great Gatsby")

print(student_1.books)