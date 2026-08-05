# for loop in list
magicians = ["alice art", "david denver", "carolina chung"]

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick " + magician.title() + "\n")

# doing something after a for loop

print("\nThank You everyone, It was a great show.")


# Try It Yourself
# 4-1. Pizzas: Think of at least three kinds of your favorite pizza.
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.

pizzas = ["veg", "margerita", "farmhouse", "peperoni"]

for p in pizzas:
    print(p)


# •Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza.
# For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
for p in pizzas:
    print(f"I like {p} pizza.")


# •Add a line at the end of your program, outside the for loop, that states how much you like pizza.
# The output should consist of three or more lines about the kinds of pizza you like and 
# then an additional sentence, such as I really love pizza!

for p in pizzas:
    print(f"I like {p} pizza.\n")
print("I really love pizza! ")


# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and 
# then use a for loop to print out the name of each animal.

animals = ["dog", "cat", "parrot"]
for a in animals:
    print(a.title())


# •Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
for a in animals:
    print(f"A {a} would make a great pet.\n")

# •Add a line at the end of your program stating what these animals have in common.
# You could print a sentence such as Any of these animals would make a great pet!

for a in animals:
    print(f"A {a} would make a great pet.\n")

print("Any of these animals would make a great pet!")

# Numerical lists

# range (inclusive, not included)
for value in range(1,5):
    print(value)        # print 1 to 4 as 5 is not included

# using range() for making a list of numbers

numbers = list(range(1,6))
print(numbers)

# even numbers range(start, end not inclusive, step)
even_num = list(range(2,11,2))
print(even_num)

# Squares
squares = []

for r in range(1,11):
    #square = r * r
    squares.append(r * r)

print(squares)

# Simple Statistics with a list of numbers

digits = list(range(0,10))
print(min(digits))

print(max(digits))

print(sum(digits))

print(len(digits))

print(sum(digits)/len(digits))


# List Comprehension

squares = [ r**2 for r in range(1,11)]
print(squares)

# try It yourself
# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for r in range(1,21):
    print(r)

# 4-4. One Million: Make a list of the numbers from one to one million, and 
# then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl-C 
# or by closing the output window .)

million = list(range(1,10000001))
print(million)


# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and ends at one million.
# Also, use the sum() function to see how quickly Python can add a million numbers.

million = list(range(1,10000001))
print(min(million))
print(max(million))
print(sum(million))
print(len(million))

# 4-6. Odd Numbers:
# Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
# Use a for loop to print each number.

odd_num = list(range(1,20,2))
print(odd_num)
for r in range(1,20,2):
    print(r)


# # 4-7. Threes: Make a list of the multiples of 3 from 3 to 30 . Use a for loop to print the numbers in your list .
# for r in range(1,11):
#     print(r * 3)


# 4-8. Cubes: A number raised to the third power is called a cube . 
# For example, the cube of 2 is written as 2**3 in Python.
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10),
# and use a for loop to print out the value of each cube.

for r in range(1,11):
    print( r ** 3)


# # 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubes = [r ** 3 for r in range(1,11)]
print(cubes)