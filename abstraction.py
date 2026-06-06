# #abstaction (showing functionalities and hiding details)
# from abc import ABC,abstractmethod#here ABC is abstract meta class...if we write only abstact methods in abstract class then it is called as interface class or if it contains abstract method and concrete method it is called abstract class
# class c_1(ABC):  #abstract class ..unable to create object for abstract class
#     @abstractmethod
#     def met_1(self):  #abstract method..method is declared but no scripting
#         pass
#     @abstractmethod
#     def met_2(self):
#         pass
#     def m_3(self,a,b):  #concrete method..here we are unable to create the object for this method so we call it as concrete method..if we are able to create to object then we can call it as instance method
#         print("this method 3 of class1")
#         return a+b,a-b
# class excecute(c_1):  #execution class  for c_1
#     def __init__(self):
#         self.name="raj"
#         self.age=23
#     def met_1(self,a,b): #here we have to take same method name to call the above abstract class methods
#         print("executed class")
#         print("hello codegnan")
#         print("a",a)
#         print("b",b)
#         print(f"my name is {self.name} and my age is {self.age}")
#     def met_2(self,c,d):
#         print("executed class met_2")
#         print("hello codegnan met_2")
#         print("a",c)
#         print("b",d)
#         print(f"my name is {self.name} and my age is {self.age}")
# obj=excecute()
# obj.met_1(10,20)
# obj.met_2(20,40)
# print(obj.m_3(10,20))



#abstraction using inheritance 
from abc import ABC,abstractmethod
class c_1(ABC):  #abstract class ..unable to create object for abstract class
    @abstractmethod
    def met_1(self):  #abstract method..method is declared but no scripting
        pass
    @abstractmethod
    def met_2(self):
        pass
    def m_3(self,a,b):  #concrete method..here we are unable to create the object for this method so we call it as concrete method..if we are able to create to object then we can call it as instance method
        print("this method 3 of class1")
        return a+b,a-b
class excecute(c_1):  #execution class  for c_1
    def __init__(self):
        self.name="raj"
        self.age=23
    def met_1(self,a,b): #here we have to take same method name to call the above abstract class methods
        print("executed class")
        print("hello codegnan")
        print("a",a)
        print("b",b)
        print(f"my name is {self.name} and my age is {self.age}")
class excecute2(excecute):
    def met_2(self,c,d):
        print("executed class met_2")
        print("hello codegnan met_2")
        print("a",c)
        print("b",d)
        print(f"my name is {self.name} and my age is {self.age}")
obj=excecute()
obj.met_1(10,20)
obj.met_2(20,40)
print(obj.m_3(10,20))
