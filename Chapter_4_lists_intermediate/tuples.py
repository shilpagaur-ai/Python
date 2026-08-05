# tuples are like lists as in you can have any values in it, can access any element using index but
# tuples are immutable ie You can not add, delete, modify any item in a tuple
# tuple are defined using parenthese() instead of square brackets like []

# rectangle dimension

rectangle = (200, 50)
print(rectangle[0])
print(rectangle[1])

# Let's try changing the tuple element
# It will throw TypeError: 'tuple' object does not support item assignment

# rectangle[0] = 250

# Looping through all values in a tuple

rectangle = (200, 50)
for r in rectangle:
    print(r)


# writing over a tuple

rectangle = (200,50)
print("Original Dimensions: ")
for r in rectangle:
    print(r)

rectangle = (250, 100)
print("Modified Dimensions: ")
for r in rectangle:
    print(r)

# Above won't give error we over wrote or say assigned new tuple to variable rectangle



# try It yourself
# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.

menu = ("bread", "salad", "juice", "egg", "vegetables")

print(" Buffet menu is : ")
for m in menu:
    print(m)

# • Try to modify one of the items, and make sure that Python rejects the change.
# menu[0] = "butter"

# • The restaurant changes its menu, replacing two of the items with different foods.
# Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

menu = ("butter", "jam", "juice", "egg", "vegetables")
print("Updated menu is :")
for m in menu:
    print(m)