# ac_data=["4585 4589 2358","7892 4589 2563","7892 4563 4862"]
# pin-no={"4585 4589 2358":(1235,500.00),"7892 4589 2563":(4555,420.00),"7892 4563 4862":(4778,4889.00)}
# print("welcome to xyz bank")
# a_c_no=str(input("enter 12 digit card number:"))
# if a_c_no in ac_data:
#   pin_no=int(input("enter your pin:"))
#   balance=100000.00
#   if a_c_no !="":
#       if type(pin_no)==int:
#           print("welcome customer what you wanted to proceed:")
#           x="deposite" 
#           y="withdraw"
#           z="mini statement"
#           user_choice=(input("enter what you need from deposite|withdraw|mini statement"))
#           if user_choice==x:
#               print("welcome to deposite space")
#               deposite_amount=float(input("enter deposit:"))
#               balance+=deposite_amount
#               print("amountdeposite is successful","\n your account balance is :",balance)
#           elif user_choice==y:
#               print("welcome to withdraw space")
#               withdraw_amount=float(input("enter amount:")) 
#               if withdraw_amount<=balance:
#                   balance-=withdraw_amount
#                   print("transaction successful \n please collect your cash:")
#                   print("your balance is",balance)
#               elif withdraw_amount>balance:
#                   print(" sorry insufficient funds:")
#               elif user_choice==z:  
#                   print("hello customer","your a/c balance is ",balance)  
#               else:
#                   print("please enter valid one:")    
#       else:
#           print("plz enter the valid pin in number")
#   else:
#       print("enter valid a/c no")

# # print(balance,"called outside of block")   
# else:
#     print("please enter the valid ac_no in xxxx xxxx xxxx form")




pin_no={"4585 4589 2358":(1235,500.00),"7892 4589 2563":(4555,420.00),"7892 4563 4862":(4778,4889.00)}
y=pin_no["4585 4589 2358"]
pin=y[0]
print("pin:",pin)
balance=y[1]
print("balance:",balance)
ac_data=["4585 4589 2358","7892 4589 2563","7892 4563 4862"]
pin=1232
if pin_no[ac_data]