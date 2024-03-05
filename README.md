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

#PROJECT-1 : A Band/Group Name Generator
```
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)
```

# Day 2 -

#Data Types

#Strings : 
pulling out a particular element from a string is called subscripting
number in the square brackets determines which character you want to pull out
```
print("Hello"[4])
print("Hello"[0])
```
 concatenating strings :
 ```
print("123" + "345")
```

#Integer :
whole numbers without any decimal places -
```
print(123 + 345)
```
underscores can be used as commas in large numbers -
```
print(123_456_789)
```

#Float :
numbers with decimal places
```
print(3.14159)
```
floating point number

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
adds the digits in a 2 digit number.e.g. if the input was 35, then output should be 3 + 5 = 8
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

#Mathematical Operations :
```
print(3 + 5)
print(7 - 3)
print(3 * 2)
print(6 / 3)

print(type(6 / 3)) is float
print(2 ** 3)
```
#PEMDAS:
> Parentheses
> Exponents
> Multiplication
> Division
> Addition
> Subtraction
e.g.
```
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
```
#BMI - Calculator :
bmi = weight(kg) / height ** 2 (m**2)
convert the type of height i.e. str to float, similarly with weight 
```
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
new_height = float(height)
new_weight = float(weight)
BMI = new_weight / (new_height) ** 2
print(BMI)

bmi_as_int = int(BMI)
print(bmi_as_int)
```

#Number Manipulation and F Strings in Python :
```
print(round(8 / 3))
```
round upto 2 decimal places
```
print(round(8 / 3, 2))
```
floor division:
8 // 3 gives 2 and here, 4 / 2 gives 2.0
```
print(8 // 3)
```
shorthand operators :
```
result = 4 / 2
result /= 2
print(result)
```
```
score = 0
#user scores a point
score += 1

print(score)
```

#f-string :
It help in coverting the data type rather than manually changing the data type that is not handy.
Add f character in front of string and start adding values and that's all.

```
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
```

#Life in Weeks - Exercise : 
```
age = input("What is your current age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int

days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

msg = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left."

print(msg)
```

#PROJECT-2 : Tip Calculator 
```
#If the bill was $150.00, split between 5 people, with 12% tip.


print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
cal_tip = tip / 100
total_tip = bill * cal_tip
total_bill = bill + total_tip

#Each person should pay (150.00 / 5) * 1.12 = 33.6
people_no = int(input("How many people to split the bill? "))
per_person_bill = total_bill / people_no


#Format the result to 2 decimal places = 33.60
final_amt = round(per_person_bill, 2)
print(f"Each person should pay : ${final_amt}")
```

# Day 3 -

#conditional statements -
```
# water_level = 50
# if water_level > 80:
#   print("Drain water")
# else:
#   print("Continue")

print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster! ")
else :
  print("Sorry, you have to grow taller before you can ride. ")
```


#Odd or Even exercise :
```
number = int(input("Which number do you want to check? "))
if number % 2 ==0:
  print("This is an even number. ")
else:
  print("This is an odd number. ")
```  

#Nested if statements and elif statements -

```
print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm? "))
if height >=120:
  print("You can ride the rollercoaster! ")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5. ")
  elif age <= 18:
    print("Please pay $7. ")
  else :
    print("Please pay $12. ")
else:
  print("Sorry, you have to grow taller beforre you can ride. ")
  ```

 #BMI 2.0 exercise using nested if statements -

 ```
height = float(input("enter your height in m: "))
weight = float(input("enter you weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight. ")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight. ")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight. ")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese. ")
else:
  print(f"Your BMI is {bmi}, you are clinically obese. ")
```

#Leap year exercise -

e.g. 2000 / 4 = 500 (Leap)
     2000 / 100 = 20 (Not leap)
     2000 / 400 = 5 (Leap)

```
# Leap year exercise
year = int(input("Which year do you want to check? "))
if year % 4 ==0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year. ")
    else :
      print("Not a leap year. ")
  else:
    print("Not a leap year. ")
else:
  print("Leap year. ")
```

#Multiple if statements in succession -

fun exercise to go ahead that include the bill payment according to, whether photo taken or not.

```
print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
  print("You can ride the rollercoaster! ")
  age = int(input("What is your age? "))
  
  if age < 12:
    bill = 5
    print("Child tickets are $5. ")
    
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7. ")
    
  else:
    bill = 12
    print("Adult tickets are $12. ")
    
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    print(f"Your final bill is ${bill + 3}.")
    
else:
  print("Sorry, you have to grow taller before you can ride. ")
```

#Pizza order exercise :
```
print("Welcome to Python Pizza Deliveries! ")
size = input("What size pizza do you want? S, M, or L.")
add_pepperoni = input("Do you want pepperoni? Y or N. ")
extra_cheese = input("Do you want extra cheese? Y or N. ")

bill = 0
if size == 'S':
  bill += 15
  
elif size == 'M':
  bill += 20
  
else:
  bill += 25
  
if add_pepperoni == 'Y':
   if size == 'S':
       bill += 2
   else :
       bill += 3

if extra_cheese == 'Y':
  bill += 1
print(f"Your final bill is: ${bill}. ")
```

#Love Calculator :
example exercise - 
```
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_str = name1 + name2
lower_case_str = combined_str.lower()
t = lower_case_str.count("t")
r = lower_case_str.count("r")
u = lower_case_str.count("u")
e = lower_case_str.count("e")
true = t + r + u + e

l = lower_case_str.count("l")
o = lower_case_str.count("o")
v = lower_case_str.count("v")
e = lower_case_str.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score} , you go together like coke and mentos. ")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else :
  print(f"Your score is {love_score}.")
```

#PROJECT-3 : Treasure Island

>ASCII ART for this figure...
```
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")


  ```


  # Day 3 -

  #Randomisation and Python Lists
  #randomisation is used to generate random numbers.
```
  import random
  #import my_module

  random_integer = random.randint(1, 10)
  print(random_integer)

  randomFloat = random.random() * 5
  print(randomFloat)

  love_score = random.randint(1, 100)
  print(f"Your love score is {love_score}")
```

list in Python : 


```
  states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

  num_of_states = len(states_of_america)

  print(states_of_america[num_of_states - 1])
```
Another example : 
```
  #dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]


  fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
  vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

  dirty_dozen = [fruits, vegetables]

  print(dirty_dozen)
```
