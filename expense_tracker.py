from expenses import Expense 

def main():
    print(f"Running Expense Tracker")
    expense_file_path = "expenses.csv"
    budget = 2000

    # User inputs expense
    #expense = get_user_expense()
    
    # Write expense to a file
    #save_expense_to_file(expense, expense_file_path)

    # Read file and summarise the expenses
    summarise_expense(expense_file_path, budget)
    


def get_user_expense(): 

    # Getting and recording information

    print("Getting User Expense")
    expense_name = input("Enter Expense Name: ")
    expense_amount = float(input("Enter Expense Amount: "))

    # Create a list of categories

    expense_categories = [ "🍔 Food", "🏡 Home", "💼 Work", "🎉 Fun", "✨ Misc"]
    
    while True:
        print("Select Category: ")
        for i, category_name in enumerate(expense_categories):
            print(" ", i+1, "- ", category_name)

        value_range = f"[1 - {len(expense_categories)}]"

        #the variable stores the index the user picked -1 in order to reflect the way python uses zero indexing
        selected_index = int(input(f"Enter a category number {value_range}:  ")) - 1 

        # Ensuring users selects index within specified range

        if selected_index in range(0, len(expense_categories)):
            
            # Getting the selected catgory based on the index
            selected_category = expense_categories[selected_index]

            # Accessing othe file expenses.py for the classes
            new_expense = Expense( name = expense_name,  category = selected_category, amount = expense_amount)
            
            return new_expense
        else:
            print("Invalid category. Please Try again")
        
          
#to add emojis control, command, space

def save_expense_to_file(expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")

    # the a is for append at it adds to the file 
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarise_expense(expense_file_path, budget):
    print("Summarising Expense")

    expenses: list[Expense] = []

    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            #removes extra lines
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense (
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            expenses.append(line_expense)
    
    amount_by_category  = {}

    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense_amount
        else:
            amount_by_category[key] = expense_amount
    
    print("Print Expenses by Category: ")
    for key, amount in amount_by_category.items():
        print(f"  {key}: £{amount:.2f}")

    # Sum accepts a list as an argument so this then take only the values of the amount from our expenses list and sums them up
    total_spent = sum([x.amount for x in expenses])
    print(f" You have spent £{total_spent} this month!")

    remaining_budget = budget - total_spent

    print(f" You have remaining £{remaining_budget:.2f} for the rest of this month!")

if __name__ == "__main__": 
## this is only true when we run it directly istead of importing it
    main()