# # Stripping Whitespaces

# fav_language = " python "

# print(fav_language.rstrip())
# print(fav_language.lstrip())
# print(fav_language.strip())

# # Avaoid Syntax Error
# # This will give error
# message = 'This will give error as it's not right and will confuse python'

# message = "This will not give error as it's not wrong use of apostrophe and won't confuse python"
# print(message)


# # Try it Yourself

# # 2-3. Personal Message: Store a person’s name in a variable, and print a message to that person. 
# # Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

# name = "Eric"

# print("Hello " + name + " , would you like to learn some Python today?")

# 2-4. Name Cases: Store a person’s name in a variable
# and then print that per- son’s name in lowercase, uppercase, and titlecase.

# person = "Eric bright"

# # lowercase
# print(person.lower())

# # uppercase
# print(person.upper())

# # titlecase
# print(person.title())

# # 2-5. Famous Quote: Find a quote from a famous person you admire.
# # Print the quote and the name of its author.
# # Your output should look something like the following, including the quotation marks:
# # Albert Einstein once said, “A person who never made a mistake never tried anything new.”

# quote = ' "A person who never made a mistake never tried anything new.”'
# author = "Albert Einstein"

# print(author + " once said," + quote)

# # 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person.
# # Then compose your message and store it in a new variable called message. 
# # Print your message.

# quote = ' "A person who never made a mistake never tried anything new.”'
# famous_person = "Albert Einstein"

# message = famous_person + " once said," + quote
# print(message)

# 2-7. Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once .
# Print the name once, so the whitespace around the name is displayed . 
# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

# name = "   Eric   "

# print(name)
# print("\t" + name)
# print("\n\t" + name)

# # lstrip()
# print(name.lstrip())

# print(name.rstrip())

# print(name.strip())