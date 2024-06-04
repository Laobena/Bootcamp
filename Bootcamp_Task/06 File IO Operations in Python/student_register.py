print("Welcome to the teachers student registry")

# Initialize an empty list to store student IDs
student_ids = []
# Prompt the user to input the number of students to register and convert the input to an integer
no_of_students = int(input("How many students are you registering?\n"))  # Convert input to an integer

# Initialize a counter for the number of students registered
students_registered = 0 
# Begin a loop to register students until the desired number is reached
while students_registered < no_of_students:
    # Prompt the user to input a student ID
    student_id = input("Please enter student ID:\n")
    
    # Check if the length of the inputted student ID is 6 characters
    if len(student_id) == 6:  
        # If the length is valid, append the student ID to the list
        student_ids.append(student_id)
        
        # Increment the counter for the number of students registered
        students_registered += 1  
    else:
        # If the length is not valid, print an error message
        print("Sorry, invalid student ID. Please enter a 6-character ID.")

# Open a file named "reg_form.txt" in write mode to store the registered student IDs
with open("reg_form.txt", "w") as f:
    
    # Iterate through the list of student IDs
    for student_id in student_ids:
        # Write each student ID to the file followed by a placeholder for additional information
        f.write(student_id + "..................\n")