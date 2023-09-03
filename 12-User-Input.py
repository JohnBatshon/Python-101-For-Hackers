# ##############################################################################################################################
#
# User Input
#
# ##############################################################################################################################
#
# User input in Python refers to the ability of a Python program to accept data or information directly from the user during runtime. This interaction allows users to provide input, which the program can then process and use to perform various tasks.
#
# In Python 3, you can obtain user input using the input() function. Here's how it works:
#
# user_input = input("Please enter some input: ")
#
# input("Please enter some input: "): This line of code displays the message "Please enter some input: " to the user, prompting them to enter some text. The text within the parentheses is called the "prompt" and is optional. You can customize it to provide instructions or context to the user.
#
# input(): This function reads a line of text entered by the user and returns it as a string. The user can type any text and press Enter. The input function then captures the entered text and stores it in the variable user_input.
#
# user_input = input("Please enter your name: ")
# print("Hello, " + user_input + "!")
#
# In this example, the program prompts the user to enter their name, captures the input as a string in the user_input variable, and then prints a greeting using the provided name.
#
# Keep in mind that the input() function always returns a string, so if you need to perform numerical calculations with the user's input, you may need to convert it to the appropriate data type (e.g., int or float) using functions like int() or float().
# 
# user_input = input("Please enter a number: ")
# number = int(user_input)
# result = number * 2
# print("Twice the number is:", result)
#
# In this case, we convert the user's input to an integer before performing a mathematical operation.
#
# ##############################################################################################################################

# This is the most simple example of a user input field. Unfortunately it is so simple the end use doesn't even know
# that the system is waiting for input.
# Result: End user is stuck because of bad programing.
# This example will be commented out to avoid this problem.
#
# test = input()
# print(test)

# In this example the first line prompts the user for input and is also greeted with a dialog "Enter the IP: "
# Once the user has entered the data the (test) variable will print it (assuming they entered an IP Address)

test = input("Enter the IP: ")
print(test)

#

while True:
    test = input("Enter the IP: ")
    print(">>> {}".format(test))
    if test == "exit":
        break
    else:
        print("exploiting..")

