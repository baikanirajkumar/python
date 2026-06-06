# #check if the number is positive,negative or zero
# a=int(input("enter the number:"))
# if a>0:
#     print(f"{a} is positive number")
# elif a==0:
#     print(f"{a} is not positive and not negative")
# else:
#     print(f"{a} is negative number")

# a=input('enter the string:')
# if len(a)==0:
#     print("string is empty")

# b=input("enter the string:")
# if not b:
#     print("the string is empty")

# c=input('enter the string:')
# if c=="":
#     print("it is empty string")

# #check wheather a number is multiple of 3 and 5
# a=int(input("enter the number:"))
# if a%3==0 and a%5==0:
#     print(f"{a} is multiple of both 3 and 5")
# else:
#     print("It is not multiple of both 3 and 5")

# #perfect square
# a=int(input("enter the number:"))#25
# n1=a**(1/2)  #underrroot 25 is 5 
# n2=n1*n1     #5*5
# if a==n2:
#     print('perfect square')
# else:
#     print("it is not perfect square")




# #check if a number is divisible by 2 and 3
# a=int(input("enter the number:"))
# if a%2==0 and a%3==0:
#     print(f"{a} is divisible by 2 and 3")
# else:
#     print(f"{a} is not divisible by 2 and 3")


# #check if a number is perfect cube
# a=int(input("enter the number:"))
# b=round((a)**(1/3))
# c=b*b*b
# if a==c:
#     print(f"{a} is perfect cube")
# else:
#     print(f"{a} is not perfect cube")

# #check if anumber is multiple of 3
# a=int(input("enter the number:"))
# if a%3==0:
#     print(f"{a} is multiple of 3")
# else:
#     print(f"{a} is not multiple of 3")


# #leap year or not
# a=int(input("enter the number:"))
# if a%4==0 and a%100!=0 or a%400==0:
#     print("leap year")
# else:
#     print("not leap year")

# #character is vowel or consonent
# a=input("enter the character:")
# if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
#     print("it is vowel")
# else:
#     print("it is consonent")

# #eligible for voting
# a=int(input("enter the number:"))
# if a>=18:
#     print("eligible for voting")
# else:
#     print("not eligible for voting")

# #centuary year or not
# a=int(input("enter the year:"))
# if a%100==0:
#     print("it is centuary year")
# else:
#     print("it is not centuary year")


# #compare two numbers print largest
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# if a>b:
#     print(f"{a} is greater than {b}")
# else:
#     print(f"{b} is greater than {a}")


# #check given character is letter or not
# a=input("enter the string:")
# if a.isalpha():
#     print("letter")
# else:
#     print("not letter")

#check wheather it is digit or letter
# a=input("enter the string:")
# if a.isdigit():
#     print("digit")
# else:
#     print("letter")

# smallest of three numbers
# a,b,c=input("enter the numbers").split(",")
# if a<b and a<c:
#     print(f"{a} is smaller")
# elif b<a and b<c:
#     print(f"{b} is smaller")
# else:
#     print(f"{c} is smaller")


# #check wheather the given string is palindrome or not
# a=input("enetr the string:")
# if a==a[::-1]:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")


# #print largest of four numbers
# a,b,c,d=input("enter multiple number:").split(",")
# if a>b and a>c and a>d:
#     print(f"{a} is largest")
# elif b>c and b>d:
#     print(f"{b} is largest")
# elif c>d:
#     print(f"{d} is largest")
# else:
#     print(f"{d} is largest")



# a,b=input("enter multiple numbers:").split(",")
# a,b=int(a),int(b)
# c=a-b
# if c>0:
#     print("positive")
# else:
#     print("negative")

# #check a number is multiple of 7 or not
# a=int(input("enter the number:"))
# if a%7==0:
#     print(f"{a} is multiple of 7")
# else:
#     print(f"{a} is not multiple of 7")


# #covert fahrenheit to celsius and vice-versa
# print("1.convert celsius to fahrenheit")
# print("2.convert fahrenheit to celsius")
# choice=int(input("enter the choice:"))
# if choice ==1:
#     celsius=float(input("enter the celsius:"))
#     fahrenheit=(celsius*(9/5))+32
#     print(fahrenheit)
# elif choice==2:
#     fahrenheit=float(input("enter the fahrenheit:"))
#     celsius=((fahrenheit-32)*5/9)
#     print(celsius)
# else:
#     print("enter correct choice")



# #guess the number game
# import random
# number=random.randint(1,10)
# while True:
#     guess=int(input("enter the number:"))
#     if number==guess:
#         print(f"{number} is equals to {guess}")
#         break
#     elif number>=guess:
#         print(f"{number} is greater than or equals to {guess}")
#         break
#     else:
#         print(f"{number} less than {guess}")
#         break


# #factors of a number
# a=int(input("enter the number:"))
# i=1
# while i<=a:
#     if a%i==0:
#         print(i)
#     i+=1



# #final price of an item after applying discount based on purchase amount
# a=int(input("enter the number:"))
# if a>=5000:
#     discount=40
# elif a>=4000:
#     discount=30
# elif a>=3000:
#     discount=20
# elif a>=2000:
#     discount=10
# final_amount=a-(a*discount/100)  #purchase-(purchase*discount/100)..  1000-(1000*40/100)=final amount
# print(f"the final amount is {final_amount}")
# print(f"the discount applied is {discount}")
# #output
# # enter the number:5000
# # the final amount is 3000.0
# # the discount applied is 40



# #checking if x is greater than y and checking x is greater than 15
# x,y=input("enter the numbers:").split(",")
# x,y=int(x),int(y)
# if x>y:
#     if x>15:
#         print(f"yes {x} is grater than 15")
#     else:
#         print(f"{x} is not greater than 15")
# else:
#     print(f"{x} is not greater than {y}")


# #print the letter grade if he score above 70 else the person gets the less than 70 marks he will be failed
# a=int(input("enter the score:"))
# if a>=70:
#     if a>=90:
#         print("A grade")
#     elif a>=80:
#         print("B grade")
#     elif a>=70:
#         print("C grade")
# else:
#     print("Failed")



def palindrome(num):
    rev=0
    temp=num
    while temp>0:
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
    if(num==rev):
        return True
    else:
        return False
    
l=int(input("enter num1"))
r=int(input("enter num2"))
for i in range(l,r+1):
    if i%7==0 and i%5!=0 and not palindrome(i):
       print(i)