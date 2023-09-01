valid = True
not_valid = False

print(valid)
print(type(valid))
print(not_valid)
print(type(not_valid))


print(valid == True)
print(not_valid == True)

print(valid != True)
print(not_valid != True)

print(not valid)
print(not not_valid)

print("_-_-_-_-_")

print((10 < 9) == True)
print((10 == 10) == True)
print((10 != 10) == True)
print((10 >= 10) == True)
print((10 <= 10) == True)
print((10 > 9) == True)

print("_-_-_-_-_")

print((10 < 9))
print((10 == 10))
print((10 != 10))
print((10 >= 10))
print((10 <= 10))
print((10 > 9))

print("_-_-_-_-_")

print(10 > 5 and 10 < 5)
print(10 > 5 or 10 < 5)

print(bool(0))
print(bool(1))


print("_-_-_-_-_")

print(bool(0) == False)
print(bool(1) == True)

print("_-_-_-_-_")
print("10 + 10")
print(10 + 10)

print("_-_-_-_-_")

print("10 - 10")
print(10 - 10)

print("_-_-_-_-_")

print("10 / 10")
print(10 / 10)

print("_-_-_-_-_")

print("10 // 10")
print(10 // 10)

print("_-_-_-_-_")

print(10 / 3)
print(10 // 3)
print(10 % 3)

print("_-_-_-_-_")

print("10 * 10")
print(10 * 10)

print("_-_-_-_-_")

print("10 ** 10")
print(10 ** 10)

print("_-_-_-_-_")

print("10 % 10")
print(10 % 10)

print("_-_-_-_-_")

x = 10
print(x)

x = x + 1
print(x)

x += 1
print(x)

x -= 1
print(x)

x *= 1
print(x)

x /= 1
print(x)

print("_-_-_-_-_")

x *= 5
print(x)

x /= 5
print(x)

print("_-_-_-_-_")

x = 13
print(bin(x))
print(bin(x)[2:].rjust(4,"0"))

print("_-_-_-_-_")

y = 5
print(y)
print(bin(y))
print(bin(y)[2:].rjust(4,"0"))

print("_-_-_-_-_")

# Bitwise AND
print(bin(x & y)[2:].rjust(4,"0"))
print(x & y)

# Bitwise OR
print(bin(x | y)[2:].rjust(4,"0"))

print("_-_-_-_-_")

print(bin(x >> 1)[2:].rjust(4,"0"))
print(bin(x >> 2)[2:].rjust(4,"0"))
print(bin(x >> 3)[2:].rjust(4,"0"))
print(bin(x >> 4)[2:].rjust(4,"0"))

print("_-_-_-_-_")

print(bin(x << 1)[2:].rjust(4,"0"))
print(bin(x << 2)[2:].rjust(4,"0"))
print(bin(x << 3)[2:].rjust(4,"0"))
print(bin(x << 4)[2:].rjust(4,"0"))

print("_-_-_-_-_")