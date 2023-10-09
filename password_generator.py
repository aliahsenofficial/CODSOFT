import random
import string

# Function to generate a random password based on user's choice
def generate_password(length, use_chars):
    # Define character sets based on user's choice
    char_sets = {
        '1': string.ascii_letters,                            # Only alphabets
        '2': string.ascii_letters + string.digits,            # Alphabets + numbers
        '3': string.ascii_letters + string.punctuation,       # Alphabets + special characters
        '4': string.ascii_letters + string.punctuation + string.digits  # Alphabets + special characters + numbers
    }

    # Check if the user's choice is valid
    if use_chars not in char_sets:
        return "Invalid choice"

    # Generate a random password using the chosen character set
    password = ''.join(random.choice(char_sets[use_chars]) for _ in range(length))
    
    return password

# Prompt the user for the desired password length
try:
    password_length = int(input("Enter the desired password length: "))
    use_chars = input("Choose the type of characters for the password:\n"
                      "1. Only alphabets\n"
                      "2. Alphabets + numbers\n"
                      "3. Alphabets + special characters\n"
                      "4. Alphabets + special characters + numbers\n>> ")

    if password_length <= 0:
        print("Password length should be a positive number.")
    else:
        # Generate and display the password
        generated_password = generate_password(password_length, use_chars)
        if generated_password == "Invalid choice":
            print("Invalid choice. Please select a valid option.")
        else:
            print("Generated Password:", generated_password)
except ValueError:
    print("Invalid input. Please enter a valid number for password length.")
