# User-defined exception class
class InsufficientBalanceError(Exception):
    def __init__(self, message="Balance is below the minimum required amount of 1000."):
        self.message = message
        super().__init__(self.message)

# BankAccount class
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        try:
            if self.balance - amount < 1000:
                raise InsufficientBalanceError(
                    f"Insufficient funds! Cannot withdraw {amount}. Your current balance: {self.balance}"
                )
            self.balance -= amount
            print(f"Withdrawal successful! New balance: {self.balance}")
        except InsufficientBalanceError as e:
            print(f"Error: {e}")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

# Main program
def main():
    # Create a bank account with an initial balance
    account = BankAccount("123456789", 2000)

    # Display current balance
    account.display_balance()

    # Attempt a withdrawal
    withdrawal_amount = int(input("Enter amount to withdraw: "))
    account.withdraw(withdrawal_amount)

    # Display balance after withdrawal
    account.display_balance()

if __name__ == "__main__":
    main()
