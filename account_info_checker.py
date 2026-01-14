class AccountService:

    @staticmethod
    def login(accounts):
        account_number = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()

        for account in accounts:
            if (
                account["Account Number"] == account_number
                and account["PIN"] == pin
            ):
                return account

        return None
