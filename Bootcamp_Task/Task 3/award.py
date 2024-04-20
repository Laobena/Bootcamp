swimming = float(input("Please enter your swimming time results in minutes:\n"))
cycling = float(input("Please enter your cycling time results in minutes\n"))
running = float(input("please eneter your running time results in minutes\n"))

print("\n")

total_time = swimming + cycling + running
print(f"Your total time is {total_time:.2f} minutes.")

print("\n")

if total_time <= 100:
    print("You have recived: Provincial colours! ")
elif total_time >= 101:
    print("You have recived: Provincial half colours!")
elif total_time >= 106:
    print("You have recived: Provincial scroll")
else:
    print("Sorry no reward. Thank You for participating.")