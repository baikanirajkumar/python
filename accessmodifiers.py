# # in python there are three access modifiers :public,private,protected


#public(access from everywhere)
# class classname():
#     def __init__(self,name,rollno):
#         self.name=name #public

#         self.rollno=rollno
#     def met_1(self):
#         print("this is method 1")
#         print(f"my nameis {self.name} and my rollno is {self.rollno}")
# c=classname("rajkumar","14")
# c2=classname("kumar",30)
# print(c.name)
# print(c.rollno)
# print(c2.name)
# print(c2.rollno)
# c.met_1()



# #protected(access inside the class and subclasses)
# class parent():
#     def __init__(self,name):
#         self._name=name
# class child(parent):
#     def met_1(self):
#         print(f"this is {self._name}")
# c=child("rajkumar")
# c.met_1()

#private(access only inside the class)
class classname():
    x="hello world"
    def __init__(self,name):
        self.__name=name
        self.rollno=14
    def met_1(self):
        print(f"this is {self.__name}")
c=classname("rajkumar")
print(c.x)
print(classname.x)
c.met_1()
print(c.rollno)
print(c._classname__name)





