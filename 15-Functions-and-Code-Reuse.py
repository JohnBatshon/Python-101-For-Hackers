# ##############################################################################################################################
#
# Dunctions and Code Reuse
#
# ##############################################################################################################################
#
# Functions in Python allow you to:
#
# Encapsulate Code: Group code into reusable blocks.
# Modularize: Divide your program into manageable parts.
# Reuse: Call the same code multiple times.
# Parameters: Pass data into functions.
# Return Values: Get results from functions.
# Abstraction: Hide implementation details.
# Enhance Readability: Make code more organized and understandable.
#
# ##############################################################################################################################

def function1():
    print("hello from function!")

function1()
function1()

def function2():
    return "hello from function2!"

return_from_function2 = function2()
print(return_from_function2)

def function3(s):
    print("\t{}".format(s))

function3("parameter")
function3("parameter2")

def funciton4(s1, s2):
    print("{} {}".format(s1,s2))
funciton4("s1","s2")
funciton4("Any","Thing")
funciton4("Hello","World!")

funciton4(s1="Thing",s2="Smelly")
funciton4(s2="Cheese",s1="Burger")

def function5(s1 = "default"):
    print("{}".format(s1))

function5()
function5("anything")

def function6(s1, *more):
    print("{} {}".format(s1, " ".join([s for s in more])))

function6("function6")
function6("function6", "a")
function6("function6", "a", "b", "c")

def function7(**ks):
    for a in ks:
        print(a, ks[a])

function7(a="1", b="2", c="3")

def function8(s, f, i, l):
    print(type(s))
    print(type(f))
    print(type(i))
    print(type(l))

function8("string", 1.0, 1, ['l','i','s','t'])

v = 100
print(v)

def function9():
    v = 5
    v += 1
    print(v)

function9()
print(v)


v = 100
print(v)

def function9a():
    global v
    v += 1
    print(v)

function9a()
print(v)

def function10():
    print("hello from function10")
    

# def function10():
#    print("hello from function 10")

def function11():
    function10()    
    print("hello from function 11")

