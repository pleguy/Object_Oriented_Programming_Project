from product.product import Product


class Movie(Product):
    def __init__(self, name, language, genre, category, stock, price, product_code, directors, starring, subtitles,
                 audio_language):
        super().__init__(name, language, genre, category, stock, price, product_code)
        self.directors = directors
        self.starring = starring
        self.subtitles = subtitles
        self.audio_language = audio_language

    def display(self):
        super().display()
        print(f"Directors: {', '.join(self.directors)}\nStarring: {', '.join(self.starring)}\n"
              f"Subtitles: {self.subtitles}\nAudio Language: {self.audio_language}")

    def calculate_discount(self):
        discount_rate = 0.05
        discounted_price = self.price - (self.price * discount_rate)
        return discounted_price

    @staticmethod
    def display_all_movies(movie_list):
        print("\nAll Movies:")
        for i, movie in enumerate(movie_list):
            print(f"{i + 1}. {movie.name}")
            movie.display()
            print("-" * 30)
