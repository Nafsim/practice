def menu():
    print("Welcome to ATM")
    print("1.Check Balance")
    print("2.Add Money")
    print("3.Cash out")
    print("4.Exit")
balance = 3500
while True:
    menu()
    choice = input("Enter your choice : ")
    if choice == "1":
        print("Current Balance =", balance, "\n")

    elif choice == "2":
        amount = float(input("Enter amount you want to add: "))
        balance = balance + amount  
        print(" ", amount, "Successfully added")
        print("New Balance =", balance, "\n")

    elif choice == "3":
        amount = float(input("Enter amount you want to cash out: "))
        if amount > balance:
            print(" You don't have enough money!\n")
        else:
            balance = balance - amount
            print("Cash out successfully", amount)
            print("Your current balance:", balance, "\n")

    elif choice == "4":
        print(" Thank you for using the ATM.\n")
        break

    else:
        print(" please enter a valid option.\n")
