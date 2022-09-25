class Book:
    def __init__(self, name, publisher, publish_date, category, author):
        self.name = name
        self.publisher = publisher
        self.publish_date = publish_date
        self.category = category
        self.author = author


class Student:

    def __init__(self, name, card_id):
        self.name = name
        self.card_id = card_id
        self.books = []


class Librarian:
    pass


book_1 = Book(name="The Great Gatsby",
              publisher="Charles Scribner's Sons",
              publish_date="April 10 1925",
              category="Tragedy",
              author={"Scott Fitzgerald": ["September 24, 1896 – December 21, 1940",
                                           "American fiction writer"]}
              )
