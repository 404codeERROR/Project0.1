# password_generator.py

import random
import string

def generate_password():
    try:
        length = int(input("Enter password length: "))
    except:
        print("Bruh, type a number 😅")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        print("You need to pick at least one character type 😅")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\nGenerated password: {password} 🔐")

def main():
    print("🔒 Password Generator 🔒")
    generate_password()

if _name_ == "_main_":
    main()