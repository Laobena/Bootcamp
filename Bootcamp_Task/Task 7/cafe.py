# Define the menu items and their corresponding prices
menu = ["americano", "latte", "cappuccino", "hot chocolate"]

# Define the stock quantity for each menu item
stock = {"americano": 107, "latte": 102, "cappuccino": 103, "hot chocolate": 101}

# Define the price for each menu item
price = {"americano": 3.70, "latte": 4.35, "cappuccino": 4.50, "hot chocolate": 4.10}

# Initialize an empty dictionary to store the total stock value for each item
total_stock = {}

# Iterate through each menu item
for item in stock:
    # Check if the item exists in the price dictionary
    if item in price:
        # Calculate the total stock value by multiplying the stock quantity with the price,
        # and round it to two decimal places
        total_stock[item] = round(stock[item] * price[item], 2)

# Print the total stock value for each item
print(total_stock)