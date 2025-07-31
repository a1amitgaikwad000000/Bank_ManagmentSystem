class BankAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0

    def verify_password(self):
        pwd = input("Re-enter password: ")
        if pwd == self.password:
            return True
        else:
            print("❌ Incorrect password.")
            return False

    def deposit(self, amount):
        if self.verify_password():
            if amount > 0:
                self.balance += amount
                print(f"✅ ₹{amount} deposited successfully.")
            else:
                print("❌ Enter valid amount.")

    def withdraw(self, amount):
        if self.verify_password():
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"✅ ₹{amount} withdrawn successfully.")
            else:
                print("❌ Insufficient balance or invalid amount.")

    def check_balance(self):
        if self.verify_password():
            print(f"💰 Current balance: ₹{self.balance}")


# --- Authentication System ---
accounts = {}

def register():
    print("\n--- 📝 Register New Account ---")
    username = input("Enter username: ")
    if username in accounts:
        print("⚠️ Username already exists.")
        return
    password = input("Set a password: ")
    accounts[username] = BankAccount(username, password)
    print("✅ Registration successful!")

def login():
    print("\n--- 🔐 Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in accounts and accounts[username].password == password:
        print(f"✅ Welcome back, {username}!")
        account_menu(accounts[username])
    else:
        print("❌ Invalid username or password.")

def account_menu(account):
    while True:
        print("\n--- 🏦 Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("🚪 Logged out successfully.")
            break
        else:
            print("❌ Invalid choice.")


# --- Main Loop ---
while True:
    print("\n=== 💼 Welcome to Secure Bank System ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    user_choice = input("Select an option: ")

    if user_choice == "1":
        register()
    elif user_choice == "2":
        login()
    elif user_choice == "3":
        print("👋 Thank you for using the system.")
        break
    else:
        print("❌ Invalid input. Try again.")
