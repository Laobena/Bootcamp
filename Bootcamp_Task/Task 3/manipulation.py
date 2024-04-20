str_manip = input("Enter a sentance: ")


print(f"The length of your string is {len(str_manip)}")

last_string = str_manip[-1]
new_string = str_manip.replace(last_string, "@")
print(f"Replacing every occurrence with '@' the result is \n{new_string}")


last_three = (str_manip[-1:-4:-1])
print(f"The last three character backwards is {last_three}")

three_letter = str_manip[:3:]
two_letter = str_manip[-2::]
new_word = three_letter + two_letter
print(f"Combining first three letter and last two letters. The result is {new_word}")