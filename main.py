from file_checker import FileManager
from account_info_checker import AccountService
from atm import Atm

def main():
    file_manager = FileManager()
    file_manager.ensure_accounts_file()

    accounts = file_manager.read_accounts()

    account_service = AccountService()
    user = account_service.login(accounts)

    if user:
        atm = Atm(user, file_manager)  
        atm.start_menu()
    else:
        print("Invalid account number or PIN")

if __name__ == "__main__":
    main()
