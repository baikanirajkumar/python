from multipledispatch import dispatch
# class c_1():
#     @dispatch()
#     def met_1(self):
#         print("this is method 1")
#     @dispatch(str)
#     def met_1(self,a):
#         print("this is method 2")
#         print("a=",a)
#     @dispatch(int,float)  # if we write object as parameter it will any type of data
#     def met_1(self,b,c):
#         print("this is method 3")
#         print("b=",b)
#         print("c=",c)
# obj=c_1()
# obj.met_1("rajkumar")
# obj.met_1(10,12.3)
# obj.met_1()


#another example with object as parameter

class c_1():
    @dispatch()
    def met_1(self):
        print("this is method 1")
    @dispatch(object)
    def met_1(self,a):
        print("this is method 2")
        print("a=",a)
    @dispatch(object,object)  # if we write object as parameter it will any type of data
    def met_1(self,b,c):
        print("this is method 3")
        print("b=",b)
        print("c=",c)
obj=c_1()
obj.met_1(10)
obj.met_1("rajkumar",12)
obj.met_1()
