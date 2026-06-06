class classname1():
    x="rajkumar"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def met_1(self):  #method
        print("my name is",self.name)
        print("my age is ",self.age)
    def more_details(self):
        self.met_1()  #wrapping of methods within same class
        print("this is method from classname1")
    def fun_1(self): #function
        print("hello world")
c1=classname1("raj",20)
c1.met_1() # we can call the method using classname
print(c1.name)
print(c1.age)
c1.fun_1()  # we can call the function using classname

# class classname2():
#     def __init__(self,desg,x,y):
#         classname1.__init__(self,x,y) #wrapping of constructors
#         self.desg=desg
#     def met_2(self,a):
#         classname1.met_1(self)  #wrapping of methods ##for below point
#         print("the designation is",self.desg)
#         classname1.fun_1(self,a) #number of parameters and type of parameters should match
# c2=classname2("dev","chandu",13)
# c2.met_2("x value")

# c1=classname1("raj",24)
# c1.more_details()


# #own example
# class c1():
#     def __init__(self,a1,a2):
#         self.a1="raj"
#         self.a2=20
#     def met_1(self):
#         print("my name is",self.a1)
#         print("my age is",self.a2)
#     def met_2(self):
#         print("hello world")
# b1=c1("rajesh",40)
# b1.met_1()

# class c2():
#     x="rajkumar"
#     def __init__(self,x,y):
#         c1.__init__(self,x,y)
#         self.desg="dev"
#     def met_2(self):
#         c1.met_1(self)
#         print("hello codegnan")
#         print("my desg is",self.desg)
#     def fun_1(d):
#         print("this is python")
#         print("desg",d.desg)
# c=c2("arj",30)
# c.met_2()  
# c.fun_1() # here inside class function can be called outside using classname(classname.function())



# d=c2("ramu",30)
# d.met_2()


