# #check the given number is positive
# a=int(input("enter the number:"))
# if a>0:
#     print("the given number is positive number")


# #check if the string is empty or not
# a=input("enter the string:")
# if a=="" or len(a)==0 or not a:
#     print("the given string is empty")
# else:
#     print("the given string is not empty")


# #positive or negative or zero
# a=int(input("enter the number:"))
# if a>0:
#     print("the given number is positive")
# elif a<0:
#     print("the given number is negative")
# else:
#     print("the given number is zero")

#check if the number is multiple of both 3 and 5
# a=int(input("enter the number:"))
# if a%3==0 and a%5==0:
#     print("number is multiple of both 3 and 5")
# elif a%3==0 and not a%5==0:
#     print("number is mutiple of only 3")
# elif a%5==0 and not a%3==0:
#     print("the number is multiple of only 5")



# #perfect square or not
# a=int(input("enter the number:"))
# n=(a)**(1/2)
# b=n*n
# if a==b:
#     print("perfect square")
# else:
#     print("not perfect square")

# a=int(input())
# b=(a)**(1/2)
# print(b)

# #check if a number is divisible by 2 and 3
# a=int(input("enter the number:"))
# if a%2==0 and a%3==0:
#     print("the given number is divisible by 2 and 3")
# else:
#     print("the given number is not divisible by 2 and 3")

# a=int(input("enter the number:"))
# b=round(a**(1/3))
# c=b*b*b
# if a==c:
#     print("the given number is perfect cube")
# else:
#     print("the given number is not perfect cube")

# #checking if a given year is leap or not
# a=int(input("enter the number:"))
# if a%4==0 and a%100!=0 or a%400==0:
#     print("the given year is leap")
# else:
#     print("the given number is not leap year")

# #check if a given character is vowel or character
# a=str(input("enter the string:"))
# if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
#     print("the given character is vowel")
# else:
#     print("the given charater is not vowel")


# #check if a given year is centuary year or not
# a=int(input("enter the number:"))
# if a%100==0:
#     print("the given year is centuary year")
# else:
#     print("not a centuary year")

# #check person is eligible for vote or not
# age=int(input("enter the age:"))
# if age>=18:
#     print("he is eligible for voting")
# else:
#     print("he is not eligible for voting")

# #compare two numbers print largest
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# if a>b:
#     print(a)
# else:
#     print(b)

# #check given character is letter is not
# a=input("enter the character:")
# if a.isalpha():
#     print("it is letter")
# else:
#     print("not letter")


# smallest of three numbers

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# if a<b and a<c:
#     print(f"{a} is smallest number")
# elif b<a and b<c:
#     print(f"{b} is smallest number")
# else:
#     print(f"{c} is smallest number")


# #given string is palindrome or not
# a=str(input("enter the string:"))
# b=a[::-1]
# if a==b:
#     print("the given string is palindrome")
# else:
#     print("the given string is not palindrome")


# #print largest of four numbers
# a=int(input("eneter the number:"))
# b=int(input("eneter the number:"))
# c=int(input("enter the number:"))
# d=int(input("eneter the number:"))
# if a>b and a>c and a>d:
#     print(f"{a} is greatest")
# elif b>a and b>c and b>d:
#     print(f"{b} is greatest number")
# elif c>a and c>b and c>d:
#     print(f"{c} is greatest number")
# else:
#     print(f"{d} is greatest number")

# a=int(input("eneter the number:"))
# b=int(input("enter the number:"))
# difference=a-b
# print(difference)
# if difference>0:
#     print("positive number")
# else:
#     print("negative number")


# a=int(input("enter the number:"))
# if a%7==0:
#     print("multiple of 7")
# else:
#     print("not multiple of 7")


# # convert fahrenheit to celsius or vice-versa
# print("1.convert celsius to fahrenheit")
# print("2.convert fahrenhit to celsius")
# a=int(input("enter the number:"))
# if a==1:
#     b=float(input("enter the celsius value:"))
#     fahrenheit=(b*9/5)+35
#     print(fahrenheit)
# elif a==2:
#     c=float(input("enter the fahrenheit value"))
#     celsius=(c-35)*5/9
#     print(celsius)
# else:
#     print("select the correct option")


# import random
# b=random.randint(1,10)
# print(b)
# while True:
#     guess=int(input("enter the number:"))
#     if b==guess:
#         print("guessed number is correct")
#     elif b>guess:
#         print("guess number is small")
#     else:
#         print("guess number is big")

##performs basics arithmetic operators
# print("1.addition")
# print("2.subtraction")
# print("3.multiplication")
# print("4.division")
# b=int(input("enter the number:"))
# if b==1:
#     c=int(input("enter the number:"))
#     d=int(input("enter the number:"))
#     print(c+d)
# elif b==2:
#     e=int(input("enter the number:"))
#     f=int(input("enter the number:"))
#     print(e-f)
# elif b==3:
#     g=int(input("enter the number:"))
#     h=int(input("enter the number:"))
#     print(g*h)
# elif b==4:
#     i=int(input("enter the number:"))
#     j=int(input("enter the number:"))
#     print(i%j)
# else:
#     print("select correct option")

##difference between division,fdivision,mdivision
# i=int(input("enter the number:"))
# j=int(input("enter the number:"))
# print(i%j)
# print(i//j)
# print(i/j)

# #final price of an item after applying a discount based on the purchase amount
# a=int(input("enter the price"))
# if a>4000:
#     discount=40
#     print(discount)
# elif a>3000:
#     discount=30
#     print(discount)
# elif a>2000:
#     discount=20
#     print(discount)
# elif a>1000:
#     discount=10
#     print(discount)
# b=round((discount/a)*100)
# print(b)
# finalprice=a-b
# print(finalprice)





