# Student: Godstime Wozuame
# I added the code to show the most expensive and least expensive items in the chart, along with the total.

shopping_list = []
shopping_list_numbered = []
price_list = []

running_total = 0
user_action = ""

options_numbers = [1, 2, 3, 4, 5]
options_list = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]

print("Welcome to the Shopping Cart Program!")
print()

while True:
    print("Please select one of the following:")
    for i in range(len(options_list)):
        option = options_list[i]
        number = options_numbers[i]
        print(f"{number}. {option}")
    try:
        user_action = int(input("Please enter an action: "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")
        continue

    if user_action == 1:
        print("What item would you like to add?")
        add_item = input(">>")
        shopping_list.append(add_item)
        shopping_list_numbered.append(add_item)
        print(f"What is the price of '{add_item}'?")
        try:
            add_price = float(input(">>"))
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue
        price_list.append(add_price)
        print(f"'{add_item.capitalize()}' has been added to the cart.")
        print()

    elif user_action == 2:
        print("The contents of the shopping cart are:")
        for i in range(len(shopping_list)):
            item = shopping_list[i]
            price = price_list[i]
            print(f"{i+1}. {item.capitalize()} - ${price:.2f}")
        print()
    elif user_action == 3:
        print("Which item would you like to remove? Enter the item number:")
        for i in range(len(shopping_list)):
            print(f"{i+1}. {shopping_list[i].capitalize()} - ${price_list[i]:.2f}")
        try:
            remove_index = int(input(">>")) - 1
            if 0 <= remove_index < len(shopping_list):
                removed = shopping_list.pop(remove_index)
                shopping_list_numbered.pop(remove_index)
                price_list.pop(remove_index)
                print(f"'{removed.capitalize()}' has been removed from the cart.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")
    elif user_action == 4:
        running_total = sum(price_list)
        print(f"The total is: ${running_total:.2f}")
        if shopping_list:
            max_price = max(price_list)
            min_price = min(price_list)
            max_index = price_list.index(max_price)
            min_index = price_list.index(min_price)
            print(f"Most expensive item: {shopping_list[max_index].capitalize()} - ${max_price:.2f}")
            print(f"Least expensive item: {shopping_list[min_index].capitalize()} - ${min_price:.2f}")
        else:
            print("Your cart is empty.")
        print()
    elif user_action == 5:
        print("Thank you. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a number from 1 to 5.")