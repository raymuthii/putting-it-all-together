class Book:
    def __init__(self, title, page_count, author=None, price=0.0):
        self.title = title
        self.page_count = page_count
        self.author = author
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
        if value is not None and not isinstance(value, str):
            raise ValueError("Author must be a string")
        self._author = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        if value < 0:
            raise ValueError("Pages must be a non-negative integer")
        self._page_count = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a non-negative number")
        self._price = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __str__(self):
        return f"Book: {self.title} by {self.author}, {self.page_count} pages, ${self.price:.2f}"
