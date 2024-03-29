
# Example Basic String
string1 = "I am a string!"
print(string1)

# Example String using single quotation marks in placed of double
string2 = 'I am also a string!'
print(string2)

# Example String using 3 double quotation marks (Multi-Line String)
string3 = """Hey all I am a string as well!
Although I have more to say.
Good job reading everthing I had to say!"""
print(string3)

# When using quotations inside of a string using the \ command will prevent it from closing the string too early.
string4 = "I\"m a string"
print(string4)

# Using single quotes
string5 = 'I\'m a sting'
print(string5)

# Using Double Quotes with a single quote inside
string5a = "I'm a string"
print(string5a)

# Example of how to extend the string to a 2nd line with the \n command.
string6 = "I\" a string\nI\"m on another line."
print(string6)

# Example of wanting to include a \ in your command by using a double \\
string6a = "\\ \x41\x42\x43"
print(string6a)

# Example of printing 10 a's in a string
string7 = "aaaaaaaaaa"
print(string7)
print(len(string7))

# Example of printing 10 a's by multiplying 1 a * 10
string7a = "a" * 10
print(string7a)
print(len(string7a))

# Example resulting in a True / False statement if the word "string" shows up in the variable string4 & string7
# In string4 it is infact true that "string" shows up which prints out "true"
print("string" in string4)
# In string7 it is infact true that "string" shows up which prints out "false"
print("string" in string7)

# Example using the .startswith command to show true or false statements if the string starts with the specified character
print(string4.startswith("I"))
print(string4.startswith("n"))

# Example using the .index command to indicate what character # starts the phrase specified "string"
# The output is 6 because there are 6 characters before the word string in string4
# "I"m a string"
print(string4.index("string"))

# How to force a string into upper and lower case letters
print(string4.upper())
print(string4.lower())

# Example showing how to remove extra spaces in a messy string with the .strip command
messy_string = "   Messy string!   "
print(messy_string)
print(messy_string.strip())

# Example of changing the ! to a ? using the .replace command. 
print(messy_string.replace("!","?"))

# Example of chaining in the .replace & .strip command to complete both tasks
print(messy_string.replace("!","?").strip())

# Example of using the .replace to change out a whole word
print(messy_string.replace("string","example"))

# Example of splitting the string based on the space between the 2 words.
print(messy_string.split())

# Example of splitting the string based on a comma
messy_string2 = "Messy,String!"
print(messy_string2)
print(messy_string2.split(","))

string4 = "I am a string!"
print(string4)
print(string4.encode())
print(string4.encode("utf-8"))

# Right Adjust to 25 characters total since the string was short additional spaces were added to the left.
print(string4.rjust(25))
print(string4.rjust(25, "X"))

# I assume this did the same but added the spaces to the end or right side of the string.
print(string4.ljust(25))
print(string4.ljust(25, "X"))

# Concatinating 2 strings together
print("I am "+ "a string")

# print("String 4 is " + len(string4) + " characters long!")
print("String 4 is " + str(len(string4)) + " characters long!")

# Showing the difference of adding 2 intergers versus 2 strings
# Interger adds the 2 numbers together resulting in = 2
# 2 Strings being added together resulting in = 11
print(1 + 1)
print(type(1 + 1))
print("1" + "1")
print(type("1" + "1"))

# Using a placeholder {}
print("String4 is {} characters long!".format(len(string4)))

# Using multiple placeholders to list Strings, Floats, and Hexidecimal Numbers
print("{} {} {}".format(len(string4), 5.0, 0x12))
print("{0} {2} {1}".format(len(string4), 5.0 , 0x12))

print("{length}".format(length=len(string4)))

# Setting the varable of length as len(string4) then printing in the length into the next line
length = len(string4)
print(f"string4 is {length} character long!")

# Printing as an integer.
print("string4 is {length} characters long!".format(length=len(string4)))

# Printing as a float with multiple examples showing longer decimal numbers.
print("string4 is {length:.1f} characters long!".format(length=len(string4)))
print("string4 is {length:.2f} characters long!".format(length=len(string4)))
print("string4 is {length:.3f} characters long!".format(length=len(string4)))
print("string4 is {length:.4f} characters long!".format(length=len(string4)))
print("string4 is {length:.5f} characters long!".format(length=len(string4)))

# Hex
print("string4 is {length:x} characters long!".format(length=len(string4)))

# Binary
print("string4 is {length:b} characters long!".format(length=len(string4)))

# Octal
print("string4 is {length:o} characters long!".format(length=len(string4)))

print("string4 is %d characters long!" % len(string4))
print("string4 is %f characters long!" % len(string4))
print("string4 is %x characters long!" % len(string4))
