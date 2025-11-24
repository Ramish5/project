import random

class BankAccount:
    def __init__(self, name, pin, balance=0):
        
        self.name = name
        self.pin = pin
        self.balance = balance
        self.account_number = self.generate_account_number()
        self.transaction_history = []
        
        
        if balance > 0:
            self.transaction_history.append(f"Account opened with: ${balance}")

    def generate_account_number(self):
        
        return random.randint(10000, 99999)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"Successfully deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"Successfully withdrew ${amount}. New Balance: ${self.balance}")

    def get_balance(self):
        print(f"\n Current Balance: ${self.balance}")

    def show_history(self):
        print(f"\nTransaction History for {self.name}:")
        print("-" * 30)
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for log in self.transaction_history:
                print(log)
        print("-" * 30)
    
def main():
    accounts = {} 

    print("===Welcome to Bank===")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Create New Account")
        print("2. Login to Account")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")

        if choice == '1':

            name = input("Enter your name: ")
            pin = input("Set a 4-digit PIN: ")
            
            
            if len(pin) != 4 or not pin.isdigit():
                print(" PIN must be exactly 4 digits.")
                continue
                
            First_deposit = float(input("Enter First deposit amount (or 0):$ "))
            
            
            new_customer = BankAccount(name, pin, First_deposit)
            
            
            accounts[new_customer.account_number] = new_customer
            
            print(f"\n Account Created Successfully!")
            print(f" YOUR ACCOUNT NUMBER IS: {new_customer.account_number}")
            print("(Please remember this number to login!)")

        elif choice == '2':
            
            try:
                acc_num = int(input("Enter Account Number: "))
            except ValueError:
                print("Invalid input.")
                continue

            if acc_num in accounts:
                current_customer = accounts[acc_num]
                entered_pin = input("Enter PIN: ")

                if entered_pin == current_customer.pin:
                    print(f"\n Welcome back, {current_customer.name}!")
                    
                
                    while True:
                        print("\n--- USER MENU ---")
                        print("1. Check Balance")
                        print("2. Deposit Money")
                        print("3. Withdraw Money")
                        print("4. Transaction History")
                        print("5. Logout")
                        
                        customer_choice = input("Choose action: ")

                        if customer_choice == '1':
                            current_customer.get_balance()
                        elif customer_choice == '2':
                            amout = float(input("Amount to deposit: "))
                            current_customer.deposit(amout)
                        elif customer_choice == '3':
                            amout = float(input("Amount to withdraw: "))
                            current_customer.withdraw(amout)
                        elif customer_choice == '4':
                            current_customer.show_history()
                        elif customer_choice == '5':
                            print(" Logging out,Thnak you for using")
                            break
                        else:
                            print(" Invalid option.")
                else:
                    print(" wrong PIN.")
            else:
                print(" Account not found.")

        elif choice == '3':
            print(" Thank you for using Bank system. Goodbye!")
            break
        else:
            print(" Wrong choice. Please ty again.")

if __name__ == "__main__":
    main()