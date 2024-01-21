class Product:
    def __init__(self, name, language, genre, category, stock, price, product_code):
        self.name = name
        self.language = language
        self.genre = genre
        self.category = category
        self.stock = stock
        self.price = price
        self.product_code = product_code

    def display(self):
        print(f"Product: {self.name}\nLanguage: {self.language}\nGenre: {self.genre}\nCategory: {self.category}\n"
              f"Stock: {self.stock}\nPrice: ${self.price}\nProduct Code: {self.product_code}")

    def calculate_discount(self):
        return self.price

    def check_stock(self):
        return self.stock
