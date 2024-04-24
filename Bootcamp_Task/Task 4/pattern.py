# Making the pattern list
pattern_list = ["*", "**", "***", "****", "*****"]
 # Reverses the list from index 3 to the beginning
reversed_list = pattern_list[3::-1] 

for item in pattern_list:
    print(item)  # Print each item in the original list
    if len(item) == 5:  # Check if the length of the item is 5
        for item in reversed_list:  # Iterate over the reversed list
            print(item)  # Print each item in the reversed list

