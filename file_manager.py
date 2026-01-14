import os
import csv

class FileManager:
    def __init__(self, filename="accounts.csv"):
        self.filename = filename
        self.ensure_accounts_file()

    def ensure_accounts_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Account Number", "NAME", "PIN", "Balance"])
                writer.writerow(["12345", "ibrahim", "1111", "12000"])
                writer.writerow(["20345", "ali", "2222", "10000"])
                writer.writerow(["30213", "ahmed", "3333", "20000"])

    def read_accounts(self):
        with open(self.filename, "r", newline="") as file:
            return list(csv.DictReader(file))

    def write_accounts(self, accounts):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["Account Number", "NAME", "PIN", "Balance"]
            )
            writer.writeheader()
            writer.writerows(accounts)
