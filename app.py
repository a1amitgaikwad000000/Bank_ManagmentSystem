import streamlit as st

# --- BankAccount Class ---
class BankAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0

    def verify_password(self, pwd):
        if pwd == self.password:
            return True
        else:
            st.error("❌ Incorrect password.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            st.success(f"✅ ₹{amount} deposited successfully.")
        else:
            st.warning("❌ Enter a valid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            st.success(f"✅ ₹{amount} withdrawn successfully.")
        else:
            st.error("❌ Insufficient balance or invalid amount.")

    def check_balance(self):
        st.info(f"💰 Current balance: ₹{self.balance}")


# --- Initialize session state ---
if 'accounts' not in st.session_state:
    st.session_state.accounts = {}  # Dictionary to store all accounts

if 'logged_in_user' not in st.session_state:
    st.session_state.logged_in_user = None


# --- Registration Function ---
def register():
    st.subheader("📝 Register New Account")
    with st.form("register_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Register")

        if submit:
            if not username or not password:
                st.warning("⚠️ Please fill in all fields.")
            elif username in st.session_state.accounts:
                st.error("⚠️ Username already exists.")
            else:
                st.session_state.accounts[username] = BankAccount(username, password)
                st.success("✅ Registration successful!")


# --- Login Function ---
def login():
    st.subheader("🔐 Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            if username in st.session_state.accounts:
                account = st.session_state.accounts[username]
                if account.password == password:
                    st.session_state.logged_in_user = account
                    st.success(f"✅ Welcome back, {username}!")
                    st.rerun()
                else:
                    st.error("❌ Invalid password.")
            else:
                st.error("❌ Username not found.")


# --- Logout Function ---
def logout():
    st.session_state.logged_in_user = None
    st.success("🚪 Logged out successfully.")
    st.rerun()


# --- Main App ---
def main():
    st.title("🏦 Secure Bank System")

    # Show login/register if not logged in
    if st.session_state.logged_in_user is None:
        choice = st.sidebar.selectbox("Choose Action", ["Login", "Register"])

        if choice == "Register":
            register()
        elif choice == "Login":
            login()

    # If logged in, show bank menu
    else:
        user = st.session_state.logged_in_user
        st.sidebar.success(f"Logged in as {user.username}")
        if st.sidebar.button("Logout"):
            logout()

        st.header(f"Welcome, {user.username}! 💼")
        st.markdown("---")

        # Bank operations
        action = st.selectbox("Choose Action", ["Deposit", "Withdraw", "Check Balance"])

        if action == "Deposit":
            st.subheader("💵 Deposit Money")
            amount = st.number_input("Enter amount to deposit", min_value=0.0, step=1.0)
            if st.button("Deposit"):
                user.deposit(amount)

        elif action == "Withdraw":
            st.subheader("💸 Withdraw Money")
            amount = st.number_input("Enter amount to withdraw", min_value=0.0, step=1.0)
            if st.button("Withdraw"):
                user.withdraw(amount)

        elif action == "Check Balance":
            st.subheader("💰 Your Balance")
            user.check_balance()


# Run the app
if __name__ == "__main__":
    main()
