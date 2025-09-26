import random

def generate_password(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_-+=<>?/"

    all_chars = letters + numbers + symbols
    password = ""
    for _ in range(length):
        password += random.choice(all_chars)
    return password

try:
    length = int(input("Enter desired password length: "))
    if length < 6:
        print("Password too short. Use at least 6 characters.")
    else:
        pwd = generate_password(length)
        print("Generated Password:", pwd)
except ValueError:
    print("Please enter a valid number.")
