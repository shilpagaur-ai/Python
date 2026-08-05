# working with part of a list ie slice of a list

players = ["charles", "martina", "michael", "florence", "eli"]

# It will give elements at index 1, 2 but not 3 as 3 is not included
print(players[1:3])

# from start (inclusive) to one index before end (end exclusive)

print(players[0:4])

# from start if start index is not mentioned

print(players[:2])

# till end if the end index is not given
print(players[2:])

# all if start & end index is not given
print(players[:])

# Slicing through negative indexing
print(players[-1:]) # start from last and it will end as it is the last index

print(players[-2:]) # output last 2 elements

# reversing the list
# start index from last element using -1 then end index no (so entire list), step is -1( go in reverse direction)
print(players[-1: : -1])

# looping through a slice

players = ["charles", "martina", "michael", "florence", "eli"]

print("The first 3 players in my team are: ")
for p in players[:3]:
    print(p.title())

# copying a list

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print(f"My favourite foods are: {my_foods}")
print(f"\nMy friend's favourite foods are: {friend_foods}")

my_foods.append("cannoli")
friend_foods.append("ice-cream")
print(my_foods)
print(friend_foods)


# try It yourself
# 4-10. Slices: Using one of the programs you wrote in this chapter,
# add several lines to the end of the program that do the following:
# • Print the message, The first three items in the list are:. 
# Then use a slice to print the first three items from that program’s list

players = ["charles", "martina", "michael", "florence", "eli"]
print(players)
print(f"\nThe first three items in the list are: {players[:3]}")


# • Print the message, Three items from the middle of the list are: 
# Use a slice to print three items from the middle of the list .

print(f"\nThree items from the middle of the list are: {players[1:-1]}")

# • Print the message, The last three items in the list are: . Use a slice to print the last three items in the list .

print(f"\nThe last three items in the lists are {players[-3:]}")

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60).
# Make a copy of the list of pizzas, and call it friend_pizzas . Then, do the following:
# • Add a new pizza to the original list .
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. 
# Print the message, My favorite pizzas are:, and then use a for loop to print the first list.

my_pizzas = ["veg", "margerita", "farmhouse", "peperoni"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("mushroom")
friend_pizzas.append("paneer-tikka")
print(my_pizzas)
print(friend_pizzas)

print(f"My pizzas are: {my_pizzas}")

# Print the message, My friend’s favorite pizzas are:, 
# and then use a for loop to print the sec- ond list. 
# Make sure each new pizza is stored in the appropriate list.

print(f"My friend's pizzas are: {friend_pizzas}")

# 4-12. More Loops:
# All versions of foods.py in this section have avoided using for loops when printing to save space . 
# Choose a version of foods.py, and write two for loops to print each list of foods.

print(f"My friend's pizzas written through for loop are: ")
for f in friend_pizzas:
    print(f)