import random
import string
print("Password Generator")
print("Enter password length")
length = int(input())
chars = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(length):
    password += random.choice(chars)
print("Generated Password:", password)
