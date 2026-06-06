# class small_value(Exception):
#     pass
# class large_value(Exception):
#     pass

# def fun_1(x):
#     if type(x) is str:
#         raise ValueError
#     elif x<100:
#         raise small_value
#     elif x>500:
#         raise large_value
#     else:
#         print(x,"type of x is",type(x))

# try:
#     fun_1(eval(input('enter the value:')))
#     print("should enter the number between 100 and 500 and not string")
# except ValueError:
#     print("the user enter the string data")
#     print("please enter the non string type of data")
#     x=input("enter the number:")
#     print("x=",int(x))
# except small_value:
#     print("you entered the number less than 100")
#     x=input("please enter the number is grater than 100 and lessthan 500:")
#     print("x=",int(x))
# except large_value:
#     print("you entered the number greater than 500")
#     x=input("enter the number less than 500 and greater than 100:")
#     print("x=",int(x))


#customize exception....to know what is the reason of raising exception in detail by customizing
class small_value(Exception):
    pass
class large_value(Exception):
    pass

def fun_1(x):
    if x<600:
        raise small_value("you entered the value is less than 600")
    elif x>700:
        raise large_value("you entered the value is greater then 700")
    else:
        print("x=",x)
try:    
    fun_1(100)
except Exception as e:
    print("e",e)