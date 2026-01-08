class AccountService:

    def login(self, accounts):
        try:
            account_number = int(input("Enter your account number: "))
            pin = int(input("Enter your PIN: "))
        except ValueError:
            print("Account number and PIN must be numbers.")
            return None

        for account in accounts:   
            if int(account["Account Number"]) == account_number and int(account["PIN"]) == pin:
                return account     

        return None 
