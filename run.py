class BankAccount:

    def __init__(self, name, account_number, account_type, branch, balance=0):
        self.name = name  # Store the name of the account holder
        self.account_number = account_number  # account number
        self.account_type = account_type
        # Store the type of the account (saving or current)
        self.branch = branch  # Store the branch name
        self.balance = balance  # Store the initial balance, default is 0
        self.transactions = []  # List to keep track of transactions

    def deposit(self, amount):
        # Method to deposit money into the account
        if amount > 0:  # Check if the deposit amount is positive
            self.balance += amount
            # Add the deposit amount to the current balance
            self.transactions.append(f"Deposited: £{amount:.2f}")
            # Record the transaction
            self.display_message(f"£{amount:.2f} deposited successfully.")
            # Display deposit success message
        else:
            # If the deposit amount is not positive, show an error message
            self.display_message("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Method to withdraw money from the account
        if amount > 0:  # Check if the withdrawal amount is positive
            if amount <= self.balance:  # Check if there is sufficient balance
                self.balance -= amount
                # Subtract the withdrawal amount from the balance
                self.transactions.append(f"Withdrew: £{amount:.2f}")
                # Record the transaction
                self.display_message(f"£{amount:.2f} withdrawn successfully.")
                # Show withdrawal success message
            else:
                # If the balance is insufficient, show an error message
                self.display_message(
                    f"Insufficient amt.current balance is £{self.balance:.2f}."
                )
        else:
            # If the withdrawal amount is not positive, show an error message
            self.display_message("Withdrawal amount must be positive.")