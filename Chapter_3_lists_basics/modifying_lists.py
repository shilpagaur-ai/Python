# Changing, dding & Removing Elements

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# Change first element

motorcycles[0] = "ducati"
print(motorcycles)

# Adding elements to the list

motorcycles.append("honda")
print(motorcycles)

# Append for building a list dynamically
new_motorcycles = []

new_motorcycles.append("honda")
new_motorcycles.append("yamaha")
new_motorcycles.append("suzuki")
new_motorcycles.append("ducati")

print(new_motorcycles)


# Inserting elements into a list
# use .insert(index at which you want to insert the element and name of the element)

new_motorcycles.insert(2, "hayabusa")
print(new_motorcycles)

# Removing element from a list

# Removing using del statement

new_motorcycles = ["honda", "yamaha", "hayabusa", "suzuki", "ducati"]

del new_motorcycles[1]
print(new_motorcycles)

# Removing using pop statement
# pop() method lets us remove last element of the list and it retrurns the last element so that we can manipulate it

new_motorcycles = ["honda", "yamaha", "hayabusa", "suzuki", "ducati"]

# Let's print what we get when we pop

print(new_motorcycles.pop())        # will give last element

print(new_motorcycles)          # new_motorcycles has been modified so it wont show ducati in this

# Alternatively we can store the value of popped element & use it also

numbers = [50, 78, 200, 18]
print(len(numbers))         # 4 as total elements are 4 and len() gives no of elements

removed = numbers.pop()
print(len(numbers))         # 3 as we removed/popped last element

print(removed + 2)          # 20 as we are manipulating the popped elemenet -18

# Popping items from any index in a list

new_motorcycles = ["honda", "yamaha", "hayabusa", "suzuki", "ducati"]
print(new_motorcycles)

first_owned = new_motorcycles.pop(0)
print("The first bike I owned was " + first_owned + ".")
print(new_motorcycles)

# Removing an item by value

new_motorcycles = ["honda", "yamaha", "hayabusa", "suzuki", "ducati"]
print(new_motorcycles)

new_motorcycles.remove("hayabusa")
print(new_motorcycles)

# using variables
new_motorcycles = ["honda", "yamaha", "hayabusa", "suzuki", "ducati"]
print(new_motorcycles)

too_expensive = new_motorcycles[2]

new_motorcycles.remove(too_expensive)

print(new_motorcycles)

print("A " + too_expensive.title() + " is too expensive for me.")


# Try It Yourself

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

guests = ["Alice", "Bob", "Claire", "Diane"]

print("Hi " + guests[0] + ", I would like to invite you for dinner.")
print("Hi " + guests[1] + ", I would like to invite you for dinner.")
print("Hi " + guests[2] + ", I would like to invite you for dinner.")
print("Hi " + guests[-1] + ", I would like to invite you for dinner.")


# 3-5. Changing Guest List: 
# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.

# Start with your program from Exercise 3-4. 
# Add a print statement at the end of your program stating the name of the guest who can’t make it .
name_no_rsvp = "Claire"
print(name_no_rsvp + " can't make it to the dinner.")

# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
guests.remove(name_no_rsvp)

guests.append("Eden")
print("People who can make it to dinner are - ")
print(guests)

# Print a second set of invitation messages, one for each person who is still in your list.

print("Hi " + guests[0] + ", I would like to invite you for dinner.")
print("Hi " + guests[1] + ", I would like to invite you for dinner.")
print("Hi " + guests[2] + ", I would like to invite you for dinner.")
print("Hi " + guests[-1] + ", I would like to invite you for dinner.")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.

# • Start with your program from Exercise 3-4 or Exercise 3-5 . 
# Add a print statement to the end of your program informing people that you found a bigger dinner table.

guests = ["Alice", "Bob", "Claire"]
print(guests)
print("We found a bigger table, so we are inviting 3 more people.")

# • Use insert() to add one new guest to the beginning of your list.
guests.insert(0, "Diane")
print(guests)

# • Use insert() to add one new guest to the middle of your list.
guests.insert(int(len(guests)/2), "Eden")
print(guests)

# • Use append() to add one new guest to the end of your list.
guests.append("Fiona")
print(guests)

# • Print a new set of invitation messages, one for each person in your list.

for g in guests:
    print(f"Hi {g}, I would like to invite you to dinner")


# 3-7. Shrinking Guest List:
# You just found out that your new dinner table won’t arrive in time for the dinner,
# and you have space for only two guests.

# • Start with your program from Exercise 3-6.
# Add a new line that prints a message saying that you can invite only two people for dinner.

guests = guests = ["Diane", "Alice", "Eden", "Bob", "Claire", "Fiona", "Test"]
print("I can only invite 2 people.")

# • Use pop() to remove guests from your list one at a time until only two names remain in your list.
# Each time you pop a name from your list, 
# print a message to that person letting them know you’re sorry you can’t invite them to dinner.

# for g in guests:
#     print("Sorry " + guests.pop() + ", I can't invite you to dinner.")
#     guests_left = len(guests)
#     print(str(guests_left) + " guests still left.")

#     if guests_left == 1:
#         print(str(guests_left) + " guests left, so stopping.")
#         break

for g in range((len(guests)) - 2):
        print("Sorry " + guests.pop() + ", I can't invite you to dinner.")

        print(str(len(guests)) + " guests still left.")

print("Remaining Guests")
print(guests)

# • Print a message to each of the two people still on your list, letting them know they’re still invited.

for g in guests:
        print(f"Hi {g}, I would like to invite you to dinner.")

# • Use del to remove the last two names from your list, so you have an empty list.
# Print your list to make sure you actually have an empty list at the end of your program.

del guests[1]
print(guests)

del guests[0]
print(guests)