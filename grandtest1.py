# a=str(input("enter the string:"))
# b=len(a)
# z=0
# output=""
# while z<b:
#     i=a[z]
#     if a[z]==a[2]:
#         i="*"
#         output+=i
#     else:
#         output+=i
#     z+=1
# print(output)


a=int(input("enter the number:"))
if a>1:
    i=2
    for i in range(2,a):
        if i<=a//2:
            print("it is not a prime number")
        else:
            print("it is prime number")
else:
    print("it is not a prime number")
