class CreateAcc:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New Balance: ${self.balance:.2f}.")
        else:
            print("Deposited amount must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        elif amount <= 0:
            print("Withdrawal amount must be positive")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount: .2f}. New Balance: ${self.balance: .2f}.")

    def CheckBalance(self):
        print(f"Current Balance: ${self.balance: .2f}.")


def bankingsystem():
    account = CreateAcc()
    while True:
        print("\nOptions: deposit, withdraw, check balance, exit")
        user = input("What would you like to do? "). lower()

        if user == "deposit":
            amount = float(input("Enter amount to depsoit: "))
            account.deposit(amount)

        elif user == "withdraw":
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)

        elif user == "Checkbalance":
            account.CheckBalance()

        elif user == "exit":
            print("Existing the Account")
            break
        else:
            print("Invalid Options")

bankingsystem()