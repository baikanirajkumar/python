# # x=int(input("enter the number:"))
# # print(x)


# #if in try block there is no error then else and finally blocks will execute..if there is error in try then except and finally block will execute
# try:
#     x=int(input("enter the number"))
#     print(x)
# except ValueError:
#     print("you have given non-numeric please give numeric value")
#     x=int(input("enter the number:"))
#     print(x)
#     print("exception handled",x)
# else:
#     print("this is else block")
# finally:  #it executes always even though error is there
#     print("this is final block")


# another example
# Example-1:
x=input("enter number1:")
y=input("enter number 2:")
try:
    z=int(x)/int(y)
    print(z)
except Exception as e:
    print("exception occured:",e)
    print(e)