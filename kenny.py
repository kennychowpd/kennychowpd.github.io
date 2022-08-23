# Ask the user to input their name
name = input("What is your name? ")

# Remove whitespace from input &Capitalize user's name
cap_name = name.strip().title()
print(name.split())
first_name, last_name = name.split()

# print welcome message
print("Hello,", cap_name + ".", "Why is your name \"" + cap_name + "\"?")
print(f"Hello, {name}. Why is your name \"{name}\"?")