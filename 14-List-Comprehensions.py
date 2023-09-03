# ########################################################################################################################################
#
# List Comprehensions
#
# ########################################################################################################################################
#
# In Python, list comprehensions are a concise way to create lists by applying an expression to each item in an existing 
# collection and optionally filtering the items based on a condition.
#
# Here's a simple breakdown:
# 
# - **Purpose**: Create a new list.
# - **Syntax**: `[expression for item in iterable if condition]`.
# - **Expression**: Operation applied to each item.
# - **Item**: Represents each element in the original collection.
# - **Iterable**: The original source of data.
# - **Condition (optional)**: Filters items based on a condition.
#
# Examples:
# 
# 1. Creating a list of squares: `[x**2 for x in numbers]`.
# 2. Filtering even numbers: `[x for x in numbers if x % 2 == 0]`.
# 3. Creating a list of uppercase strings: `[word.upper() for word in words]`.
#
# List comprehensions simplify list creation and are particularly handy for straightforward operations and filtering.
#
# ########################################################################################################################################

list1 = ['a', 'b', 'c']
print(list1)

list2 = [x for x in list1]
print(list2)

list3 = [x for x in list1 if x == 'a']
print(list3)

list4 = [x for x in range(5)]
print(list4)

list5 = [hex(x) for x in range(5)]
print(list5)

list6 = [hex(x) if x > 0 else "X" for x in range(5)]
print(list6)

list7 = [x * x for x in range(5)]
print(list7)

list8 = [x for x in range(5) if x == 0 or x == 1]
print(list8)

list9 = [[1,2,3],[4,5,6],[7,8,9]]
print(list9)

list10 = [y for x in list9 for y in x]
print(list10)

set1 = {x + x for x in range(5)}
print(set1)

list11 = [c for c in "string"]
print(list11)

print("".join(list11))
print("-".join(list11))

list12 = []
for c in "string":
    list12.append(c)
print(list12)
