# n = int(input("Enter the number: "))
# d = 2

# while d <= n // 2:
#     if n % d == 0:
#         print("Not a prime number")
#         break
#     d += 1
# else:
#     print("Prime number")



# number=int(input("enter the number:"))
# d=2
# while d<=number//2:
#     if number%d==0:
#         print("not a prime number")
#         break
#     d+=1
# else:
#     print("it is prime number")



# a=int(input("enter the number:"))
# if a>=5:
#     print("he is tall")
# elif a<5 and a>3:
#     print("he is medium")
# else:
#     print("he is short")



# #it is to check the numbers less than 20
# n = int(input("Enter a number: "))

# if n in (2, 3, 5, 7, 11, 13, 17, 19):
#     print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")


a=int(input("enter the number:"))
if a<=1:
    print("it is not a prime number")
else:
    for i in range(2,a):
        if a%i==0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")





           