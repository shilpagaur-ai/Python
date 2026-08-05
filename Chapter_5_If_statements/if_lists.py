# if statements with lists

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for topping in requested_toppings:
    print(f"Adding {topping}.")

print("\nFinished Making Your Pizza.")

# If we run out of Green Peppers
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for topping in requested_toppings:
    if topping == "green peppers":
        print(f"Sorry, we are out of {topping} right now.")
    else:
        print(f"Adding {topping}.")

print("\nFinished Making Your Pizza.")

# checking if the list is not empty

requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
    print("\nFinshing making your pizza.")

else:
    print("Are you sure you want a plain pizza?")

# Using multiple lists

available_toppings = ["mushrooms", "olives", "green pepper", "pepperoni", "pineapple", "extra cheese"]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza.")

# try It yourself
# 5-8. Hello Admin:
# Make a list of five or more usernames, including the name 'admin'.
# Imagine you are writing code that will print a greeting to each user after they log in to a website.
# Loop through the list, and print a greeting to each user:
# • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

user_names = ["alice", "eric", "admin", "sophia"]

for u in user_names:
    if u == "admin":
        print(f"Hello admin, would you like to see a status report? ")
    else:
        print(f"Hello {u.title()}, thank you for logging in again.")



# 5-9. No Users:
# Add an if test to hello_admin.py to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed.

user_names = []

if user_names:
    for u in user_names:
        if u == "admin":
            print(f"Hello admin, would you like to see a status report? ")
        else:
            print(f"Hello {u.title()}, thank you for logging in again.")

else:
    print("We need to find some users!")

# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username .
# • Make a list of five or more usernames called current_users .
# • Make another list of five usernames called new_users. 
# Make sure one or two of the new usernames are also in the current_users list .
# • Loop through the new_users list to see if each new username has already been used.
# If it has, print a message that the person will need to enter a new username . 
# If a username has not been used, print a message saying that the username is available .
# • Make sure your comparison is case insensitive . If 'John' has been used, 'JOHN' should not be accepted .

current_users = ["alice", "bob", "kate", "carol", "sabrina", "nate", "eli"]

new_users = ["ella", "david", "Bob", "eli", "fisher", "peteR", "sabriNA"]

for n in new_users:
    if n.lower() in current_users:
        print(f"Username {n} is taken. Please choose another username.")
    else:
        print(f"Username {n} is available.")


# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd.
# Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a list.
# • Loop through the list .
# • Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
# Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

ordinal_num = list(range(1,10))

for n in ordinal_num:
    if n == 1:
        print(f"{n}st")
    elif n == 2:
        print(f"{n}nd")
    elif n == 3:
        print(f"{n}rd")
    else:
        print(f"{n}th")