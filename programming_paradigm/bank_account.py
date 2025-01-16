class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = initial_balance  # Private attribute for encapsulation

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Deduct the amount from the account balance if sufficient funds exist."""
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")