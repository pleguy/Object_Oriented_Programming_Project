from product.product import Product


class Book(Product):
    def __init__(self, name, language, genre, category, stock, price, product_code, author, isbn):
        super().__init__(name, language, genre, category, stock, price, product_code)
        self.author = author
        self.isbn = isbn

    def display(self):
        super().display()
        print(f"author: {self.author}\nISBN: {self.isbn}")

    def calculate_discount(self):
        discount_rate = 0.12
        discounted_price = self.price - (self.price * discount_rate)
        return discounted_price

    @staticmethod
    def display_all_books(book_list):
        print("\nAll Books:")
        for i, book in enumerate(book_list):
            print(f"{i + 1}. {book.name}")
            book.display()
            print("-" * 30)
