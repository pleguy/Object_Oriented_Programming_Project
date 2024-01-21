from Users.user import User


class Customer(User):
    def __init__(self, username):
        super().__init__(username, "Customer")
