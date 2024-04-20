user_input = int(input("Please enter a number\n"))
total = 0
count = 0

while user_input != -1:
    print("Please try again")
    user_input = int(input("Please enter a number\n"))
    
    total += int(user_input)
    count += 1

    if count == 0:
        print("No numbers entered")
    else:
        average = total / count
        print(f"Average:{average}")