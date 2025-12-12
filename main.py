from bank import BankAccount

def display_menu():
    """Prints the main menu options."""
    print("\n--- Simple Banking Application ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("----------------------------------")

def get_valid_amount(prompt):
    """Prompts the user for a positive numerical amount."""
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            else:
                print("Amount must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Main function to run the banking application."""
   
    # 1. Initialization: Create a BankAccount object
    print("Welcome to the Bank Account Setup.")
    holder_name = input("Enter the account holder's name: ")
    initial_deposit = get_valid_amount("Enter initial deposit amount: $")
   
    # Instantiate the BankAccount class
    account = BankAccount(holder_name, initial_deposit)
    print("\nAccount created successfully!")
    print(account) # Uses the __str__ method from BankAccount
   
    # 2. Main Application Loop
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
       
        if choice == '1':
            # Check Balance
            current_balance = account.get_balance()
            print(f"\n**{account.account_holder}'s Current Balance is: ${current_balance:.2f}**")
           
        elif choice == '2':
            # Deposit
            deposit_amount = get_valid_amount("Enter deposit amount: $")
            account.deposit(deposit_amount)
           
        elif choice == '3':
            # Withdraw
            withdraw_amount = get_valid_amount("Enter withdrawal amount: $")
            account.withdraw(withdraw_amount)
           
        elif choice == '4':
            # Exit
            print("\nThank you for using the Simple Banking Application. Goodbye!")
            break
           
        else:
            print("\nInvalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
