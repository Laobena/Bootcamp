print("Welcome to Holiday calculator\n")

city_list = ["Barcelona", "London", "Rome", "Amsterdam", "Istanbul"]
print("Here are cities we currently have available:")
print(", ".join(city_list))

city_flights = input("Which city would you like to fly to?\n")
while city_flights not in city_list:
    print("Invalid city. Please choose from the available options.")
    city_flights = input("Which city would you like to fly to?\n")

flight_cost = [90, 130, 60, 70, 140]
num_nights = int(input("How many nights would you like to stay?\n"))
per_night_cost = [40, 100, 40, 70, 90]

rental_days = int(input("How many days would you want to rent a car?\n"))
per_day_car_cost = [20, 40, 20, 25, 30]

def hotel_cost(city, nights):
    index = city_list.index(city)
    return nights * per_night_cost[index]

def plane_cost(city):
    index = city_list.index(city)
    return flight_cost[index]

def car_rental(city, days):
    index = city_list.index(city)
    return days * per_day_car_cost[index]

def holiday_cost():
    total_hotel_cost = hotel_cost(city_flights, num_nights)
    total_plane_cost = plane_cost(city_flights)
    total_car_cost = car_rental(city_flights, rental_days)
    return total_hotel_cost + total_plane_cost + total_car_cost

total_cost = holiday_cost()
print("Hotel Cost:£", hotel_cost(city_flights, num_nights))
print("Flight Cost:£", plane_cost(city_flights))
print("Car Rental Cost:£", car_rental(city_flights, rental_days))
print("Total Cost:£", total_cost)