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
    def __init__(self, publisher_name, publisher_birth_date, publisher_death_date=None):
        self.publisher_name = publisher_name
        self.publisher_birth_date = publisher_birth_date
        self.publisher_death_date = publisher_death_date


class Student:

    def __init__(self, name, card_id):
        self.name = name
        self.card_id = card_id
        self.books = []


class Librarian:
    pass
