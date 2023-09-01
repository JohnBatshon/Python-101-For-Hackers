
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

