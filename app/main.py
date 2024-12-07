def show_balance():
    pass

def deposit():
    pass

def withdraw():
    pass

def exit():
    pass

balance = 0
is_running = False

while is_running:
    print("Banking Program")
    print ("1. Show Balance")
    print ("2. Deposit")
    print ("3. Withdraw")
    print ("4. Exit")

    choice = input("Enter valuer (1-4)")

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Invalid choice")





