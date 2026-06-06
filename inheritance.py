# #single inheritance example
# class grand_father():
#     def m_gf1(self):
#         print("this property belongs to grand father")
#     def m_gf2(self,a,b):
#         return a,b,a+b,"this is grandfather method2"
# gf=grand_father()
# # gf.m_gf1()
# print(gf.m_gf2(100,200))


# class father(grand_father):
#     def m_father(self):
#         print("this is father method1")
#     def m_father2(self,f):
#         return f,f*2,"this is father method 2"
        
# f=father()
# f.m_father()
# print(f.m_father2("child class"))
# f.m_gf1()
# print(f.m_gf2(100,200)) #we can call the properties of parent class by using child class object but we cannot call the proprties of child class by using parent class object 


# #example for above point
# grand=grand_father()
# grand.m_gf1()
# print(grand.m_gf2(100,200))

# # gf.m_father() #error for above point example


# #multilvel inhertance
# class child(father):
#     def c_1(self):
#         print("this is child class")
#     def c_2(self,a,b):
#         return a,b,a+b,"this is child class"
# c=child()
# c.c_1()
# print(c.c_2(100,200))
# c.m_father()
# print(c.m_father2("apple"))
# c.m_gf1()

# #multiple inheritance
# class a():
#     def m_1(self):
#         print("this is method 1 of A class")
#     def m_2(self):
#         print("this is method2 of A class")
# class b():
#     def m_3(self):
#         print("this is method 3 of b class")
#     def m_4(self):
#         print("this is method 4 of b class")
# class c():
#     def m_5(self):
#         print("this is method 5 of class c")
#     def m_6(self):
#         print("this is method 6 of class c")
#     def m_n(self):
#         print("this is m_n of class c")
# class child(a,b,c):   # if there are multiple methods with same name it will go through method resolution order(MRO)..first preference is for a(first occurance)
#     def m_7(self):
#         print("this is method of child")
#     def m_n(self):
#         print("this is method of child class")
# d=child()
# d.m_7()
# d.m_1()
# d.m_2()
# d.m_3()
# d.m_4()
# d.m_5()
# d.m_6()
# d.m_n()
# print(child.mro())    #for checking the preferene order
# print(child.__mro__)  #dun dum method 

#hierachical inheritance

class parent():
    def met_1(self):
        print("this is parent class met_1")
    def met_2(self):
        print("this is parent class met_2")
class child_1(parent):
    def met_3(self):
        print("this is child class met_3")
    def met_4(self):
        print("this is child class met_4")
class child_2(parent):
    def met_5(self):
        print("this is child2 met_5")
    def met_6(self):
        print("this is child_2 met_6")
# a=child_2()
# a.met_1()
# a.met_2()
# a.met_5()
# a.met_6()

# we can call the methods in parent with the help of object of child class1 but unable to call childclass2 (vice versa) 
# b=child_1()
# b.met_3()
# b.met_4()
# b.met_1()
# b.met_2()

# #super keyword wrapping of methods
# class parent():
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def met_1(self):
#         print(f"my name is {self.name} and my age is {self.age} and my gender is {self.gender}")
# class child(parent):
#     def __init__(self,id,branch,name,age,gender):
#         self.id=id
#         self.branch=branch
#         super().__init__(name,age,gender)
#     def met_1(self):
#         super().met_1()
#         print(f"my id is {self.id} and branch is {self.branch}")
# d=child("1234","csm","rajkumar","24","male")
# d.met_1()



 #multiple inhertance wrapping of methods
class grand_father():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def m_gf1(self):
        print(f"my name is {self.name} and my age is {self.age}")
class father(grand_father):
    def __init__(self,gender,name,age):
        self.gender=gender
        super().__init__(name,age)
    def m_father(self):
        super().m_gf1()
        print("this is father method1")        
class child(father):
    def __init__(self,gender,name,age,id):
        self.id=id
        super().__init__(gender,name,age)
    def c_1(self):
        super().m_father()
        print("this is child class")
c=child("1234","male","25","rajkumar")
c.c_1()


