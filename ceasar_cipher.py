import sys
import random  # Importing random module for generating random characters
from colorama import Fore, init  # Importing colorama for colored output

init()  # Initializing colorama

# Function to implement the Caesar cipher
def implement_caesar_cipher(message, key, decrypt=False):
    result = ""

    for character in message:
        if character.isalpha():  # Check if the character is alphabetic
            shift = key if not decrypt else -key  # Calculate the shift based on the key

            if character.islower():  # Check if the character is lowercase
                result += chr(((ord(character) - ord('a') + shift) % 26) + ord('a'))  # Encrypt lowercase character
            else:
                result += chr(((ord(character) - ord('A') + shift) % 26) + ord('A'))  # Encrypt uppercase character
        else:
            # Replace space with a random character from a predefined list
            result += random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?/") if character == " " else character
    return result

# Input from the user
text_to_encrypt = input(f"{Fore.GREEN}[?] Please enter the message: ")
key = int(input(f"{Fore.GREEN}[?] Please specify the shift length: "))

# Check if the key is within the valid range
if key > 25 or key < 0:
    print(f"{Fore.RED}[!] Your shift length should be between 0 and 25 ")
    sys.exit()

# Encrypt the message and display the result
encrypted_message = implement_caesar_cipher(text_to_encrypt, key)
print(f"{Fore.BLUE}[+] Encrypted message: {encrypted_message}")
