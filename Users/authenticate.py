from Users.admin import Admin
from Users.customer import Customer


def authenticate_user():
    print("LOGIN")
    username = input("Enter username: ")
    role = input("Enter '*' for Admin or press Enter for Customer: ")

    if role == '*':
        return Admin(username)
    else:
        return Customer(username)
