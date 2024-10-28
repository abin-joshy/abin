balance_amount=1000
while True:
    print("\n1.\tcheck Balance\n2.\tDeposit Money\n3.\tWithdraw Money\n"
          "4.\tExit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print(f"The current balance ${balance_amount}")
    elif choice==2:
        deposit_amount=float(input("Enter the amount you want to deposit:"))
        balance_amount=balance_amount+deposit_amount
        print(f"The deposited amount is ${deposit_amount} and\n"
              f"The current balance is ${balance_amount}")
    elif choice==3:
        withdraw_amount=float(input("Enter the amount to be withdrawn:"))
        balance_amount=balance_amount-withdraw_amount
        if balance_amount<0:
            print("Insufficient Balance")
        else:
            print(F"The amount withdraw from the account is ${withdraw_amount}"
              F"The balance amount is ${balance_amount}")
    elif choice==4:
        break
    else:
        print("Invalid Entry")
