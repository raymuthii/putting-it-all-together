class Shoe:
    def __init__(self, brand, style, size, price):
        self.brand = brand
        self.style = style
        self.size = size
        self.price = price

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string")
        self._brand = value

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        if not isinstance(value, str):
            raise ValueError("Style must be a string")
        self._style = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Size must be a non-negative number")
        self._size = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a non-negative number")
        self._price = value

    def __str__(self):
        return f"Shoe: {self.brand} {self.style}, size {self.size}, ${self.price:.2f}"