pattern_list = ["*", "**", "***", "****", "*****"]
reversed_list = pattern_list[3::-1]

for item in pattern_list:
    print(item)
    if len(item) == 5:
        for item in reversed_list:
            print(item)
            

