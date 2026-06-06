#reverse a number
a=123
b=int(str(a)[::-1])
print(b)


# #palindrome number
# a=input("enter the number:")
# b=a[::-1]
# if a==b:
#     print(f"{a} is palindrome")
# else:
#     print(f"{a} is not palindrome")


# #fibonacci series
# n=int(input("enter the number:"))
# a=0
# b=1
# print(a,end=" ")
# print(b,end=" ")
# for i in range(n):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c


# #Second largest number
# a=[10,20,5,6,2,27]
# b=sorted(a,reverse=True)
# print(b)
# print(b[1])


# #factorial
# a=int(input("enter the number:"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# #count vowels in string
# string=input("enter the string:")
# b=0
# for i in string:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         b+=1
#     else:
#         continue
# print(b)

# #method-2
# string=input("enter the string:")
# b=0
# for i in string:
#     if i in "aeiou":
#         b+=1
#     else:
#         continue
# print(b)


# #sort list without using sort()
# a=[10,23,12,56,34]
# b=[]
# print(len(a))
# for i in range(6):
#     if i>a[1] or  



# #check anagram
# def fun(x,y):
#     if sorted(x)==sorted(y):
#         print("it is anagram" )
#     else:
#         print("it is not anagram")
# fun("listen","silent")


# set={}
# b=type(set)
# print(b)



#practice

# a=123
# b=(int(str(a)[::-1]))
# print(b)


# #palimdrome
# a=input("enter the number")
# b=a[::-1]
# if a==b:
#     print(f"{a} is palinfrome")
# else:
#     print(f"{a} is not plaindrome")


# #fibonacci series
# n=int(input("enter the number:"))
# a=0
# b=1
# print(a,end="")
# print(b,end="")
# for i in range(n):
#     c=a+b
#     print(c,end="")
#     a=b
#     b=c

# a=[1,2,1,3,4,5,6,1,3]
# b=sorted(a,reverse=True)
# print(b)
# print(b[1])

# #factorial
# a=int(input("enter the number"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)


# string=input("enter the string:")
# b=0
# for i in string:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         b+=1
#     else:
#         continue
# print(b)


# def fun_1(x,y):
#     if sorted(x)==sorted(y):
#         print("it is anagram")
#     else:
#         print("it is not anagram")
# fun_1("listen","silent")

# #even or odd
# a=int(input("enter the number:"))
# if a%2==0:
#     print("it is even number")
# else:
#     print("it is odd number")


# a,b=input("enter the number:").split(",")
# if a!=b:
#     print(b,a,sep=",")
# else:
#     print(a,b,sep=",")
