# Prompt the user for the price of a meal
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Calculate the total price of the meals
total_price = (child_meal * num_children) + (adult_meal * num_adults)
print(f"\nSubtotal: ${total_price:.2f}")

# Prompt the user for the price of a drink and appetizer
drink_price = float(input("What is the price of a drink? "))
num_drinks = int(input("How many drinks are there? "))
appetizer_price = float(input("What is the price of an appetizer? "))
num_appetizers = int(input("How many appetizers are there? "))

# Calculate the total price of drinks and appetizers
total_price_drinks = drink_price * num_drinks
total_price_appetizers = appetizer_price * num_appetizers

# Add the drinks and appetizers to the total price
new_total_price = total_price + total_price_drinks + total_price_appetizers
print(f"Subtotal (including drinks and appetizers): ${new_total_price:.2f}")

# Calculate the sales tax 
sales_tax_rate = float(input("\nWhat is the sales tax rate? "))
sales_tax = (new_total_price * sales_tax_rate) / 100
print(f"Sales Tax: ${sales_tax:.2f}")

# Calculate the total price including sales tax
total_price_with_tax = new_total_price + sales_tax
print(f"Total: ${total_price_with_tax:.2f}\n")

# Calculate the payment amount
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total_price_with_tax
print(f"Change: ${change:.2f}")

# Check for insufficient payment
if change < 0:
    print("Insufficient payment. Please provide more money.")
