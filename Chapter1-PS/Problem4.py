import os  # Import the os module to interact with the operating system

# Specify the directory path (use '.' for current directory)
directory_path = '/'  # Set the path of the directory to list

try:
    contents = os.listdir(directory_path)  # Get a list of all files and folders in the specified directory
    print(f"Contents of directory '{directory_path}':")  # Print a header message
    for item in contents:  # Loop through each item in the directory
        print(item)  # Print the name of the item (file or folder)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")  # Handle case where directory is not found
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")  # Handle case where access is denied