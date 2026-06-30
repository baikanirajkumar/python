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
# x=input("enter number1:")
# y=input("enter number 2:")
# try:
#     z=int(x)/int(y)
#     print(z)
# except Exception as e:
#     print("exception occured:",e)
#     print(e)

"""Exception handling in Python is the process 
handling runtime errors using try, except, else, 
and finally blocks, allowing the program to continue execution without crashing."""


# #ZeroDivisionError
# try:
#     a=10
#     b=0
#     c=a/b
# except ZeroDivisionError:
#     print("Cannot divide by Zero")


# #ValueError
# try:
#     a=int(input("enter the number:"))
# except ValueError:
#     print("please enter a valid integer")

# #KeyError
# try:
#     dict={"name":"rajkumar","age":14}
#     print(dict["rollno"])
# except KeyError:
#     print("Key not found")

# #IndexError
# try:
#     list=[1,2,3,4]
#     print(list[5])
# except IndexError:
#     print("Index out of range")

#NameError
# try:
#     print(x)
# except NameError:
#     print("varaible is not defined")

# #typeerror
# try:
#     print(10+"raj")
# except TypeError:
#     print("Cannot add string and int")


#complete example
try:
    a=int(input('enter the number:'))
    b=int(input("enter the number:"))
    c=a/b
except ZeroDivisionError:
    print("cannot divide with Zero")
except ValueError:
    print("please enter an integer")
else:
    print("result",c)
finally:
    print("program execution completed")