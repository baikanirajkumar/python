#method overloading using module
from multipledispatch import dispatch
# class c_1():
#     @dispatch()
#     def met_1(self):
#         print("this is method 1")
#     @dispatch(str)
#     def met_1(self,a):
#         print("this is method 2")
#         print("a=",a)
#     @dispatch(int,float)  # if we write object as parameter it will take any type of data..example written below
#     def met_1(self,b,c):
#         print("this is method 3")
#         print("b=",b)
#         print("c=",c)
# obj=c_1()
# obj.met_1("rajkumar")
# obj.met_1(10,12.3)
# obj.met_1()


# #another example with object as parameter

# class c_1():
#     @dispatch()
#     def met_1(self):
#         print("this is method 1")
#     @dispatch(object)
#     def met_1(self,a):
#         print("this is method 2")
#         print("a=",a)
#     @dispatch(object,object)  # if we write object as parameter it will any type of data
#     def met_1(self,b,c):
#         print("this is method 3")
#         print("b=",b)
#         print("c=",c)
# obj=c_1()
# obj.met_1(10)
# obj.met_1("rajkumar",12)
# obj.met_1()

# #here it is checking obj is instance of class or not..output is true or false
# print(isinstance(obj,c_1)) 

# #here it is checking x is int type or not
# x=10
# print(isinstance(x,int))



#checking type of parameter example
class c_1():
    def met_1(self,a):
        if type(a) is int:
            print("it is int type of data")
        elif type(a) is str:
            print("it is string type of data")
        elif type(a) is list:
            print("it is list type of data")
obj=c_1()
obj.met_1(19)
obj.met_1("rajkumar")
obj.met_1([1,2,3])

#another example(for two parameters)
class c_1():
    def met_1(self,a,b):
        if type(a) is int and type(b) is str:
            print("it is int type of data and float type of data")
        elif type(a) is str and type(b) is str:
            print("it is string type of data and string type of data")
        elif type(a) is list and type(b) is tuple:
            print("it is list type of data and tuple type of data")
obj=c_1()
obj.met_1(19,"rajkumar")
obj.met_1("rajkumar","chandu")
obj.met_1([1,2,3],(1,2,3))
