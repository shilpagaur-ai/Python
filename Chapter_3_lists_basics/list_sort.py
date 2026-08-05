# # Sorting a list

# # Sorting permanently with sort() method

# cars = ["bmw", "audi", "toyota", "subaru"]

# cars.sort()
# print(cars)

# # Sorting in reverse order
# cars.sort(reverse = True)
# print(cars)

# # Sorting temporarily with the sorted() function
# # sorted just displays in sorted anner but does not mutate the original list

# unsorted_cars = ["bmw", "audi", "toyota", "subaru", "lincon"]
# print(sorted(unsorted_cars))
# print(unsorted_cars)

# # Printing a list in reverse order

# unsorted_cars.reverse()
# print(unsorted_cars)


# Try It Yourself

# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit .
# • Store the locations in a list . Make sure the list is not in alphabetical order .
# • Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
places = ["New York city", "Kenya", "Chille", "Iceland"]
print("Original Order")
print(places)

# • Use sorted() to print your list in alphabetical order without modifying the actual list.
# • Show that your list is still in its original order by printing it.
print("Using sorted() for displaying the list in sorted order")
print(sorted(places))

# • Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
print("Using Sorted to display reverse order")
print(sorted(places, reverse = True))

print("Orginal List still intact shown below -")
print(places)

# • Use reverse() to change the order of your list . Print the list to show that its order has changed.
places.reverse()
print("List has reversed as we used reverse() method")
print(places)

# • Use reverse() to change the order of your list again . Print the list to show it’s back to its original order.
places.reverse()
print("reversed again so back to original")
print(places)

# • Use sort() to change your list so it’s stored in alphabetical order . Print the list to show that its order has been changed.
places.sort()
print("List is permanently sorted using sort()")
print(places)

# • Use sort() to change your list so it’s stored in reverse alphabetical order . Print the list to show that its order has changed.
places.sort(reverse = True)
print("Reverse Sorted List")
print(places)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46)
# use len() to print a message indicating the number of people you are inviting to dinner.
# Done earlier in that exercise only

# 3-10. Every Function: Think of something you could store in a list.
# For example, you could make a list of mountains, rivers, countries, cities, languages, or any- thing else you’d like.
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once .
new = ["nile", "Alps", "New York City", "English"]

# Accessing an element

print(new[0])       # nile
print(new[-2])      # New York city

# Adding Kilimanjaro at end, French at start
new.append("Kilimajaro")
new.insert(0, "French")

print(new)

# Removing Kilimanjaro from end, removing Alps, removing French from start

new.pop()
new.remove("Alps")
del new[0]
print(new)

# Sorted()

print(sorted(new))
print("Still original List unsorted")
print(new)

# sort()
new.sort()
print("Orginal list mutated and sorted")
print(new)


# Sort reverse
print("Reverse sort()")
new.sort(reverse = True)
print(new)

# index Error
# print(new[3]) # IndexError: List index out of range
