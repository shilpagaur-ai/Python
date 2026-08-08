# Simple Dictionaries
# aliens.py

alien_0 = {"color": "green", "point": 5}

print(alien_0["color"])
print(alien_0["point"])

# accessing value in a dictionary
new_points = alien_0["point"]
print(f"You just earned {new_points} points.")

# adding new key-value pair
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)

# modifying values in a dictionaries
alien_0 = {}
alien_0["color"] = "green"
print(f"The alien is {alien_0["color"]}.")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0["color"]}.")

# Modifying dicts: example 2

alien_0 = { "x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original x-position: {alien_0["x_position"]}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # It must be a fast alien
    x_increment = 3

# The new position of the alien is old Position + Increment
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"The new x-position: {alien_0["x_position"]}")

# Deleting Key-Value Pair
alien_0 = {"color": "green", "point": 5}
print(alien_0)


del alien_0["color"]
print(alien_0)

# Dictionary of similar objects
fav_language = {
    "akash" : "python",
    "sarah" : "C",
    "peter" : "java",
    "claire": "python"
}

# print Sarah's fav language
print(f"Sarah's favourite language is {fav_language["sarah"]}.")

# try It yourself
# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.

person = {"first_name" : "sachin", "last_name": "tendulkar", "age": 50, "city": "mumbai"}

for k,v in person.items():
    print(f"{k}: {v}")

# 6-2. Favorite Numbers:
# Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value in your dictionary.
# Print each person’s name and their favorite number.
# For even more fun, poll a few friends and get some actual data for your program.

fav_num = {"alice": 100 , "bob" : 234, "claire": 453, "david": 75}

for k,v in fav_num.items():
    print(f"{k.title()}: {v}")

# 6-3. Glossary:
# A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning,
# or print the word on one line and then print its meaning indented on a second line.
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {"if": "conditional statements", "variables": "to store values of various types", "string": "text data", "tuple": "a datatype to store any type of value and it is immutable", "list": "datatype which can store any kind of value and can be modified"}

for k,v in glossary.items():
    print(f"{k.title()}: {v.title()}")

for k,v in glossary.items():
    print(f"{k.title()}: \n{v.title()}")

