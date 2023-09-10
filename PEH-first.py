#!/bin/python3

# #######
# Strings
# #######

print("This is the begining of strings")
print('\n')
# Print String "Hello World!" to the terminal.
print("hello world!")

# Single Quote Example
print('holla back world!')

# Print Multiple Lines (Triple Quote)
print("""This is the
begining of a long
string""")

# Can also concatenate strings together.
print("This string is " + "awesome!")

# Print a new line
print('\n')
print("Testing new line out.")

print("This is the end of Strings")
print('\n')
# ######
# Math
# ######

print("This is the begining of Math")
print('\n')

# Addition
print(50 + 50)

# Subtraction
print(50 - 25)

# Multiplication
print(50 * 5)

# Division
print(50 / 5)

# Follows standard Math Order of Operatins PEMDAS
print(50 + 50 - 50 * 50 / 50)

# Exponents
print(50 ** 2)

# Modulo - (Remainder) Takes what is left over
print( 50 % 6)

# Division with remainder (AKA Float)
print( 50 / 6) 

# Division with no remainder (or Float)
print(50 // 6)

print("This is the end of the Math Section")


print('\n')

# #####################
# Variables and Methods
# #####################

print("This is the start of the Variables and Methods section")
print('\n')

# Set the variable for quote and then printed the variable.

quote = "All is fair in love and war."
print(quote)

# Upper command will print the quote in all uppercase letters.

print(quote.upper())

# Lower command will print the quote in all lowercase letters.

print(quote.lower())

# Title command will print the quote out as a title.

print(quote.title())

# Counts letters and spaces of a string.

print(len(quote))

name = "Heath" #string
age = 33 #Integer
gpa = 3.7 #float (has decimal)

# Integers are whole numbers and the decimals will be dropped off and not rounded.

print(int(age))
print(int(30.1))
print(int(30.9))

# Example of a error in the below command.
# print("My name is " + name + " and I am " + age + " years old.")
# TypeError: can only concatenate str (not "int") to str

# Fixed version
print("My name is " + name + " and I am " + (str(age)) + " years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print("My name is " + name + " and I am " + (str(age)) + " years old.")

print('\n')

# ##########
# Functions
# ##########
print("Start of the functions section")

print('\n')

def who_am_i(): # This is a function without parameters.
	name = "Heath" # Local variable
	age = 30
	print("My name is " + name + " and I am " + (str(age)) + " years old.")
who_am_i()

def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

# Simple Addition

def add(x,y):
	print(x + y)

add(7,7)

# Multiplies x * y and places it into return.

def multiply(x,y):
	return x * y

multiply(7,7)

print(multiply(7,7))

# Calculates the Square Root

def square_root(x):
	print(x ** .5)
	
square_root(64)

# Defines the new line parameter to shorten up the repeatable task.
def nl():
	print('\n')
	
nl()

# ###############################################
# Boolean Expressions and Relational Operations
# ###############################################

nl()
print("This is the start of the Boolean Expressions and Relational Operations section")
nl()

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)

print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()

# Relational and Boolean Operators

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False

test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False

nl()

# #########################
# Conditional Statements (if / else)
# #########################

nl()

def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you!"

print(drink(3))
print(drink(1))

def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money."
	elif (age < 21) and (money >= 5):
		return "Nice try kid!"
	else:
		return "You are too young and too poor."

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

nl()

# ######
# Lists
# ######

# Lists typically have brackets []
nl()
print("This is the start of the lists section.")
nl()

movies = ["When Harry Met Sally", "The Hangover", "Spaceballs", "Star Wars"]

# Index starts with 0. So if you want to print the first index it would be [0] and not [1]

print(movies[0])
print(movies[1])
print(movies[2])
print(movies[3])

# Will not print the [0] or the last [3]. The expectation would be 1 + 2 only.
print(movies[1:3])

print(movies[1:])
print(movies[:1])
print(movies[-1]) # Returns last item in the list.

print(len(movies)) # Counts the amount of items in the list.
movies.append("JAWS") # Adds to the end.
print(movies)

movies.insert(2, "Hustle")
print(movies)

movies.pop() # Removes the last entry in a list.
print(movies)

movies.pop(0) # Removes the first index item in the list [0]
print(movies)

amber_movies = ['Just Go with it', '50 First dates']
print(amber_movies)

our_favorite_movies = movies + amber_movies
print(our_favorite_movies)

grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
print(grades)

# In the below example index 0 (first index is being focused and then within that index the 2nd entry [1] is being focused.

bobs_grade = grades [0][1]
print(bobs_grade)

# Here we are modifying the first index, but the second entry to change bob's grade from 82 to 83.
grades [0][1] = 83
print(grades)

nl()
# Tuples - Does not change ()
nl()

print("This is the start of the Tuples section")

grades = ("a", "b", "c", "d", "f")
# Neither of these commands work
# grades.pop()
# grades.append()

print(grades[0])
print(grades[1])
print(grades[2])
print(grades[3])
print(grades[4])

nl()
# #######
# Looping
# #######

print("This is the start of the looping secion")
nl()

# For loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)

# While Loops - Executes as long as True

i = 1

while i < 10:
	print(i)
	i += 1

nl()
# ################
# Advanced Strings
# ################

print("This is the start of the Advanced Strings section")
nl()

my_name = "Heath"
print(my_name[0]) # First Letter
print(my_name[-1]) # Last Letter

sentence = "This is a sentence."
print(sentence[:4])

print(sentence.split()) # This is a delimiter. Default is a space.

sentence_split = sentence.split()

sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = 'He said, "give me all your money"'
print(quote)

quote2 = "He said, 'give me all your money'"
print(quote2)

quote3 = "He said, \"give me all your money\""
print(quote3)

too_much_space = "               hello                "
print(too_much_space)
print(too_much_space.strip())
print(too_much_space)

print("A" in "Apple") # True
print("a" in "Apple") # False

letter = "A"
word = "Apple"

print(letter.lower() in word.lower()) # Improved way to do this.

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))

print("My favorite movie is %s." % movie)

# Most current way of doing this task.
print(f"My favorite movie is {movie}.")


nl()
# ############
# Dictionaries
# ############
print("This is the start of the dictionaries section")
nl()

# Key Value Pairs {}

drinks = {"White Russian": 7, "Old  Fashioned": 10, "Lemon Drop": 8} # Drink is the key, Price is the value.

print(drinks)
nl()

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)
nl()

employees['Legal'] = ["Mr. Frond"] # Adds new Key value pair
print(employees)
nl()

employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)
nl()

drinks['White Russian'] = 8
print(drinks)
nl()

print(drinks.get("White Russian"))
