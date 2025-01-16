class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the specified amount if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.__account_balance:
            print("Insufficient funds.")
            return False
        self.__account_balance -= amount
        print(f"Withdrew: ${amount:.2f}")
        return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")