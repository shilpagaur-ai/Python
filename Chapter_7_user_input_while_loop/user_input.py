# # Asking for User Input
# message = input("Tell me something, I will repeat it back to you: ")
# print(message)

# # writing clear prompt

# name = input("Please enter your name: ")
# print(f"Hello {name.title()}, How are you doing?")

# += adds the prompts

prompt = "If you tell us who you are, we can personalise the messages you see!"
prompt += "\nEnter your name: "

message = input(prompt)
print(f"Hi {message.title()}, How are you ?")

# Accepting Numerical Inputs 

age = input("Enter your age: ")

print(f"In 2 years, you will be {int(age)+2}.")

# rollercoaster.py

height = int(input("Enter your height in inches: "))

if height >= 36:
    print(f"You are tall enough to ride. Enjoy!")
else:
    print(f"You will be able to ride when you are little older.")


# Modulo Operator (% - gives remainder when x/y)

print(4/3)

# even_odd.py

num = int(input("Enter a number and I will tell you if it is even or odd."))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# try It yourself
# 7-1. Rental Car:
# Write a program that asks the user what kind of rental car they would like.
# Print a message about that car, such as “Let me see if I can find you a Subaru.”
car = input("Which car would you like to rent: ")
print(f"Let me see if I can find you a {car}.")

# 7-2. Restaurant Seating:
# Write a program that asks the user how many people are in their dinner group.
# If the answer is more than eight,
# print a message saying they’ll have to wait for a table.Otherwise, report that their table is ready.
num = int(input("How many people are there in your dinning group?: "))

if num > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")


# 7-3. Multiples of Ten:
# Ask the user for a number, and then report whether the number is a multiple of 10 or not.

num = int(input("Enter a number and I will tell you whether it is a multiple of 10 or not. "))

if num % 10 == 0:
    print(f"{num} is a multiple of 10.")

else:
    print(f"{num} is not a multiple of 10.")
