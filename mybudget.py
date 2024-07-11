import datetime

class BudgetTracker:
    def __init__(self):
        self.categories = {}
        self.transactions = []
        self.budget_type = None

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories[category_name] = 0.0

    def add_income(self, category_name, amount):
        self.add_category(category_name)
        self.categories[category_name] += amount
        self.transactions.append((datetime.datetime.now(), category_name, 'Add', amount))

    def deduct_expense(self, category_name, amount):
        self.add_category(category_name)
        self.categories[category_name] -= amount
        self.transactions.append((datetime.datetime.now(), category_name, 'Deduct', amount))

    def move_money(self, from_category, to_category, amount):
        self.deduct_expense(from_category, amount)
        self.add_income(to_category, amount)

    def view_summary(self):
        print("Budget Summary:")
        for category, amount in self.categories.items():
            print(f"Category: {category}, Balance: ${amount:.2f}")

    def view_details(self):
        print("Detailed Budget:")
        for transaction in self.transactions:
            date, category, trans_type, amount = transaction
            print(f"Date: {date}, Category: {category}, Type: {trans_type}, Amount: ${amount:.2f}")

    def setup_budget(self):
        print("Choose Budget Type:")
        print("1. Real Budget")
        print("2. Projected Budget")
        budget_choice = input("Enter your choice: ")

        if budget_choice == '1':
            self.budget_type = "Real"
            self.handle_real_budget()
        elif budget_choice == '2':
            self.budget_type = "Projected"
            self.handle_projected_budget()
        else:
            print("Invalid choice, please try again.")
            self.setup_budget()

    def handle_real_budget(self):
        print("Setting up Real Budget")
        self.collect_income()

    def handle_projected_budget(self):
        print("Setting up Projected Budget")
        self.collect_income()

    def collect_income(self):
        print("Please enter your income details:")
        categories = [
            "Salary/Wages", "Full time work", "Bonuses", "Commissions", "Tips", "Part time work",
            "Freelance/Side Gigs", "Passive money", "Investment income", "Rental Income", "Commercial Income",
            "Government Benefits", "Gifts/Inheritance", "Miscellaneous Income"
        ]

        for category in categories:
            amount_str = input(f"Enter amount for {category}: ")
            amount = float(amount_str.replace(',', ''))
            self.add_income(category, amount)

    def run(self):
        self.setup_budget()
        
        while True:
            print("\nWhat would you like to do?")
            print("1. Add Income")
            print("2. Deduct Expense")
            print("3. Move Money")
            print("4. View Summary")
            print("5. View Details")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                category = input("Enter the category for income: ")
                amount_str = input("Enter the amount: ")
                amount = float(amount_str.replace(',', ''))
                self.add_income(category, amount)
            elif choice == '2':
                category = input("Enter the category for expense: ")
                amount_str = input("Enter the amount: ")
                amount = float(amount_str.replace(',', ''))
                self.deduct_expense(category, amount)
            elif choice == '3':
                from_category = input("Enter the category to move money from: ")
                to_category = input("Enter the category to move money to: ")
                amount_str = input("Enter the amount: ")
                amount = float(amount_str.replace(',', ''))
                self.move_money(from_category, to_category, amount)
            elif choice == '4':
                self.view_summary()
            elif choice == '5':
                self.view_details()
            elif choice == '6':
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    budget_tracker = BudgetTracker()
    budget_tracker.run()
