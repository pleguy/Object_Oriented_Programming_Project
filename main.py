from book.book import Book
from music.music import Music
from movie.movie import Movie
from cart_list.cart import Cart
from Users.authenticate import authenticate_user
from Users.user import User


def admin_menu(admin):
    while True:
        print("\nAdmin Menu:")
        print("1. Update Product Information")
        print("2. Exit")
        choice = input("Select operation (1/2): ")

        if choice == '1':
            update_product_information_menu()
        elif choice == '2':
            print("Admin logged out.")
            break
        else:
            print("Invalid choice. Please try again.")


def update_product_information_menu():
    print("\nSelect Category:")
    print("1. Book")
    print("2. Movie")
    print("3. Music")
    print("4. Exit")
    category_choice = input("Select category: ")

    if category_choice == '4':
        print("Returning to admin menu.")
        return

    product_list = get_product_list_by_category(category_choice)

    if not product_list:
        print("No products in the selected category.")
        return

    display_products(product_list)

    while True:
        print("\nUpdate Product Menu:")
        print("1. Update Stock")
        print("2. Update Price")
        print("3. Exit")
        update_choice = input("Select operation (1/2/3): ")

        if update_choice == '1':
            update_stock_price(product_list, 'stock')
        elif update_choice == '2':
            update_stock_price(product_list, 'price')
        elif update_choice == '3':
            print("Returning to admin menu.")
            break
        else:
            print("Invalid choice. Please try again.")


def get_product_list_by_category(category_choice):
    if category_choice == '1':
        return books
    elif category_choice == '2':
        return movies
    elif category_choice == '3':
        return musics
    else:
        return []


def display_products(product_list):
    for i, product in enumerate(product_list):
        print(f"{i + 1}. {product.name}")


def update_stock_price(product_list, attribute):
    if not product_list:
        print("No products in the selected category.")
        return

    display_products(product_list)

    product_number = input("Enter the number of the product to update (or press Enter to go back): ")

    if product_number.isdigit() and 1 <= int(product_number) <= len(product_list):
        select_product = product_list[int(product_number) - 1]
        new_value = input(f"Enter the new {attribute}: ")

        if attribute == 'stock':
            select_product.stock = int(new_value)
        elif attribute == 'price':
            select_product.price = float(new_value)

        print(f"{select_product.name} {attribute.capitalize()} updated to {new_value}.")
    elif not product_number:
        print("Returning to update menu.")
    else:
        print("Invalid product number. Please try again.")


def customer_menu(customer):
    cart = Cart()

    while True:
        print("\nCustomer Menu:")
        print("1. View Cart")
        print("2. Select Category")
        print("3. Exit")
        choice = input("Select operation (1/2/3): ")

        if choice == '1':
            cart.view_cart()
        elif choice == '2':
            show_category_menu()
            category_choice = input("Select category: ")
            display_products_by_category(category_choice, cart)
        elif choice == '3':
            exit_choice = input("Do you want to exit? (y/n): ")
            if exit_choice.lower() == 'y':
                print("Customer logged out.")
                break
            else:
                print("Returning to customer menu.")
        else:
            print("Invalid choice. Please try again.")


def show_category_menu():
    print("\nProduct Categories:")
    print("1. Book")
    print("2. Music")
    print("3. Movie")
    print("4. Exit")


def display_products_by_category(category_choice, cart):
    if category_choice == '1':
        Book.display_all_books(books)
        add_to_cart_choice(cart, books)
    elif category_choice == '2':
        Music.display_all_music(musics)
        add_to_cart_choice(cart, musics)
    elif category_choice == '3':
        Movie.display_all_movies(movies)
        add_to_cart_choice(cart, movies)
    elif category_choice == '4':
        print("Returning to customer menu.")
    else:
        print("Invalid category choice. Please try again.")


def add_to_cart_choice(cart, products):
    product_number = input("Enter the number of the product to add to cart (or press Enter to go back): ")
    if product_number.isdigit() and 1 <= int(product_number) <= len(products):
        select_product = products[int(product_number) - 1]
        cart.add_to_cart(select_product)
        print(f"{select_product.name} added to the cart.")
    elif not product_number:
        print("Returning to customer menu.")
    else:
        print("Invalid product number. Please try again.")


def find_product_by_code(product_code):
    for product_list in [books, musics, movies]:
        for product in product_list:
            if product.product_code == product_code:
                return product
    return None


books = []
musics = []
movies = []

books.extend([
    Book("Legend of Drizzt: Homeland", "English", "Fantasy", "Book", 80, 15.0, "B00002", "R. A. Salvatore",
         "978-0-06-112008-4"),
    Book("Dune", "English", "Sci-Fi", "Book", 120, 18.0, "B00003", "Frank Herbert", "958-0-7432-7356-5"),
    Book("Hitchhiker's Guide to the Galaxy", "English", ["Sci-Fi", "Comedy"], "Book", 100, 20.0, "B00001",
         "Douglas Adams", "969-0-13-026730-1")
])

musics.extend([
    Music("Bohemian Rhapsody", "English", "Rock", "Music", 40, 25.0, "M00002", "Queen", "CD", 6),
    Music("Rolling in the Deep", "English", "Pop", "Music", 60, 30.0, "M00003", "Adele", "MP4", 4),
    Music("Dead Presidents II", "English", "Hip-Hop", "Music", 50, 150.0, "M00001", "Jay-Z", "MP4", 5)
])

movies.extend([
    Movie("Taxi Driver", "English", ["Crime", "Drama"], "Movie", 15, 25.0, "MV00002", ["Martin Scorsese"],
          ["Robert De Niro", "Jodie Foster"], "Turkish", "Dolby Digital"),
    Movie("Zodiac", "English", ["Crime", "Drama", "Mystery"], "Movie", 20, 35.0, "MV00003", ["David Fincher"],
          ["Jake Gyllenhaal", "Robert Downey Jr.", "Mark Ruffalo"], "Turkish", "Dolby Atmos"),
    Movie("Mad Max Fury Road", "English", ["Action", "Adventure", "Sci-Fi"], "Movie", 25, 30.0, "MV00001",
          ["George Miller"], ["Charlize Theron", "Tom Hardy"], "Turkish", "Dolby Atmos")
])


user = authenticate_user()

if user.role == "Admin":
    admin_menu(user)
else:
    customer_menu(user)
