# ==========================================
# DecodeLabs - Project 2
# Task 2: Expense Tracker
# ==========================================

# Initialize total expense
total = 0

print("================================")
print("       EXPENSE TRACKER")
print("================================")

while True:

    # Take expense from the user
    expense = input(
        "\nEnter expense amount (or type 'done' to finish): "
    )

    # Check whether the user wants to stop
    if expense.lower() == "done":
        break

    # Convert the input into a number
    try:
        expense = float(expense)

        # Add the new expense to the total
        total = total + expense

        # Display the updated total
        print("Expense added successfully!")
        print("Current Total Spent: ₹", total)

    # Handle invalid input
    except ValueError:
        print("Invalid input!")
        print("Please enter a valid expense amount.")

# Display final result
print("\n================================")
print("       EXPENSE SUMMARY")
print("================================")
print("Total Spent: ₹", total)
print("================================")
print("Thank you for using Expense Tracker!")
