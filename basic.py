# print() displays something on the screen
print("Hello World!")

# Printing numbers
print(100)

# Printing multiple values
print("My name is", "Siraj")

# Calculation inside print()
print(10 + 20)

# A variable stores a value
name = "Siraj"
age = 21
height = 5.8

print(name)
print(age)
print(height)

# Variables can be changed
age = 22
print("Updated age:", age)

# String = text
name = "Siraj"

# Integer = whole number
age = 21

# Float = decimal number
height = 5.8

# Boolean = True or False
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# input() takes information from the user
user_name = input("Enter your name: ")

print("Hello", user_name)

# This is a single-line comment.
# Python ignores comments.
# Comments are used to explain code.

# Example:
# Store the user's age
user_age = 21

print(user_age)

# String -> Integer
number_text = "25"
number = int(number_text)

print(number)
print(type(number))

# String -> Float
price_text = "99.50"
price = float(price_text)

print(price)
print(type(price))

# Number -> String
age = 21
age_text = str(age)

print(age_text)
print(type(age_text))

# Input normally returns a string,
# so convert it to int when doing calculations.
user_age = int(input("Enter your age: "))

print("Next year you will be", user_age + 1)

name = "Siraj"

# Find length
print("Length:", len(name))

# Uppercase
print(name.upper())

# Lowercase
print(name.lower())

# Join strings
first_name = "Siraj"
last_name = "Khan"

full_name = first_name + " " + last_name

print(full_name)

# Repeat a string
print("Hello " * 3)

# Access characters
# Python starts counting from 0
print(name[0])
print(name[1])
print(name[2])

# Last character
print(name[-1])

# Slicing
# Gets characters from index 0 up to (but not including) 3
print(name[0:3])

# AND
# Both conditions must be True

age = 21
has_id = True

if age >= 18 and has_id:
    print("You can enter.")


# OR
# At least one condition must be True

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")


# NOT
# Reverses True/False

is_raining = False

if not is_raining:
    print("You don't need an umbrella.")

# IF

age = 20

if age >= 18:
    print("You are an adult.")


# IF-ELSE

age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")


# IF-ELIF-ELSE

marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Need improvement.")

print("\n===== CALCULATOR =====")

# Get two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get operation
operator = input("Enter operation (+, -, *, /): ")

# Perform operation
if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":

    # Prevent division by zero
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid operator!")

# range(5) gives 0, 1, 2, 3, 4
for number in range(5):
    print(number)


# Starting from 1 and ending at 5
for number in range(1, 6):
    print(number)


# range(start, stop, step)
# Start = 0
# Stop before 10
# Increase by 2
for number in range(0, 10, 2):
    print(number)

# Repeat something 5 times
for i in range(5):
    print("Hello")


# Print numbers 1 to 5
for i in range(1, 6):
    print(i)


# Loop through a string
name = "Siraj"

for letter in name:
    print(letter)

number = 1

# Keep running while number is <= 5
while number <= 5:

    print(number)

    # Increase number
    # Without this, the loop could run forever
    number = number + 1

# break completely stops the loop

for number in range(1, 11):

    if number == 6:
        break

    print(number)

# continue skips the current iteration

for number in range(1, 6):

    if number == 3:
        continue

    print(number)

# A list stores multiple values
fruits = ["Apple", "Banana", "Mango"]

print(fruits)

# Access list items
print(fruits[0])
print(fruits[1])

# Change an item
fruits[1] = "Orange"

print(fruits)

# Add an item
fruits.append("Mango")

print(fruits)

# Remove an item
fruits.remove("Apple")

print(fruits)

# Loop through a list
for fruit in fruits:
    print(fruit)


# A tuple is similar to a list,
# but its values cannot be changed.

fruits = ("Apple", "Banana", "Mango")

print(fruits)

print(fruits[0])
print(fruits[1])

# This would cause an error:
# fruits[0] = "Orange"

# A set stores unique values

numbers = {1, 2, 3, 4, 5}

print(numbers)

# Duplicate values are automatically removed
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)

# Add a value
numbers.add(5)

print(numbers)

# Remove a value
numbers.remove(2)

print(numbers)

# Convert a list into a set to remove duplicates
numbers = [1, 2, 2, 3, 3, 4, 4]

unique_numbers = set(numbers)

print(unique_numbers)

# Dictionary stores data as key : value

student = {
    "name": "Siraj",
    "age": 21,
    "course": "MScIT"
}

print(student)

# Access values using keys
print(student["name"])
print(student["age"])
print(student["course"])

# Change a value
student["age"] = 22

print(student)

# Add a new key-value pair
student["college"] = "NKT College"

print(student)

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)

# A function is a reusable block of code

def say_hello():
    print("Hello!")


# Calling the function
say_hello()


# Function with a parameter

def greet(name):
    print("Hello", name)


greet("Siraj")
greet("Yash")
greet("Hinal")


# Function with return

def add(a, b):

    # Calculate the result
    result = a + b

    # Return the result to whoever called the function
    return result


answer = add(10, 20)

print("Answer:", answer)


# Another function example

def square(number):
    return number * number


result = square(5)

print("Square:", result)

import random

print("\n===== GUESS THE NUMBER =====")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("I have selected a number between 1 and 100.")
print("Try to guess it!")

# Keep asking until the user gets it right
while True:

    guess = int(input("Enter your guess: "))

    # Guess is too low
    if guess < secret_number:
        print("Too low! Try again.")

    # Guess is too high
    elif guess > secret_number:
        print("Too high! Try again.")

    # Guess is correct
    else:
        print("Correct! You guessed the number!")

        # Stop the loop
        break
