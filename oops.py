# x=100
# class cl_1(): #class declaration
#     x=100     #class variable(inside class variable is called class variable)
#     def m_1(self): # method 
#         pass



# def fun_1(self):   #function
#     print("hello")
# fun_1(100)

class classname():
    x="hello world"
    def fun_2(self,a,b,z):  #method
        print(classname.x)
        print("inside class",z.x)
        return "method",a,b
c=classname()  #object creation
print(c.fun_2(1000,2000,c))
print("classname",classname.x)
print("classname",c.x)

