# File Read & Write Challenge

# Read from an existing file
with open("input.txt", "r") as file:
    content = file.read()

# Modify content (convert to uppercase)
modified_content = content.upper()

# Write to a new file
with open("output.txt", "w") as file:
    file.write(modified_content)

print("File has been read and modified content written to output.txt")
