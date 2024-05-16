# Initialize empty variables
total = 0.0  # Use floating-point numbers for total
count = 0

# Prompt the user for input and calculate average
while True:
    user_input = input("Please enter a number (enter '-1' to stop):\n")
    # Check if the user wants to stop immediately
    if user_input == "-1":
        if count == 0:
            print("No numbers entered. Exiting.")  # Inform the user if no numbers were entered
        else:
            average = total / count
            print(f"The average of the entered numbers (excluding '-1'): {average}")  # Print the average of the entered numbers
        break

    # Convert input to float and handle exceptions
    try:
        user_number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")  # Inform the user of invalid input
        continue
    
    # Check if the input is -1 immediately
    if user_number == -1:
        print("You entered -1 immediately. Exiting.")  # Inform the user of immediate exit
        break

    # Update total and count
    total += user_number
    count += 1

# Calculate and display the average if count is not zero
if count != 0:
    average = total / count
    print(f"Average of the entered numbers: {average}")  # Print the average after all numbers are entered

