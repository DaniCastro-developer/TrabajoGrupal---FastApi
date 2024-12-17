class Books:
    def __init__(self, id, name, publisher, year, edition, authors):
        self.id = id
        self.name = name
        self.publisher = publisher
        self.year = year
        self.edition = edition
        self. authors = authors

    def __dict__(self):
        return {
                "id": self.id,
                "name": self.name,
                "publisher": self.publisher,
                "year": self.year,
                "edition": self.edition,
                "authors": self.authors,
                }


class Book_reviews:
    def __init__(self, review_id, book_id, review, validated):
        self.review_id = review_id
        self.book_id = book_id
        self.review = review
        self.validated = validated
    
    def __dict__(self):
        return {
            "review_id": self.review_id,
            "book_id": self.book_id,
            "review": self.review,
            "validated": self.validated
        }