# Open the file "DOB.txt" in read mode
with open("DOB.txt", "r") as file:
    # Initialize empty lists to store names and birthdays
    names = []
    birthdays = []
    # Iterate through each line in the file
    for line in file:
        # Split the line into parts based on whitespace
        parts = line.split()
        # Extract the name by joining the parts except the last three (assumed to be the birth date)
        name = " ".join(parts[:-3])  
        # Extract the birth date by joining the last three parts
        birthday = " ".join(parts[-3:])  
        # Append the name and birthday to their respective lists
        names.append(name)
        birthdays.append(birthday)


print("Names:")
for name in names:
    print(name)


print("\nBirthdays:")
for birthday in birthdays:
    print(birthday)


        
