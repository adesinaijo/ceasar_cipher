Caesar Cipher Encryption Script

This script encrypts messages using a Caesar cipher, featuring colored output via colorama, replacing spaces with random characters, and validating the shift key (0-25).
Features

    Implements the Caesar cipher for message encryption.
    Uses colorama for colored console output.
    Replaces spaces with random special characters for added obfuscation.
    Validates the shift key to ensure it is within the range of 0-25.

Requirements

    Python 3.x
    colorama library

Installation

Install the colorama library using pip:

bash

pip install colorama

Usage

Run the script and follow the prompts to enter a message and a shift key for encryption.
Example

bash

[?] Please enter the message: Hello World
[?] Please specify the shift length: 3
[+] Encrypted message: Khoor#Zruog

In this example, the message "Hello World" is encrypted with a shift length of 3, resulting in "Khoor#Zruog".
