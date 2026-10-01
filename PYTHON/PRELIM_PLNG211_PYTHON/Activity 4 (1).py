def get_nonnegative_amount(prompt):
    """Read a valid, non-negative monetary amount from the user."""
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Invalid amount. Please enter zero or a positive number.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")


item_one_cost = get_nonnegative_amount("Enter the cost of item 1: $")
item_two_cost = get_nonnegative_amount("Enter the cost of item 2: $")
payment = get_nonnegative_amount("Enter your payment: $")

total_cost = item_one_cost + item_two_cost

print("\nTotal cost: ${:.2f}".format(total_cost))

if payment < total_cost:
    amount_owed = total_cost - payment
    print("You still owe ${:.2f}.".format(amount_owed))
else:
    change = payment - total_cost
    print("Thank you for your payment.")
    print("Your change is ${:.2f}.".format(change))