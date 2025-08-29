# error_handling.py
# This program asks for a filename and safely reads it.
# It shows errors if the file does not exist or cannot be read.

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
    print("\nFile content:")
    print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: Could not read the file.")
