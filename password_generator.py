import random # Used to randomly select characters to include in the password. 
import string # Imports the string module for ASCII characters (lower & uppercase) and digits (0 to 9).

# Pseudocode: Define a function named generate_password that takes three parameters:
# - min_length: The minimum length of the generated password
# - numbers: A flag to include numbers in the password or not
# - special_characters: A flag to include special characters in the password or not

def generate_password(min_length, numbers=True, special_characters=True):
    # Initialize a variable with all ASCII letters
    letters = string.ascii_letters 
    # Initialize a variable with all digits
    digits = string.digits 
    # Initialize a variable with all special characters
    special = string.punctuation 
    
    # Start with a character set that includes only ASCII letters
    characters = letters
    
    # # Pseudocode: If numbers should be included (if numbers=True), add digits to the character set.
    if numbers:
        characters += digits
    
    # Pseudocode: If special characters should be included (if special_characters=True), add special characters to the character set.
    if special_characters:
        characters += special
    
    # Initialize variables to hold the password and status flags
    pwd = "" # Initialises an empty string for the password 
    meets_criteria = False # This is a box named meets_criteria, and you're putting the value False in it. 
    # Later on, you'll check if the password meets certain conditions (like having numbers or special characters). If it does, you'll change this to True.
    has_number = False # This is a box named has_number, and you're putting the value False in it. 
    # This is to keep track of whether your password has any numbers in it. If you later add a number to your password, you'll change this to True.
    has_special = False # This is another box, and it's just like has_number
    #  it keeps track of whether your password has any special characters (like !, @, #, etc.).
    
    # Pseudocode: Loop until the password meets the criteria and reaches the minimum length
    while not meets_criteria or len(pwd) < min_length:
        # Pick a random character from the character set and add it to the password
        new_char = random.choice(characters)
        pwd += new_char

        # Pseudocode: If the new character is a digit, set has_number to True
        if new_char in digits:
            has_number = True

        # Pseudocode: If the new character is a special character, set has_special to True
        elif new_char in special:
            has_special = True

        # Assume that the password now meets the criteria
        meets_criteria = True

        # Pseudocode: If numbers are required, set meets_criteria based on has_number
        if numbers:
            meets_criteria = has_number

        # Pseudocode: If special characters are required, adjust meets_criteria accordingly
        if special_characters:
            meets_criteria = meets_criteria and has_special

    # Return the generated password
    return pwd

# Pseudocode: Collect user inputs for minimum length, numbers, and special characters
min_length = int(input("Enter the minimum length: "))  
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

# Generate the password and print it
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)