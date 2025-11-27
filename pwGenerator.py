#Generate a random password of length n

import random
import string

password_len = 12
password = ''
print("Welcome to Password Generator!")

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

all_characters = string.ascii_letters + string.digits + string.punctuation

for i in range(password_len):
    password += random.choice(all_characters)

print(f"Your generated password is: {password}")