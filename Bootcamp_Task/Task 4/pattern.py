# Making the pattern list
pattern_list = ["*", "**", "***", "****", "*****"]
 # Reverses the list from index 3 to the beginning
reversed_list = pattern_list[3::-1] 

for item in pattern_list:
    print(item)  # Print each item in the original list
    if len(item) == 5:  # Check if the length of the item is 5
        for item in reversed_list:  # Iterate over the reversed list
            print(item)  # Print each item in the reversed list


# Diffrent way
# Iterate from 1 to 10
for num_asterisks in range(1, 11):
    # Print increasing number of asterisks for first 5 iterations
    if num_asterisks <= 5:
        print("*" * num_asterisks)
    # Print decreasing number of asterisks for remaining iterations
    else:
        # Determine the difference in positions from 10
        num_spaces = 10 - num_asterisks
        # Print asterisks multiplied by the difference
        print("*" * num_spaces)