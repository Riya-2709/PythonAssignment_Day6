import json
import os

# File path for storing expenses
FILE_NAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "expenses.json"
)


# Load expenses from JSON file
def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


# Save expenses to JSON file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense(expenses):
    description = input("Enter expense description: ")

    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        expense = {
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount! Please enter a number.")


# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n----- EXPENSES -----")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['description']} - "
            f"₹{expense['amount']:.2f}"
        )


# Delete an expense
def delete_expense(expenses):
    if not expenses:
        print("No expenses available to delete.")
        return

    view_expenses(expenses)

    try:
        number = int(input("Enter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        removed_expense = expenses.pop(number - 1)
        save_expenses(expenses)

        print(
            f"Deleted: {removed_expense['description']} "
            f"- ₹{removed_expense['amount']:.2f}"
        )

    except ValueError:
        print("Invalid input! Please enter a number.")


# Calculate total spending
def total_spending(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Spending = ₹{total:.2f}")


# Display menu
def show_menu():
    print("\nEXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spending")
    print("5. Exit")


# Main program
expenses = load_expenses()

while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        delete_expense(expenses)

    elif choice == "4":
        total_spending(expenses)

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please select 1-5.")