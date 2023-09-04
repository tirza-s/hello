# Ask user for their name 
name = input("What is your name ? ").strip().title()

#remove whitespace from str
#name = name.strip()

#capitalize user's name
#name = name.capitalize()

#name = name.strip().title()

#ask the user user first and last name then split
first, last = name.split(" ")

#Say hello to the user
print(f"Hello, {first}")


