# #instance methods
# # 1.works with instance variables
# # 2.uses self as first parameter


# class classname():
#     def __init__(self,name):
#         self.name=name
#     def met_1(self):#instance method
#         print(f"this is {self.name}")
# c=classname("rajkumar")
# c.met_1()


#class methods
# 1.works with class variables
# 2.uses cls as first parameter
# 3.Declared using @classmethod decorator


class classname():
    a="class variable"
    @classmethod
    def met_1(cls):
        print(f"class variable",cls.a)
classname.met_1()
c=classname()
c.met_1()



#static method
# 1.donot use class or instance variables
# 2.used for utility functions
# 3.declared using @staticmethod decorator
# 4.no cls or self

# class classname():
#     @staticmethod
#     def met_1(a,b):
#         print("add",a+b)
# classname.met_1(10,20)
