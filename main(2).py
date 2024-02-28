#Data Types

# Strings
# subscripting
print("Hello"[4])
print("Hello"[0])

# concatenating strings
print("123" + "345")

# Integer

print(123 + 345)
# underscores can be used as commas in large numbers
print(123_456_789)

# Float
print(3.14159)

# Boolean

print(True)
print(False)

# Type Error, Type Checking and Type Conversion

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

# data type exercise
two_digit_number = input("Enter two digit number: ") 
print((int(two_digit_number[0])) + (int(two_digit_number[1])))

# Mathematical Operations
print(3 + 5)
print(7 - 3)
print(3 * 2)
print(6 / 3)
# print(type(6 / 3)) is float
print(2 ** 3)
# PEMDAS
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)


# BMI - Calculator :
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
new_height = float(height)
new_weight = float(weight)
BMI = new_weight / (new_height) ** 2
print(BMI)
bmi_as_int = int(BMI)
print(bmi_as_int)

# Number Manipulation and F Strings in Python
print(round(8 / 3))
# round upto 2 decimal places
print(round(8 / 3, 2))
# floor division
print(8 // 3)
result = 4 / 2
result /= 2
print(result)

score = 0
# user scores a point
score += 1

print(score)

# f-string
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

age = input("What is your current age?")
#Life in Weeks - Exercise : 
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
msg = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left."
print(msg)
