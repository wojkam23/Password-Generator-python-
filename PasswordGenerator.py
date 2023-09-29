import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the password length: "))

if password_length > 0:
    password = generate_password(password_length)
    print("Generated password:", password)
else:
    print("The password length must be greater than zero.")
