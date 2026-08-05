cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())

    else:
        print(car.title())


# Checking for inequalities

requested_toppings = "mushroom"

if requested_toppings != "anchovies":
    print("Hold the anchovies!")


# Numerical Comparison

answer = 17

if answer != 42:
    print("This is not the correct answer. Please try again!")


# Checking whether a value is in the list

requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings)
print("pepperoni" in requested_toppings)

# Checking whether a value is not in a list

banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Boolean Expressions
# try It yourself
# 5-1. Conditional Tests:
# Write a series of conditional tests.
# Print a statement describing each test and your prediction for the results of each test.
# Your code should look something like this:
#                   car = 'subaru'
#                   print("Is car == 'subaru'? I predict True.")
#                   print(car == 'subaru')
#                   print("\nIs car == 'audi'? I predict False.")
#                   print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line evaluates to True or False .
# • Create at least 10 tests . Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

# test 1
car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == "subaru")

# test 2
num = list(range(1,6))
print("Is 6 in num ?, I predict False")
print(6 in num)

# test 3
print("Is 2 in num?, I predict True")
print(2 in num)

# test 4
print("Is length of num = 5? I predict True")
print(len(num) == 5)

# test 5

cars_num = ["bmw", 5, "audi", 10 ]
print("Is 11 in cars_num? I predict False")
print( 11 in num)

# test 6

cars_num.append(11)
print(cars_num)

print("Is 11 in cars_num? I predict True Now")
print( 11 in cars_num)

# test 7

del cars_num[0]

print("Is bmw in cars_num? I predict False")
print("bmw" in cars_num)

# test 8
cars_num.insert(0, "bmw")
print("Is bmw in cars_num? I predict True")
print("bmw" in cars_num)

# test 9
cubes = [r**3 for r in range(1, 6)]
print("Is 4 in cubes? I predict False")
print(4 in cubes)

# test 10
print("Is cubes[1] + 1 == 3? I predict false")
print(cubes[1]+1 == 3)



# 5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10.
# If you want to try more comparisons, write more tests and add them to conditional_tests.py.
# Have at least one True and one False result for each of the following:
# • Tests for equality and inequality with strings
# test for equality
sum = 20
if sum == 10:
    print(True)
else:
    print(False)

# test for inequality

print(sum!= 19)

# • Tests using the lower() function
names = ["Adam", "Eve", "Bob"]
print(names[0].lower() == "adam")

# • Numerical tests involving equality and inequality
# Done Above

# greater than and less than, greater than or equal to, and less than or equal to
avg = 25
print(avg > 10)
print(avg < 20)
print(avg == 25)
# • Tests using the and keyword and the or keyword
print("Tests using and and or")
print(avg > 10 and avg < 100)
print(avg >=25 or avg <= 5 )
# • Test whether an item is in a list
new_list = ["apple", "banana", "carrot"]
print("Is banana in the list? I predict True")
print("banana" in new_list)
# • Test whether an item is not in a list
print("Is kiwi in the list? I predict False")
print("kiwi" in new_list)