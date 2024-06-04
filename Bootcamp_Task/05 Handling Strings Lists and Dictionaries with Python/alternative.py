# Define the input string
new_string = "Lets go out in an adventure!"

# Function to alternate the case of characters in a string
def alternate_char(string):
    result = ""
    # Iterate over each character in the string along with its index
    for place, char in enumerate(string):
        # If the index of the character is even, convert to uppercase
        if place % 2 == 0:
            result += char.upper()
        # If the index of the character is odd, convert to lowercase
        else:
            result += char.lower()
    return result

# Apply alternate_char function to the input string
alt_char_string = alternate_char(new_string)

# Print the result
print(alt_char_string)


# Function to alternate the case of words in a string
def alternate_word(string):
    # Split the string into a list of words
    word_list = string.split(" ")
    separator = " "
    # Iterate over each word in the list along with its index
    for place, word in enumerate(word_list):
        # If the index of the word is even, convert to lowercase
        if place % 2 == 0:
            word_list[place] = word.lower()
        # If the index of the word is odd, convert to uppercase
        else:
            word_list[place] = word.upper()
    # Join the modified words back into a string
    join_list = separator.join(word_list)
    return join_list

# Apply alternate_word function to the input string
alt_word_string = alternate_word(new_string)

# Print the result
print(alt_word_string)