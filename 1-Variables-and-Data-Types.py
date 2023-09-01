name = "john"
print(name)

name_length = 4
print(name_length)

name, name_length = "john", 4

print(type(name))
print(type(name_length))

name_length = int("4")
print(type(name_length))

# The below command will not work because the name John is not an integer.
# name = int("john")

# Case sensitvity makes a difference. In the example below the 2 varables are the same with 1 exception of a capital letter.
# This causes 2 different variables to exists and can cause some confusion.
# It is best to standardize when using varables (i.e. always lowercase)

name_length = 4
Name_length = 5

print(name_length)
print(Name_length)

# When using the list varable it is best to use brackets, quotations, and commas to for each item in the list
# i.e. ["87", "12", "77"]
# i.e. ["John", "Andy", "Mike"]
name_list = ["John", "Jane", "Jenn"]
print(type(name_list))
print(name_list)

name1, name2, name3 = name_list
print(name1)
print(name2)
print(name3)

name_tuple = ("Mike", "Hank", "Andy")
print(type(name_tuple))
print(name_tuple)

name_dictionary = {"John": 4, "Jane": 7}
print(type(name_dictionary))
print(name_dictionary)

name_boolean = True
print(type(name_boolean))
print(name_boolean)

name_range = range(6)
print(type(name_range))
print(name_range)

name_bytes = b"john"
print(type(name_bytes))
print(name_bytes)

