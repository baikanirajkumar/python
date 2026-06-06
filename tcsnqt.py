# #print numbers from 1 to n using for loop
# a=int(input("enter the number:"))
# for i in range(1,a+1):
#     print(i)


# #print numbers from 1 to n using while loop

# n=int(input("enter the number:"))
# while n<=10:
#     print(n) 
#     n+=1

# #count number of digits(method-1)
# digits=int(input("enter the number:"))
# b=str(digits)
# print(len(b))


# #count number of digits without using len()(method-2)
# a=int(input("enter the number:"))
# count=0
# while a>0:
#     a=a//10
#     count+=1
# print(count)


# #reverse a number using slicing (method-1)
# a=int(input("enter the number:"))
# b=str(a)
# c=b[::-1]
# print(c)

# #reverse a number without using slicing (method-2)  #error because it is not working with numbers ending with 00
# a=int(input("enter the number:"))  
# count=0
# while a>0:
#     b=a%10
#     count=count*10+b
#     a=a//10
# print(count)

#armstrong number
# n=int(input("Enter number"))
# temp=n
# digits=0
# while temp>0:
#     temp=temp//10
#     digits+=1
# num=0
# temp=n
# while temp>0:
#     rem=temp%10
#     num+=rem**digits
#     temp=temp//10
# if num==n:
#     print("Yes")
# else:
#     print("no")


# #how many even and odd digits in a number
# a=int(input("enter the number:"))
# even=0
# odd=0
# while a>0:
#     b=a%10
#     a=a//10
#     if b%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even)
# print(odd)


# a=int(input("enter the number:"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

#fibonacci series
a=int(input("enter the number:"))
b=0
c=1
print(b,end=" ")
print(c,end=" ")
for i in range(a-2,a):
    d=b+c
    print(d,end=" ")
    b=c
    c=d
