class Atm:
    def __init__(self, user, file_manager):
        self.user = user
        self.file_manager = file_manager

    def show_menu(self):
        print("\nWelcome to the ATM MENU")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

    def check_balance(self):
        print(f"Your current balance is: {self.user['Balance']}")

    def deposit(self):
        try:
            amount = float(input("Enter the amount you want to deposit: "))
            if amount <= 0:
                print("The amount should be greater than zero")
                return
        except ValueError:
            print("Please enter a valid amount")
            return

        new_balance = float(self.user["Balance"]) + amount
        self.user["Balance"] = str(new_balance)

        self.file_manager.update_balance(
            int(self.user["Account Number"]),
            self.user["Balance"]
        )

        print(f"Deposit successful. New balance is: {self.user['Balance']}")

    def withdraw(self):
        try:
            amount = float(input("Enter the amount you want to withdraw: "))
            if amount <= 0:
                print("The amount should be greater than zero")
                return
        except ValueError:
            print("Please enter a valid amount")
            return

        current_balance = float(self.user["Balance"])

        if amount > current_balance:
            print("Insufficient balance")
            return

        new_balance = current_balance - amount
        self.user["Balance"] = str(new_balance)

        self.file_manager.update_balance(
            int(self.user["Account Number"]),
            self.user["Balance"]
        )

        print(f"Withdrawal successful. New balance is: {self.user['Balance']}")

    def start_menu(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                print("Thank you for using the ATM")
                break
            else:
                print("Invalid choice, please try again")
