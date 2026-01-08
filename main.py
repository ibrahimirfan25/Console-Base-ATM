from file_checker import FileManager
from account_info_checker import AccountService

def main():
    file_checker = FileManager()
    file_checker.ensure_accounts_file()

    accounts = file_checker.read_accounts()

    account_service = AccountService()
    user = account_service.login(accounts)

    if user:
        print("ACCESS GRANTED")
        print(f"Welcome {user['NAME']}")
        print(f" your balance is {user['Balance']}")

    else:
        print("invalid account number")

if __name__ == "__main__":
    main()
    

