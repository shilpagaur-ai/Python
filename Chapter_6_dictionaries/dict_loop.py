# Looping through dictionaries

user_0 = {
    "user_name" : "efermi",
    "first_name" : "enrico",
    "last_name" : "fermi"
}

for k,v in user_0.items():
    print(f"Key   : {k.title()}")
    print(f"Value : {v.title()}\n")

fav_language = {
    "jen" : "python",
    "enrico" : "C",
    "sarah" : "java",
    "phil" : "python"
}

for k,v in fav_language.items():
    print(f"{k.title()}'s favourite language is {v.title()}. ")

for k in fav_language:
    print(k.title())

friends = ["phil", "sarah"]

for k,v in fav_language.items():
    if k in friends:
        print(f"{k.title()}")
    else:
        print(f"Hi {k}, I see your favourite language is {v}")

if "erin" not in fav_language.keys():
    print("Erin, Please take our poll!")

for k in sorted(fav_language):
    print(k.title())

# Accessing only values
print(f"Following languages are being mentioned: ")
for v in fav_language.values():
    print(f"\t{v.title()}")

# for only unique value wrap in set()

for v in set(fav_language.values()):
    print(v.title())

# try It yourself
# 6-4. Glossary 2:
# Now that you know how to loop through a dictionary,
# clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements 
# with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    "if": "conditional statements", 
    "variables": "to store values of various types", 
    "string": "text data", "tuple": "a datatype to store any type of value and it is immutable", 
    "list": "datatype which can store any kind of value and can be modified"
    }

for k in glossary:
    print(k.title())

for v in glossary.values():
    print(v)

for k,v in glossary.items():
    print(f"{k.title()}: {v}")

glossary["dict"] = "datatype with key-value pair"

for k,v in glossary.items():
    print(f"{k.title()}: {v}")

# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through.
# One key-value pair might be 'nile': 'egypt'.
# •Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# •Use a loop to print the name of each river included in the dictionary.
# •Use a loop to print the name of each country included in the dictionary.

rivers = {
    "ganges" : "India",
    "nile" : "egypt",
    "thames" : "england"
}

for k,v in rivers.items():
    print(f"The {k.title()} runs through {v.title()}.")

# 6-6. Polling: Use the code in favorite_languages.py (page 104).
# •Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that are not.
# •Loop through the list of people who should take the poll.
# If they have already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take the poll.

fav_language = {
    "jen" : "python",
    "enrico" : "C",
    "sarah" : "java",
    "phil" : "python"
}

# Important learning: I wrote people as set using {} as I am writing dicts 
# It gave me an arbitarary order as sets are implemented as hash tables and order followed is as per hash values
# so order will be arbitrary but lookup will be pretty fast

people = ["jen", "josh", "jenna", "sarah"]

for p in people:
    if p in fav_language:
        print(f"Hi {p.title()}, Thank you for responding!")
    else:
        print(f"{p.title()}, Please take our poll!")
