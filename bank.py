class BankAccount:
    """
    Represents a simple bank account with basic deposit and withdrawal functions.
    """
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        # Ensure the initial balance is non-negative
        if initial_balance >= 0:
            self._balance = initial_balance  # _balance is a convention for a protected variable
        else:
            print("Warning: Initial balance cannot be negative. Setting to 0.")
            self._balance = 0

    def get_balance(self):
        """Returns the current balance of the account."""
        return self._balance

    def deposit(self, amount):
        """Adds a positive amount to the balance."""
        if amount > 0:
            self._balance += amount
            print(f"Deposit successful. ${amount:.2f} credited.")
            return True
        else:
            print("Error: Deposit amount must be positive.")
            return False

    def withdraw(self, amount):
        """Subtracts a positive amount from the balance, if funds are available."""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
       
        if amount > self._balance:
            print("Error: Insufficient funds.")
            return False
       
        self._balance -= amount
        print(f"Withdrawal successful. ${amount:.2f} debited.")
        return True

    def __str__(self):
        """String representation of the object for printing."""
        return f"Account Holder: {self.account_holder}\nCurrent Balance: ${self._balance:.2f}"