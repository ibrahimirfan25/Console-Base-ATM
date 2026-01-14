class TransactionService:
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def transfer(self, from_account, to_account, amount):
        accounts = self.file_manager.read_accounts()

        sender = None
        receiver = None

        for acc in accounts:
            if acc["Account Number"] == from_account:
                sender = acc
            if acc["Account Number"] == to_account:
                receiver = acc

        if not sender or not receiver:
            return False, "Account not found"

        if int(sender["Balance"]) < amount:
            return False, "Insufficient balance"

        sender["Balance"] = str(int(sender["Balance"]) - amount)
        receiver["Balance"] = str(int(receiver["Balance"]) + amount)

        self.file_manager.write_accounts(accounts)

        return True, "Transfer successful"
