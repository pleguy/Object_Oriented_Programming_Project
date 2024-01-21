from Users.user import User


class Admin(User):
    def __init__(self, username):
        super().__init__(username, "Admin")

    def update_product_info(self, product):
        print(f"Admin {self.username} updated product information for {product.name}.")