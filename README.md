# Password Generator

## Introduction

This project serves as my introduction to Python programming and has taught me the core syntax and principles of the language. I'm eager to further expand my skill set and take on more ambitious projects in Python and other languages. 

## Overview

This project is a simple yet powerful password generator written in Python. It allows the user to generate passwords based on different criteria such as length, inclusion of numbers, and special characters. This is my very first Python project.

## Features

- Generate random passwords with a user-specified minimum length.
- Option to include numbers in the generated password.
- Option to include special characters in the generated password.

## What I Learned

- Basic Python syntax and operations.
- How to use Python's `random` and `string` modules to randomly select characters.
- Basic understanding of conditional statements and loops.
- User input validation and conversion.
- The importance of password complexity and criteria.

## Code Explanation

The code makes use of Python's built-in libraries, `random` and `string`, to generate a random sequence of characters based on user input.

The `generate_password` function is the core of the application. It takes in three parameters:

- `min_length`: The minimum length for the password.
- `numbers`: A boolean value to determine if numbers should be included.
- `special_characters`: A boolean value to determine if special characters should be included.

The function loops until it creates a password that meets all the specified criteria.

## Installation and Usage

1. Clone the repository or download the code.
2. Navigate to the folder containing the `password_generator.py` file.
3. Run `python password_generator.py` in your terminal.
4. Follow the on-screen instructions to generate your password.