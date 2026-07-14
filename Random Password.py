import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    chars = ""

    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


while True:
    print("\n===== RANDOM PASSWORD GENERATOR =====")

    # Length Validation
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Character Type Selection
    print("\nSelect character types:")
    upper = input("Include Uppercase Letters? (y/n): ").lower() == 'y'
    lower = input("Include Lowercase Letters? (y/n): ").lower() == 'y'
    digits = input("Include Numbers? (y/n): ").lower() == 'y'
    symbols = input("Include Symbols? (y/n): ").lower() == 'y'

    selected_types = sum([upper, lower, digits, symbols])

    # Validation: At least 2 types selected
    if selected_types < 2:
        print("\nError: Please select at least TWO character types.")
        continue

    password = generate_password(length, upper, lower, digits, symbols)

    print("\nGenerated Password:")
    print(password)

    # Generate Again Option
    again = input("\nGenerate another password? (y/n): ").lower()
    if again != 'y':
        print("Thank you for using Password Generator!")
        break