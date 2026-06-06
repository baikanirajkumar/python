balance_in_account=1000
print("welcome to SBI ATM")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")
choice=int(input("enter the number:"))
if choice==1:
    print("you selected Check Balance")
    pin=input("enter the pin")
    pinlen=len(pin)
    if pinlen==4 and pin=="1234":
        print(f"your current balance is {balance_in_account} Rupees")
    else:
        print("please enter valid pin")
elif choice==2:
    print("you selected Deposit Money")
    deposit_money=int(input("enter the amount to deposit:"))
    if deposit_money>=100:
        balance_in_account+=deposit_money
        print(f"your current balance in account is {balance_in_account}")
    else:
        print("minimum amount to deposit is more than 100")
elif choice==3:
    print("you selected Withdraw Money")
    withdraw_amount=int(input("enter the amount"))
    if withdraw_amount<=balance_in_account:
        print("withdraw successful")
        balance_in_account-=withdraw_amount
        print(f"your current balance is {balance_in_account}")
    else:
        print("insufficient balance")
elif choice==4:
    print("you selected exit")
    print("Thank You visit again")
else:
    print("choose correct option")

