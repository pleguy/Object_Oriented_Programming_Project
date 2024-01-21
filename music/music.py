from product.product import Product


class Music(Product):
    def __init__(self, name, language, genre, category, stock, price, product_code, artist, format, run_time):
        super().__init__(name, language, genre, category, stock, price, product_code)
        self.artist = artist
        self.format = format
        self.run_time = run_time

    def display(self):
        super().display()
        print(f"Artist: {self.artist}\nFormat: {self.format}\nRun Time: {self.run_time} minutes")

    def calculate_discount(self):
        discount_rate = 0.15
        discounted_price = self.price - (self.price * discount_rate)
        return discounted_price

    @staticmethod
    def display_all_music(music_list):
        print("\nAll Music:")
        for i, music in enumerate(music_list):
            print(f"{i + 1}. {music.name}")
            music.display()
            print("-" * 30)
