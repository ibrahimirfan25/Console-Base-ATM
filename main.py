from file_manager import FileManager
from account_info_checker import AccountService
from atm import Atm
from Transaction_amount import TransactionService

def main():
    file_manager = FileManager()
    accounts = file_manager.read_accounts()

    user = AccountService.login(accounts)
    if not user:
        print("Invalid account number or PIN")
        return

    transaction_service = TransactionService(file_manager)
    atm = Atm(user, file_manager, transaction_service)
    atm.start_menu()

if __name__ == "__main__":
    main()
