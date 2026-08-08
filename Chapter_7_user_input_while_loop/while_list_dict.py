# While loop with dictionary and lists

# confirmed_users.py

# start with users that need to be verified 
# add to empty list if confirmed

unconfirmed_users = ["alice", "brian", "candace"]

confirmed_users = []

# verify unconfirmed users untill there is no more confirmed users

while unconfirmed_users:
    # remove last user from unconfirmed users
    current_user = unconfirmed_users.pop()

    print(f" Verifying user: {current_user.title()}")

    confirmed_users.append(current_user)

print(f"Confirmed users are : {confirmed_users[-1: :-1]}")


# pets.py

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while 'cat' in pets:
    pets.remove("cat")

print(pets)

# mountain_poll.py

responses = {}

polling_active = True

while polling_active == True:
    name = input("What's your name: ")
    response = input("\nWhich mountain would you like to climb today: ")

    responses[name] = response

    # check again
    repeat = input("Would anyone else like to poll today(Yes/No): ")

    if repeat.lower() == "no":
        polling_active = False


for k,v in responses.items():
    print(f"{k.title()} would like to climb {v.title()} mountain today.")

# try It yourself
# 7-8. Deli:
# Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order
# such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ["cheese", "tomato", "cucmber", "corn and peas", "spinach & mushroom"]

finished_sandwiches = []

for s in sandwich_orders:
    print(f"I made your {s} sandwich.")
    finished_sandwiches.append(s)

print(f"\nSandwiches which has been made so far are :")

for f in finished_sandwiches:
    print(f)


# 7-9. No Pastrami:
# Using the list sandwich_orders from Exercise 7-8, 
# make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["pastrami","cheese", "tomato", "pastrami", "cucmber", "corn and peas", "pastrami","spinach & mushroom"]

print("The deli has run out of pastrami sandwiches")

sandwich_orders.remove("pastrami")

finished_sandwiches = []

for s in sandwich_orders:
    print(f"I made your {s} sandwich.")
    finished_sandwiches.append(s)

print(f"\nSandwiches which has been made so far are :")

for f in finished_sandwiches:
    print(f"{f.title()} sandwich")

# 7-10. Dream Vacation:
# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll.

vacation = {}

polling_active = True

while polling_active == True:

    name = input("What's your name: ")
    response = input(" Which place would you like to visit in the world: ")

    # add these to the dictionary
    vacation[name] = response

    # check if anyone left to poll

    repeat = input("Would anyone else like to tell(Yes/No): ")

    if repeat.lower() == "no":
        polling_active = False

for k,v in vacation.items():
    print(f"{k.title()} would like to visit {v.title()}.")

