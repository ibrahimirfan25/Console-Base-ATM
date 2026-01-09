import os
import csv

class FileManager:
    def __init__(self, filename="accounts.csv"):
        self.filename = filename

    def ensure_accounts_file(self):
        if not os.path.isfile(self.filename):
            with open(self.filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Account Number", "NAME", "PIN", "Balance"])
                writer.writerow([12345, "ibrahim", 1111, 12000])
                writer.writerow([20345, "ali", 2222, 10000])
                writer.writerow([30213, "ahmed", 3333, 20000])

    def read_accounts(self):
        with open(self.filename, mode="r", newline="") as file:
            return list(csv.DictReader(file))

    def update_balance(self, account_number, new_balance):
        # 1. Read all accounts from CSV
        accounts = self.read_accounts()

        # 2. Update balance of matching account
        for account in accounts:
            if int(account["Account Number"]) == account_number:
                account["Balance"] = str(new_balance)

        # 3. Write updated accounts back to CSV
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["Account Number", "NAME", "PIN", "Balance"]
            )
            writer.writeheader()
            writer.writerows(accounts)
