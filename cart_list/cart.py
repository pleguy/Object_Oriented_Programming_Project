class Cart:
    def __init__(self):
        self.products = []
        self.total_price = 0

    def add_to_cart(self, product):
        if len(self.products) < 5:
            self.products.append(product)
            self.total_price += product.calculate_discount()
            print(f"{product.name} added to the cart.")
        else:
            print("Cart is full. Cannot add more products.")

    def view_cart(self):
        print("\nShopping Cart:")
        for product in self.products:
            print(f"{product.name} - ${product.calculate_discount()}")
        print(f"Total Price: ${self.total_price}")