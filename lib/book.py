class Book:
    def __init__(self, title, pages, author=None, price=0.0):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise ValueError("Author must be a string")
        self._author = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Pages must be a non-negative integer")
        self._pages = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a non-negative number")
        self._price = value

    def __str__(self):
        return f"Book: {self.title} by {self.author}, {self.pages} pages, ${self.price:.2f}"