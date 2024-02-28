#Data Types

# Strings
# pulling out a particular element from a string is called subscripting
# number in the square brackets determines which character you want to pull out
print("Hello"[4])
print("Hello"[0])

# concatenating strings
print("123" + "345")

# Integer
# whole numbers without any decimal places
print(123 + 345)
# underscores can be used as commas in large numbers
print(123_456_789)

# Float
# numbers with decimal places
print(3.14159)
# floating point number

# Boolean

print(True)
print(False)

# Type Error, Type Checking and Type Conversion
# len(4837)

num_char = len(input("what is your name? "))
# print("Your name has " + num_char + " characters.")
# for knowing the type of data
print(type(num_char))

# conversion of data type
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a))
# conversion or type casting
a = str(123)
print(type(a))
a = float(123)
print(type(a))

print(70 + float("100.5"))

print(str(70) + str(100))
