# ##############################################################################################################################
#
# Reading and Writing Files with Python3
#
# ##############################################################################################################################
# In Python3, reading and writing files is a common operation for working with data.
# Here's a quick and simple explanation of how to do it:
#
# Reading Files:
#
# To read data from a file, you can use the open() function to open the file in read mode ('r').
#
# You can then use methods like read(), readline(), or readlines() to read the file's contents.
#
# # Open a file in read mode
# with open('filename.txt', 'r') as file:
#    content = file.read()  # Read the entire file into a string
#
# Process the content
# print(content)
#
# ##############################################################################################################################
#
# Writing Files:
#
# To write data to a file, you can use the open() function with write mode ('w').
# Be careful because this will overwrite the existing file content if it exists.
# To append content, use 'a' mode.
#
# You can use the write() method to write data to the file.
#
# # Open a file in write mode (creates a new file or overwrites an existing one)
# with open('newfile.txt', 'w') as file:
#    file.write('Hello, world!\n')  # Write data to the file
#
# To append content to an existing file, use 'a' mode
# with open('existingfile.txt', 'a') as file:
#    file.write('Appending more content.\n')
#
# ##############################################################################################################################
#
# Closing Files:
# It's essential to close files using the with statement or the close() method to ensure proper resource management and data integrity.
#
# with open('filename.txt', 'r') as file:
#    content = file.read()
#
# File is automatically closed when the 'with' block exits
#
# ##############################################################################################################################
#
# These are the basic operations for reading and writing files in Python 3.
# They allow you to interact with external files and work with their contents in your Python programs.
#
# ##############################################################################################################################

# Note the file must exist for this to properly work. Otherwise the following error will appear
# FileNotFoundError: [Errno 2] No such file or directory: 'top-100.txt'
# When successful the entire file will be written out into the terminal.

f = open('top-100.txt')
print(f)

f = open('top-100.txt', 'rt')
print(f)

print(f.read())

print("---")

# Using the "f.seek(0)" resets back to the top allowing the command to read otherwise it will not read it and the following
# will be written []

f.seek(0)
print(f.readlines())

print("---")

# f.seek(0): This line sets the file's current position to the beginning (offset 0) of the file.
# In other words, it moves the file's "cursor" to the start of the file.
# for line in f:: This line starts a for loop that iterates over each line in the file f.
# It reads the file line by line and assigns each line to the variable line during each iteration.
# print(line.strip()): Inside the loop, this line prints the content of the current line.
# The strip() method is used to remove any leading or trailing whitespace (like spaces or newline characters) from the line.
# This ensures that you print the line without any extra spaces or formatting.
# f.close(): After the loop is done, this line closes the file f.
# Closing the file is essential to release system resources and ensure that all changes (if any) are saved to the file.
#
# So, in summary, this code snippet opens a file f, moves the file's cursor to the beginning, reads each line in the file,
# prints each line without leading or trailing whitespace, and finally closes the file.
# It's a common pattern for reading and processing the contents of a text file in Python.

f.seek(0)
for line in f:
    print(line.strip())
f.close()

print("---")

# In this example a file named test.txt is to be opened, if the file does not exist then a new file will be written.
# Once the file is open the next line will write some text into the file "test line!"
# The final line is to close the file out.

f = open("test.txt", "w")
f.write("test line!")
f.close()

# Switching to "a" we are appending the file to add in the additional text. If we failed to close the file after we
# would start to have duplicate entries each time we ran the program. Closing out the file is key to prevent duplicates.

print("---")

f = open("test.txt", "a")
f.write("test line two!")
f.close()

print("---")

print(f.name)
print(f.closed)
print(f.mode)

print("---")

# The Rockyou.txt file will have issues if using the f.readlines() command above. To resolve this we would use
# open('rockyou.txt, encoding='latin-1')
# Example Command

with open('rockyou.txt', encoding='latin-1') as f:
          for line in f:
            pass
