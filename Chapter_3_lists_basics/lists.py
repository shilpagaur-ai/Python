# # Lists are mutable (we can add or delete from a list) collection of items & can have strings, numbers, lists or anything else

# bicycles = ["trek", "cannondale", "redline", "specialised"]

# print(bicycles)             # will print list with square bracket

# print(type(bicycles))       # will output <class 'list>

# # Accessing a list - index is used, Python uses zero indexing ie- first position is index 0

# # get first item from the bicycles list

# print(bicycles[0])

# # get last item from the bicycle list using negative index

# print(bicycles[-1])

# # using string method for string item in the list

# # Uppercase the last item
# print(bicycles[-1].upper())

# # using individual values from the list

# general = ["bicycle", 20, "car"]

# # Accessing the item, doing operation on it and converting to str to get the str message

# message = "There are " + str(general[1]/20 + 2) + " items in the list."

# print(message)

# print(general[1] + 1)

# print(general[-1] + " is the last element in the list.")



# # Try It Yourself

# # 3-1. Names: Store the names of a few of your friends in a list called names.
# # Print each person’s name by accessing each element in the list, one at a time.

# names = ["Alice", "Bob", "Claire", "Diane"]

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[-1])

# # 3-2. Greetings: Start with the list you used in Exercise 3-1
# # but instead of just printing each person’s name, print a message to them.
# # The text of each message should be the same, but each message should be personalized with the person’s name.

# message = "Hi, How are you doing, "
# print(message + names[0] + "?")
# print(message + names[1] + "?")
# print(message + names[2] + "?")
# print(message + names[3] + "?")


# # 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and 
# # make a list that stores several examples . Use your list to print a series of statements about these items, 
# # such as “I would like to own a Honda motorcycle.”

# cars = ["ferrari", "mustang", "porche", "lincon"]

# print("I saw a TV series named after my favourite " + cars[-1] + " car.")

# print("I would love to own a " + cars[1] + " one day.")
