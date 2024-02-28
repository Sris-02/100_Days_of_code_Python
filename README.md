# 100 Days of Code

# Day 1 -

python print function:
``` 
  print("hello world!")
```
string concatenation :
```
print("Hello " + "Everyone!")
```
input function :
```
input("What is your name?")
```
After that , exploring the len function, python variables, ...

#PROJECT-1 :
```
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)
```

# Day 2 -

#Data Types

#Strings : 
> pulling out a particular element from a string is called subscripting
> number in the square brackets determines which character you want to pull out
```
print("Hello"[4])
print("Hello"[0])
```
 concatenating strings :
 ```
print("123" + "345")
```

#Integer :
> whole numbers without any decimal places -
```
print(123 + 345)
```
> underscores can be used as commas in large numbers -
```
print(123_456_789)
```

#Float :
> numbers with decimal places
```
print(3.14159)
```
> floating point number

#Boolean :
```
print(True)
print(False)
```

#Type Error, Type Checking and Type Conversion :
```
#len(4837)

num_char = len(input("what is your name? "))

# print("Your name has " + num_char + " characters.")
# for knowing the type of data
print(type(num_char))

# conversion of data type
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")
```
```
a = 123
print(type(a))
```

 conversion or type casting :
 ```
a = str(123)
print(type(a))
a = float(123)
print(type(a))

print(70 + float("100.5"))

print(str(70) + str(100))
```

#data type exercise :
```
two_digit_number = input("Enter two digit number: ")
# check the data type 
print(type(two_digit_number))
# get the first and second digits using subscripting then convert string to int.
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# then add the two digits together
print((int(two_digit_number[0])) + (int(two_digit_number[1])))
```

