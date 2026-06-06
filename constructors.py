# class cl_1():
#     x="rajkumar"   #class variable
#     def __init__(self):  # constructor decalaration
#         self.a1="first instance variable"  # instance variables
#         self.a2="second instance variable"
#         self.a3="third instance variable"
#     def meth_1(self,a,b): #method declaration
#         return a,b,cl_1.x,self.a1,self.a2,self.a3
#     def meth_2(self,l):
#         print(l.x)
# c=cl_1() #object creation
# print(isinstance(c,cl_1))
# print(c.meth_1(10,20))
# print("using object",c.x)
# print("using classname",cl_1.x)
# print(c.a1,c.a2,c.a3)


# #constructor example
# class cl_2():
#     def __init__(self,a,b):
#         self.name=a
#         self.age=b
#         self.desg="dev"
#     def met_1(self):
#         print("name",self.name)
#         print("age",self.age)
#         print("desig",self.desg)
# c=cl_2("abc",20)
# c.met_1()
# d=cl_2("xyz",30)
# d.met_1()
