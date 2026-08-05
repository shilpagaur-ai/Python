# Simple Dictionaries
# aliens.py

alien_0 = {"color": "green", "point": 5}

print(alien_0["color"])
print(alien_0["point"])

# accessing value in a dictionary
new_points = alien_0["point"]
print(f"You just earned {new_points} points.")

# adding new key-value pair
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)

# modifying values in a dictionaries
alien_0 = {}
alien_0["color"] = "green"
print(f"The alien is {alien_0["color"]}.")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0["color"]}.")