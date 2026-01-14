class Atm:
    def __init__(self, user, file_manager, transaction_service):
        self.user = user
        self.file_manager = file_manager
        self.transaction_service = transaction_service

    def show_menu(self):
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transfer\n5. Exit")

    def check_balance(self):
        print("Balance:", self.user["Balance"])

    def deposit(self):
        amount = int(input("Enter amount: "))
        self.user["Balance"] = str(int(self.user["Balance"]) + amount)

        accounts = self.file_manager.read_accounts()
        for acc in accounts:
            if acc["Account Number"] == self.user["Account Number"]:
                acc["Balance"] = self.user["Balance"]

        self.file_manager.write_accounts(accounts)

    def withdraw(self):
        amount = int(input("Enter amount: "))
        if amount > int(self.user["Balance"]):
            print("Insufficient balance")
            return

        self.user["Balance"] = str(int(self.user["Balance"]) - amount)

        accounts = self.file_manager.read_accounts()
        for acc in accounts:
            if acc["Account Number"] == self.user["Account Number"]:
                acc["Balance"] = self.user["Balance"]

        self.file_manager.write_accounts(accounts)

    def transfer(self):
        to_account = input("Receiver account: ")
        amount = int(input("Amount: "))

        success, msg = self.transaction_service.transfer(
            self.user["Account Number"],
            to_account,
            amount
        )
        print(msg)

    def start_menu(self):
        while True:
            self.show_menu()
            choice = input("Choice: ")

            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                self.transfer()
            elif choice == "5":
                break
