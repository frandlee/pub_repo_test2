import os

# Simple function that takes user input to list files in a directory
def list_directory(directory):
    # Vulnerable to command injection
    os.system(f'ls {directory}')

# Insecure way of taking input from user
user_input = input("Enter a directory name to list its contents: ")

# Calling the vulnerable function with the user input
list_directory(user_input)