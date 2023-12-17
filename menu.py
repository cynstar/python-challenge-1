# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

order_list = []
#CE-upon review I declared a second list so I have a list containing the cumulative order_list.
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
                    # CE - menu_category_name is the menu category selected, eg. "Snacks"
            item_number = input(f"Type {menu_category_name} item number: ")

            # 3. Check if the customer typed a number
            if item_number.isdigit():
                # Convert the menu selection to an integer
                # CE - value entered was converted from string format to integer
                item_number = int(item_number)

                # 4. Check if the menu selection is in the menu items
                #CE - check if the numeric entry example: 1, is in the menu_items dictionary
                if item_number in menu_items.keys():
                    # Store the item name as a variable
                    # CE- item name contained name and price. created a variable for each
                    item_name_price = menu_items[item_number]
                    # CE - the name dict value is now a string below
                    item_name = item_name_price['Item name']
                    #CE - the item price is now a float type
                    item_price = float(item_name_price['Price'])

                    # Ask the customer for the quantity of the menu item
                    item_qty = input(f'You selected {item_name}. How many would you like? ')

                    # Check if the quantity is a number, default to 1 if not
                    if item_qty.isdigit():
                        item_qty = int(item_qty)
                        #CE - print(f"{item_qty} is now an integer")
                        #CE - added a check that input is > 0
                        if item_qty > 0:
                            order_list = [
                                    {"menu item name": item_name},
                                    {"item price": item_price},
                                    {"quantity ordered":item_qty}
                                    ]
                            # CE - appending to the overall order list to collect each order_list.
                            order.append(order_list)
                        else:
                            print(f"Quantity must be more than 0.")
                    # CE - instruction above seems to be part of the True, moved
                    # Tell the customer that their input isn't valid
                    else:
                        item_qty = 1
                        #CE - print(f"{item_qty} was defaulted to integer 1")   
                        print(f"Your input is invalid.")

                # Tell the customer they didn't select a menu option
                else:
                    print(f"A valid menu option was not selected.")
            #CE - added this line. I don't see an else if item number isn't a digit.
            else:
                print(f"Your input is invalid.")
                
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        # CE - corrected this while True loop with assistance from chatgpt
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()
        # Complete the order
        # Since the customer decided to stop ordering, thank them for
        # their order
        if keep_ordering == "y":
            # Keep ordering
            print(order_list)
            print(order)
            break  # Exit the keep ordering question loop

            # Exit the keep ordering question loop
        elif keep_ordering == "n":
            print("Thank you for placing your order.")
            place_order = False
            break  # Exit both the inner and outer loops
               # Tell the customer to try again 
        else:
            print("Invalid entry. Please try again.")



# Print out the customer's order
print("This is what we are preparing for you.\n")

# # Uncomment the following line to check the structure of the order
# print(order)

# CE - added this order below to work through the next steps without needing to go through the ordering functionality again.
# order = [[{'menu item name': 'Soda - Small'}, {'item price': 1.99}, {'quantity ordered': 2}], [{'menu item name': 'Burger - Chicken'}, {'item price': 7.49}, {'quantity ordered': 1}], [{'menu item name': 'Tea - Thai iced'}, {'item price': 3.99}, {'quantity ordered': 2}]]


print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for x in order:

    # 7. Store the dictionary items as variables
    item = x[0]['menu item name']
    price = x[1]['item price']
    qty = x[2]['quantity ordered']
    the_order = [item, price, qty]


    # 8. Calculate the number of spaces for formatted printing
# I asked chatgpt why the way I did it wasn't working and it indicated that it was due to how I had the parenthesis plus I was attempting to subtract from float. I've revised based on the clarifications.
      # 9. Create space strings
    space = " "
    string_price = str(price) 
    formatted = f' {item}{space * (25-len(item))}| {string_price}{space * (7-len(string_price))}| {qty}'


    # 10. Print the item name, price, and quantity
    print(formatted)

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
    #CE - I couldn't figure out how to create this list comprehension. I kept getting only the sum of one value instead of the sum of all the values. 

   #total_cost = sum([])
# Total_Cost = [price * qty for x in order]
# print(Total_Cost)