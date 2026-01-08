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

