import json
from datetime import datetime

# File to store expense data
EXPENSE_FILE = "expenses.json"

def load_expenses():
    """Load expenses from a JSON file."""
    try:
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    """Save expenses to a JSON file."""
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    """Add a new expense."""
    try:
        amount = float(input("Enter amount spent: "))
        description = input("Enter description: ")
        category = input("Enter category (food, transport, entertainment, etc.): ")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        expense = {"amount": amount, "description": description, "category": category, "date": date}
        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)

        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def view_expenses():
    """Display all recorded expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} - {expense['category']}: ${expense['amount']} ({expense['description']})")

def view_summary():
    """Display a summary of expenses by category and month."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    category_summary = {}
    monthly_summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        month = expense["date"][:7]  # Extract YYYY-MM

        category_summary[category] = category_summary.get(category, 0) + amount
        monthly_summary[month] = monthly_summary.get(month, 0) + amount

    print("\nCategory-wise Summary:")
    for category, total in category_summary.items():
        print(f"{category}: ${total:.2f}")
    
    print("\nMonthly Summary:")
    for month, total in monthly_summary.items():
        print(f"{month}: ${total:.2f}")

def main():
    """Main menu for the expense tracker application."""
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
