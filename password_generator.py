import random
import string

def generate_password():
    length = int(input("Enter the length of the password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    if length < 6 or length > 15:
        print("Password must be between 6 and 15 characters")
        return False
    else:
        for i in range(length):
            password += random.choice(characters)
    return password

result = generate_password()
if result:
    print("Your password is:", result)
else:
    print("Password generation failed")

