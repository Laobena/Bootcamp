# Printing Welcome to the user
print("Welcome to Holiday calculator\n")

city_list = ["Barcelona", "London", "Rome", "Amsterdam", "Istanbul"]
print("Here are cities we currently have available:")
# Print the available cities separated by commas
print(", ".join(city_list))

# Prompt the user to choose a city for flights
city_flights = input("Which city would you like to fly to?\n")
# Validate the chosen city, prompting until a valid city is chosen
while city_flights not in city_list:
    print("Invalid city. Please choose from the available options.")
    city_flights = input("Which city would you like to fly to?\n")

# Costs for flights and accommodations
flight_cost = [90, 130, 60, 70, 140]
per_night_cost = [40, 100, 40, 70, 90]
per_day_car_cost = [20, 40, 20, 25, 30]

# Prompt the user for the number of nights for accommodations
num_nights = int(input("How many nights would you like to stay?\n"))

# Prompt the user for the number of days to rent a car
rental_days = int(input("How many days would you want to rent a car?\n"))

# Calculate the cost of accommodations in the chosen city
def hotel_cost(city, nights):
    index = city_list.index(city)
    return nights * per_night_cost[index]

# Calculate the cost of flights to the chosen city
def plane_cost(city):
    index = city_list.index(city)
    return flight_cost[index]

# Calculate the cost of renting a car in the chosen city
def car_rental(city, days):
    index = city_list.index(city)
    return days * per_day_car_cost[index]

# Calculate the total cost of the holiday
def holiday_cost():
    total_hotel_cost = hotel_cost(city_flights, num_nights)
    total_plane_cost = plane_cost(city_flights)
    total_car_cost = car_rental(city_flights, rental_days)
    return total_hotel_cost + total_plane_cost + total_car_cost

# Calculate and display the breakdown of costs
total_cost = holiday_cost()
print("Hotel Cost:£", hotel_cost(city_flights, num_nights))
print("Flight Cost:£", plane_cost(city_flights))
print("Car Rental Cost:£", car_rental(city_flights, rental_days))
print("Total Cost:£", total_cost)