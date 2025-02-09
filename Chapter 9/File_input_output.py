# ->> Volatile Memory: Volatile memory loses its data when the power supply is turned off.
# Example: RAM (Random Access Memory) is a type of volatile memory used for temporary data storage.

# ->> Non-Volatile Memory: Non-volatile memory retains its data even when the power is off.
# Example: Hard Drives, SSDs, and Flash Drives are common examples of non-volatile memory.

# Python provides robust file handling capabilities for reading, writing, and managing files efficiently.
# File handling uses built-in functions and methods like open(), read(), write(), append(), close(), etc.
# It's crucial to use proper file handling techniques to avoid errors and ensure smooth execution.

# Opening a file in different modes:
# 'r' -> read mode, 'w' -> write mode, 'a' -> append mode, 'rb' -> read in binary mode, 'rt' -> read in text mode.

# Example: Writing data to a file using 'w' mode
with open("example.txt", "w") as file:
    """
    This block opens 'example.txt' in write mode ('w').
    If the file doesn't exist, it is created.
    If the file exists, its content is overwritten.
    The 'with' statement ensures the file is automatically closed after the block execution.
    """
    file.write("Hello, World!\n")
    file.write("This is an example of writing to a file in Python.\n")
    # Write operations are buffered until the file is closed or flushed.

# Example: Appending data to a file using 'a' mode
with open("example.txt", "a") as file:
    """
    This block opens the file in append mode ('a').
    Content is added to the end of the file without modifying existing data.
    """
    file.write("This line is appended to the file.\n")

# Example: Reading the entire content of a file using 'r' mode
with open("example.txt", "r") as file:
    """
    Opens the file in read mode ('r') to access its content.
    The read() method retrieves the entire file content as a single string.
    """
    content = file.read()
    print("File Content:\n", content)

# Example: Reading a file line-by-line using readline()
with open("example.txt", "r") as file:
    """
    readline() reads one line at a time, making it efficient for large files.
    Useful when you need to process lines incrementally instead of loading the whole file into memory.
    """
    first_line = file.readline()  # Reads the first line
    second_line = file.readline()  # Reads the second line
    print("First Line:", first_line.strip())  # strip() removes trailing newline characters
    print("Second Line:", second_line.strip())

# Example: Reading all lines at once into a list using readlines()
with open("example.txt", "r") as file:
    """
    The readlines() method reads all lines from the file and returns them as a list of strings.
    Each string in the list represents one line from the file.
    """
    lines = file.readlines()
    print("Lines as List:", lines)

# Handling errors gracefully using try-except
try:
    with open("non_existent_file.txt", "r") as file:
        """
        This block attempts to open a file that doesn't exist.
        If the file is not found, a FileNotFoundError is raised, which is handled by the except block.
        """
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename or path.")

# Notes and Best Practices:
# 1. Always use the 'with' statement to handle files. It ensures files are closed properly after use.
# 2. Use the correct mode ('r', 'w', 'a', etc.) based on the intended operation.
# 3. Handle errors, like missing files or permission issues, using try-except blocks.
# 4. For reading large files, use readline() to process data line-by-line instead of loading the entire file.
# 5. Avoid hardcoding file paths. Use libraries like os.path for better portability.

# Output:
# This script demonstrates writing, appending, and reading files using Python's file handling methods.


# Open the file in read ('r') mode.
file = open("example.txt", "r")

try:
    # Read the content of the file.
    content = file.read()
    # Print the content that was read from the file.
    print("File Content:\n", content)
finally:
    # The finally block will always execute, even if an error occurs.
    # Here, we make sure to close the file to release resources.
    print("The file will be closed now.")
    # Close the file explicitly to avoid memory leaks and ensure changes are saved.
    file.close()
