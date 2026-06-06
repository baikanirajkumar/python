# x=int(input("enter the number:"))
# if x>50:
#     print("enter valid number")
# while x<=50 and x>=1:
#       print("the value of x",x)
#       x+=1
# print("end of loop")



# table printing format using while loop

# a=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(a,"*",i,"=",a*i)
#     i+=1

# a=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(a,"*",i,"=",a*i)
#     i+=1

# # fibonacci series
# a=int(input("enter the number:"))
# a=a-2
# b=0
# c=1
# print(b)
# print(c)
# for i in range(a):
#     d=b+c
#     print(d)
#     b=c
#     c=d


#checking prime number or not using for loop
# a=int(input("enter the number:"))
# if a>1:
#     for i in range(2,a):
#         if a%2==0:
#             print("it is not a prime number")
#             break
#         else:
#             print("it is prime number")
#             break
# else:
#     print("it is not a prime number")

# a=int(input("enter the number:"))
# if a>1:
#     i=2
#     while i<=a//2:
#         if a%i==0:
#             print("it is not a prime number")
#             break
#         i+=1
#     else:
#         print("it is a prime number")
# else:
#     print("it is not a prime number")

# replacing
a=str(input("enter the string:"))
b=len(a)
z=0
output=""
while z<b:
    i=a[z]
    if a[z]==a[2]:
        i="*"
        output+=i
    else:
        output+=i
    z+=1
print(output)
    
    
