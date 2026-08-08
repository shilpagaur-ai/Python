# # A list of dictionaries

# list_dict = [
#     {"first" : 1},
#     {"second" : 2},
#     {"third" : 3},
#     {"fourth" : 4},
#     {"fifth" : 5}
#      ]

# # Accessing indexwise element which will give key-value pair

# print(list_dict[0])

# # But if want only 1

# print(list_dict[0]["first"])


# # aliens.py

# alien_0 = {"colour" : "green", "point" : 5}
# alien_1 = {"colour" : "yellow", "point" : 10}
# alien_2 = {"colour" : "red", "point" : 15}

# aliens = [alien_0, alien_1, alien_2]

# for a in aliens:
#     print(a)


# # Make 30 green aliens programmatically

# green_aliens = []

# for r in range(30):
#     new_alien = {"colour" : "green", "speed": "slow", "point" : 5}
#     green_aliens.append(new_alien)

# print(len(green_aliens))

# print(green_aliens[: 5])



# # Change colour, point and add speed to aliens for first 3 aliens

# green_aliens = []

# for r in range(0, 30):
#     new_alien = {"colour" : "green","speed": "slow","point" : 5}
#     green_aliens.append(new_alien)

# for g in green_aliens[0:3]:

#     # we have g which is the first element and is a dict not a list item so we access using "key" not index
#     if g["colour"] == "green":
#         g["colour"] = "yellow"

#         # Key speed will be added 
#         g["speed"] = "medium"
#         g["point"] = 10

# for g in green_aliens[0:5]:
#     print(g)

# # A dictionary of lists

# pizza = {
#     "crust" : "thin",
#     "toppings" : ["mushrooms", "extra cheese", "green pepper", "pepperoni"],
#     "sauces" : ["tomato", "basic", "garlic"]
#     }

# # access each key in the pizza dictionary

# for p in pizza:
#     print(p)

# # access each key-value pair in the pizza dictionary

# for p in pizza.items():
#     print(p)

# # access mushrooms in the pizza dictionary

# print(pizza["toppings"][0])
# # all toppings
# print(f"All pizza toppings are: {pizza['toppings']}")


# # access garlic in the pizza dictionary

# print(pizza["sauces"][-1])

# # Summarise the order

# print(f"You have ordered a pizza with {pizza['crust']} crust and the toppings are as follows: ")

# for t in pizza["toppings"]:
#     print(f"\t{t}")

# print("Your sauces are as follows: ")

# for s in pizza["sauces"]:
#     print(f"\t{s}")


# # Example Fav_languages

# fav_languages = {
#     "jen" : ["c", "python"],
#     "edward" : ["c"],
#     "sarah" : ["ruby", "java"],
#     "phil" : ["c++", "python"]
# }

# for k, v in fav_languages.items():

#     if len(fav_languages[k]) >1:
#         print(f" {k.title()}'s favourite languages are: ")

#         for v in fav_languages[k]:
#             print(f"\t{v.title()}")
#     else:
#         print(f" {k.title()}'s favourite language is: ")
        
#         for v in fav_languages[k]:
#             print(f"\t{v.title()}")

# print(len(fav_languages["edward"]))


# # Dictionary of dictionary

# college = {
#     "dept_1" : {"name" : "IT", "strength" : 200},
#     "dept_2" : {"name" : "mechanical", "strength" : 50},
#     "dept_3" : {"name" : "chemical", "strength" : 120}
# }

# # accessing each key
# for c in college:
#     print(c)

# # accessing each key - value pair

# for k,v in college.items():
#     print(f"{k}: {v}")

# # accessing each value

# for v in college.values():
#     print(v)

# # accessing inner values of nested dictionaries in each dept

# print("----------------\n")
# for v in college.values():

#     # below code gives the output = dict_values(['IT', 200])
#     print(f"{v.values()}")

#     # below code will give just [IT, 200]
#     print(f"{list(v.values())}")

#     # below code will give just values separated by comma(,)
#     print(f"{v["name"]}, {v["strength"]}")

# # example 2 of dictionary of dictionaries
# users = {
#     "aeinstean" : {"first" : "albert", "last" : "einstein", "location" : "princeton"},
#     "mcurie" : {"first" : "marie", "last" : "currie", "location" : "paris"}
# }

# for k,v in users.items():
#     print(f"Username: {k}")
#     print(f"\tFull Name: {v['first'].title()} {v['last'].title()}")
#     print(f"\tLocation: {v['location'].title()}")

# # try It yourself
# # 6-7. People:
# # Start with the program you wrote for Exercise 6-1 (page 102).
# # Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
# # Loop through your list of people.
# # As you loop through the list, print everything you know about each person.

# people = [
#     {"first_name" : "sachin", "last_name": "tendulkar", "age": 55, "city": "mumbai"},
#     {"first_name" : "mahendra", "last_name": "dhoni", "age": 42, "city": "ranchi"},
#     {"first_name" : "virat", "last_name": "kohli", "age": 38, "city": "delhi"}
# ]

# for p in people:
#     print(f"{p['first_name'].title()} {p['last_name'].title()} is {p['age']} years old and lives in {p['city'].title()}.")

# # 6-8. Pets:
# # Make several dictionaries, where the name of each dictionary is the name of a pet.
# # In each dictionary, include the kind of animal and the owner’s name.
# # Store these dictionaries in a list called pets.
# # Next, loop through your list and as you do print everything you know about each pet.

# pets = [
#     {"name": "dog", "type" : "mammal", "owner": "sarah"},
#     {"name": "parrot", "type" : "Bird", "owner" : "john"},
#     {"name": "turtle", "type" : "amphibian", "owner" : "david"}
# ]

# for pet in pets:
#     print(f"{pet['name'].title()} is a {pet['type'].lower()} and its owner is {pet['owner'].title()}.")


# # 6-9. Favorite Places:
# # Make a dictionary called favorite_places.
# # Think of three names to use as keys in the dictionary, and store one to three favorite places for each person.
# # To make this exercise a bit more interesting, ask some friends to name a few of their favorite places.
# # Loop through the dictionary, and print each person’s name and their favorite places.

# fav_places = {
#     "alice" : ["paris", "london", "bali"],
#     "bob" : ["nyc", "kochi", "thailand"],
#     "claire" : ["jaipur", "chiang-mai", "zurich", "rome"]
# }

# # following will give trailing comma
# for k,v in fav_places.items():
#     print(f"{k.title()}'s favourite places are:", end = " ")
#     for p in range(len(v)):
#         print(f"{v[p].title()}", end = ",")
#     print("\n")

# # It won't have trailing commas & we used a new method . join()
# for k, v in fav_places.items():
#     place = ", ".join(p.title() for p in v)
#     print(f"{k.title()}'s favourite places are: {place}.")

# # 6-10. Favorite Numbers:
# # Modify your program from Exercise 6-2 (page 102)
# # so each person can have more than one favorite number.
# # Then print each person’s name along with their favorite numbers.

# fav_num = {
#     "alice": [100, 87, 34],
#     "bob" : [90, 56, 234],
#     "claire": [45, 67, 453],
#     "david": [99, 100, 75]
#     }

# for k, v in fav_num.items():
#     nums = ", ".join(str(n) for n in v)
#     print(f"{k.title()}'s favourite numbers are: {nums}.")

# # 6-11. Cities:
# # Make a dictionary called cities.
# # Use the names of three cities as keys in your dictionary.
# # Create a dictionary of information about each city 
# # and include the country that the city is in, its approximate population, and one fact about that city.
# # The keys for each city’s dictionary should be something like country, population, and fact.
# # Print the name of each city and all of the information you have stored about it.

# cities = {
#     "delhi" : {"country" : "India", "population": " 20 Million", "fact" : "Capital of largest democracy"},
#     "paris" : {"country" : "france", "population": " 2 million", "fact" : "Home of modern Democracy"},
#     "rome" : {"country" : "itly", "population": " 2 Million", "fact" : "Pizza inventor"}
# }

# for k, v in cities.items():
#     print(f"{k.title()} is in {v["country"].title()} and has{v["population"].title()} population & it is the {v["fact"].lower()}.")
