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
        print("your current balance is  XXXX Rupees")
    else:
        print("please enter valid pin")
elif choice==2:
    print("you selected Deposit Money")
    deposit_money=int(input("enter the amount to deposit:"))
    if deposit_money>=100:
        balance_in_account+=deposit_money
        print("your current balance in account is{balance_in_acccount}")
    else:
        print("minimum amount to deposit is more than 100")
elif choice==3:
    print("you selected Withdraw Money")
elif choice==4:
    print("ypu selected exit")
else:
    print("choose correct option")

