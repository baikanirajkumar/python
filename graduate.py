# #instance method
# class insta():
#     def __init__(self,name):
#         self.name=name
#     def met_1(self):
#         print("my name is:",self.name)
# obj=insta("rajkumar")
# obj.met_1()


# #class method
# class cla():
#     school="st mathews school"
#     @classmethod
#     def met_1(cls):
#         print("my school name is",cls.school)
# cla.met_1()



# #staticmethod
# class cla():
#     @staticmethod
#     def met_1(a,b):
#         print(a+b)
# obj=cla()
# obj.met_1(1,2)
# cla.met_1(5,3)

#class variable and instance variable
class cls():
    school="eks school" #class variable
    def __init__(self,name,rollno):
        self.name=name #instance variable
        self.rollno=rollno
    def met_1(self):
        print("my school name is",self.school)
        print("my name is",self.name)
        print("my rollno is",self.rollno)
obj=cls("rajkumar",14)
obj.met_1()
print(obj.name,obj.rollno,obj.school)
obj1=cls("ramesh",24)
print(obj1.name,obj1.rollno,obj1.school)