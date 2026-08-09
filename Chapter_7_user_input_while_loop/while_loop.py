# counter.py

counter = 1
while counter <= 5:
    print(counter)
    counter += 1

# parrot.py

prompt = "Tell me something, I will repeat it back to you.\n"
prompt += "Enter 'quit' to end the program. "

message = ""

while message.lower() != "quit":
    message = input(prompt)
    print(message)


# parrot2.py

prompt = "Tell me something, I will repeat it back to you."
prompt += "Enter 'quit' to end the program.\n"

active = True
message = ""

while active == True:
    message = input(prompt)

    if message.lower() == "quit":
        active = False
    else:
        print(message)

# Using break to exit a loop
# cities.py
prompt = "Enter name of a city you have visited"
prompt += "Enter 'quit' to end the program."

while True:
    message = input(prompt)
    if message.lower() == "quit":
        break
    else:
        print(f"I would love to visit {message}.")

# using continue to return to the begining of the loop

current = 0
while current < 10:
    current += 1
    if current % 2 == 0:
        continue # skip even numbers

    print(current)


# try It yourself
# 7-4. Pizza Toppings:
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

while True:
    message = input("Which pizza topping you would like to add: ")

    if message.lower() == "quit":
        break

    else:
        print(f"I will add {message} to your pizza.")

# 7-5. Movie Tickets:
# A movie theater charges different ticket prices depending on a person’s age.
# If a person is under the age of 3, the ticket is free;
# if they are between 3 and 12, the ticket is $10; and 
# if they are over age 12, the ticket is $15.
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

age = int(input("What's your age: "))

if age < 3:
    print("Your ticket is free.")
elif age < 12:
    print("Your ticket costs $10.")
else:
    print("Your ticket costs $15.")

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.

# Here the goal is to actually see the age in the loop which I did not do earlier

age = ""

while age.lower() != "quit":

    age = input("What's your age: ")

    if age.lower() != "quit":
        if int(age) < 3:
            print("Your ticket is free.")
        elif int(age) < 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")

# • Use an active variable to control how long the loop runs.

active = True

while active == True:

    age = input("What's your age: ")

    if age.lower() == "quit":
        active = False
    elif int(age) < 3:
        print("Your ticket is free.")
        
    elif int(age) < 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")


# • Use a break statement to exit the loop when the user enters a 'quit' value.

active = True

while True:

    age = input("What's your age: ")

    if age.lower() == "quit":
        break

    elif int(age) < 3:
        print("Your ticket is free.")
        
    elif int(age) < 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")




# 7-7. Infinity: Write a loop that never ends, and run it . 
# (To end the loop, press ctrl-C or close the window displaying the output .)

age = int(input("What's your age: "))

# while True:
    # if age < 3:
    #     print("Your ticket is free.")
    # elif age < 12:
    #     print("Your ticket costs $10.")
    # else:
    #     print("Your ticket costs $15.")