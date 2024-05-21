user = {'pin':8899 , 'balance': 1909}

def withdraw_cash():
    """Withdraw cash from the account."""
    while True:
        amount = int(input("Enter the amount of money you want to withdraw: "))
        if amount > user['balance']:
            print("You don't have sufficient balance to make this withdrawal.")
        else:
            user['balance'] -= amount
            print(f"{amount} Dollars successfully withdrawn. Your remaining balance is {user['balance']} Dollars.")
            print('')
            return False

def deposit_cash():
    """Deposit cash into the account."""
    amount = int(input("Enter the amount of money you want to deposit: "))
    user['balance'] += amount
    print(f"{amount} Dollars successfully deposited. Your updated balance is {user['balance']} Dollars.")
    print('')

def balance_enquiry():
    """Check the account balance."""
    print(f"Total balance: {user['balance']} Dollars")
    print('')

is_quit = False

print("Welcome to the ATM")
pin = int(input("Please enter your four-digit PIN: "))

if pin == user['pin']:
    while not is_quit:
        print("\nWhat do you want to do?")
        print("1. Withdraw Cash")
        print("2. Deposit Cash")
        print("3. Balance Enquiry")
        print("4. Quit")
        query = int(input("Enter the number corresponding to the activity you want to do:"))

        if query == 1:
            withdraw_cash()
        elif query == 2:
            deposit_cash()
        elif query == 3:
            balance_enquiry()
        elif query == 4:
            is_quit = True
        else:
            print("Please enter a correct value shown.")
else:
    print("Entered wrong PIN.")
