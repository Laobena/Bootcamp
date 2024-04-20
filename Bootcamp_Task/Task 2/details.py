# Input commands to gather and store data that is given by the user
name = input("What is you name?\n")
age = input("How old are you?\n")
house_numb = input("What is your house number?\n")
street_name = input("What is your street name?\n")

# I used a fstring to gather and print all the data into a string
print(f"This is {name}. Your {age} years old and lives at {house_numb} {street_name}.")