# Define the menu items and their corresponding prices
menu = ["americano", "latte", "cappuccino", "hot chocolate"]

# Define the stock quantity for each menu item
stock = {"americano": 107, "latte": 102, "cappuccino": 103, "hot chocolate": 101}

# Define the price for each menu item
price = {"americano": 3.70, "latte": 4.35, "cappuccino": 4.50, "hot chocolate": 4.10}

# Initialize a variable to store the total stock value
total_stock_value = 0

# Iterate through each menu item
for item in menu:
    # Check if the item exists in both stock and price dictionaries
    if item in stock and item in price:
        # Calculate the value of the current item by multiplying the stock quantity with the price
        item_value = stock[item] * price[item]
        # Add the item_value to the total_stock_value
        total_stock_value += item_value

# Print the total stock value
print("Total stock value:", round(total_stock_value, 2))