import json

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
            return expenses
    except FileNotFoundError:
        return []


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


expenses = load_expenses()

def add_expense():
    Name = input("Enter expense name: ")

    if not Name.replace(" ", "").isalpha():
        print("invalid name! use letters only. ")
        return
    
    while True:
        try:
            Amount = float(input("Enter expense amount: "))

            if Amount <= 0:
                print("Error: Amount must be greater than zero. ")
            else:
                break

        except ValueError:
            print("Error: please enter a valid number. ")

    expense = {
        "Name" : Name,
        "Amount": Amount
    }

    expenses.append(expense)

    save_expenses()

    print("Expense added successfully! ")



def view_expenses():
    if not expenses:
        print("No expenses recorded yet. ")
        return

    for expense in expenses:
        print(f" {expense["Name"]}:$ {expense ["Amount"] }  ")


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense ["Amount"]

    print(f"Total expenses: ${total}")



def delete_expenses():
    if not expenses:
        print("No expenses available to delete. ")
        return
    print("\n--- YOUR EXPENSES ---")

    for number , expense in enumerate(expenses, start=1):
        print(f"{number}. {expense["Name"]}: ${expense["Amount"]}")


    try:
        choice = int(input("Enter the number of the expense to delete: "))

        if choice < 1 or choice > len(expenses):
            print("invalid selection!")
            return

        confirmation = input("Are you sure you want to delete this expense? (yes/no): ")

        if confirmation.lower() == "yes":
            deleted_expenses = expenses.pop(choice - 1)
            save_expenses()

            print(f"{deleted_expenses["Name"]} deleted successfully!")
        else:
            print("Deleted cancelled.")

    except ValueError:
        print("Please enter a valid number. ")



def main():
     while True:
        print("\n---EXPENSE TRACKER ---")
        print("1. Add expense")
        print("2.view expenses")
        print("3.Calculate total")
        print("4.delete expense")
        print("5.Exit")

        choice = input("choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            delete_expenses()

        elif choice == "5":
            print("come again soon")
        else:
            print("Invalid choice!")




main()





