class Book:
    Book_list = []

    def __init__(self, name, publish_date, category, publisher, author):
        self.name = name
        self.publish_date = publish_date
        self.category = category
        self.publisher = publisher
        self.author = author
        self.name_list(self)

    @classmethod
    def name_list(cls, book):
        cls.Book_list.append(book.name)


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


class Librarian(Book):
    @staticmethod
    def get_book(student, book_name):
        if len(student.books) >= 5:
            raise "Maximum books"
        else:
            if book_name in __class__.Book_list:
                student.books.append(book_name)
                __class__.Book_list.remove(book_name)
            else:
                raise "This book is not available"

    @staticmethod
    def book_back_in(student, book_name):
        __class__.Book_list.append(book_name)
        student.books.remove(book_name)


author_1 = Author(author_name="Scott Fitzgerald", author_birth_date=1896, author_death_date=1940)
author_2 = Author(author_name="Leo Tolstoy", author_birth_date=1828, author_death_date=1910)

publisher_1 = Publisher(publisher_name="Charles Scribner's", )

book_1 = Book(name="The Great Gatsby",
              publish_date=1925,
              category="Tragedy",
              publisher=publisher_1,
              author=author_1)

book_2 = Book(name="War and Peace",
              publish_date=1869,
              category="Historical novel",
              publisher=publisher_1,
              author=author_2)

student_1 = Student("John", 123558)

Librarian.get_book(student=student_1, book_name="The Great Gatsby")
Librarian.get_book(student=student_1, book_name="War and Peace")

Librarian.book_back_in(student=student_1, book_name="The Great Gatsby")

print(Book.Book_list)

print(student_1.books)
