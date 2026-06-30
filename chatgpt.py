# #check even or odd
# a=int(input("enter the number:"))
# if a%2==0:
#     print("even")
# else:
#     print("odd")

# #print largest of two numbers
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# if a>b:
#     print(a)
# else:
#     print(b)

# #check prime
# a=int(input("enter the number:"))
# if a<=1:
#     print("it is not prime number")
# else:
#     for i in range(2,a):
#        if a%i==0:
#           print("it is not prime number")
#           break
#     else:
#         print("it is prime number")


# #reverse a string
# a=input("enter the string:")
# b=a[::-1]
# print(b)

# #palindrome string
# a=input("enter the string:")
# b=a[::-1]
# if a==b:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")


# #factorial of number
# a=int(input("enter the number:"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# #fibonacci series
# fib=int(input("enter the number:"))
# a=0
# b=1
# print(a)
# for i in range(fib):
#     c=a+b
#     print(c)
#     a=b
#     b=c

# #maximum element from the list
# list=map(int,input("enter the numbers:").split(","))
# print(max(list))

# #count vowels in string
# a=input("enter the string:")
# count=0
# for i in a:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         print(i)
#         count+=1
# print(count)

# #count vowels in string
# a=input("enter the string:")
# count=0
# for i in a:
#     if i in "aeiou":
#         print(i)
#         count+=1
# print(count)

# #swap two numbers
# a=int(input("enter the number1"))
# b=int(input("enter the nuumber2"))
# a,b=b,a
# print(a)
# print(b)

# #remove duplicates from list
# a=input("enter the list").split(",")
# print(list(set(a)))

# #sum of digits
# a=int(input("enter the number:"))
# sum=0
# while a>0:
#     r=a%10
#     sum+=r
#     a=a//10
# print(sum)

# #sort the list
# a=input("enter the list").split(",")
# a.sort()
# print(a)

# #armstrong number
# a=int(input("enter the number"))
# temp=a
# sum=0
# count=len(str(a))
# while a>0:
#     r=a%10
#     sum=sum+r**count
#     a=a//10
# if temp==sum:
#     print("armstrong number")
# else:
#     print("not armstrong number")

for i in range(5):
    for i in range(5):
        if i==4:
            print("*")
        else:
            print("*_",end=" ")
    print()