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

# #class variable and instance variable
# class cls():
#     school="eks school" #class variable
#     def __init__(self,name,rollno):
#         self.name=name #instance variable
#         self.rollno=rollno
#     def met_1(self):
#         print("my school name is",self.school)
#         print("my name is",self.name)
#         print("my rollno is",self.rollno)
# obj=cls("rajkumar",14)
# obj.met_1()
# print(obj.name,obj.rollno,obj.school)
# obj1=cls("ramesh",24)
# print(obj1.name,obj1.rollno,obj1.school)


# a=int(input("enter the number:"))
# print(a)

# b,c=input("enter a & b ").split(",")
# print(b,c)

# list=input("enter the list:").split(",")
# print(list)

# a=list(map(int,input("enter the values").split(",")))
# print(a)

# a=eval(input("multiple data"))
# print(a)
# print(type(a))

#string functions
# a="string"
# print(len(a))
# print(max(a))
# print(min(a))
# print(sorted(a))

# a="rajkumar"
# b="baikani"
# c=a+b
# print(c)
# print(c*3)

# print(a>b)
# print(ord("r"))
# print(ord("b"))

# del a
# print(a)
# c=a.upper()
# print(c)
# d="RAJ"
# e=d.lower()
# print(e)

# b=a.capitalize()
# print(b)
# a="this is rajkumar.iam from warangal"
# b="THIS IS RAJKUMAR.IAM FROM WARANGAL"
# print(a.title())
# print(a.swapcase())
# print(b.swapcase())

# a="rajkumar baikani"
# # print(a.index("a"))
# # print(a.index("aj"))
# # print(a.index("ku"))
# print(a.find("aaj"))
# print(a.rfind("a"))
# print(a.rindex("a"))
# print(a.startswith("r"))
# print(a.endswith("i"))
# print(len(a))
# print(a.startswith("a",0,16))
# print(a.endswith("i",0,16))

# a="rajkumar"
# # print(a.rjust(15,"*"))
# # print(a.ljust(15,"*"))
# print(a.center(15,"*"))
# b="88raj88"
# c="rajkumar"
# print(b.strip("8"))
# print(b.lstrip("8"))
# print(b.rstrip("8"))
# print(c.lstrip("raj"))
# print(c.rstrip("kumar"))

# a=input("enter the string:")
# count=0
# for i in a:
#     if i==" ":
#         continue
#     else:
#         count+=1
# print(count)

# x=[1,2,3,4,5]
# x.append(5)
# print(x)
# x.insert(3,5)
# print(x)
# x.extend([6,7])
# print(x)
# x.remove(1)
# print(x)
# x.pop()
# print(x)
# del x[1]
# print(x)
# x.clear()
# print(x)
# x=["a","b","d","a"]
# x.sort(reverse=False)
# print(x)
# x.sort(reverse=True)
# print(x)
# print(len(x))
# print(x.count("a"))
# print(x.index("a"))
# print(max(x))
# print(min(x))

# x=[1,2,3,4]
# # print(sum(x))
# # x[1]="a"
# # print(x)
# y=x.copy()
# print(id(x))
# print(id(y))
# x=["a","z","b","d"]
# x.sort()
# print(x)
# # print(sorted(x))
# y=[True,False,True]
# print(any(y))
# print(all(y))
# x=["a","b","c","d"]
# y=list(enumerate(x))
# print(y)

# class student:
#     school="ABC SCHOOL"
#     def __init__(self,name):
#         self.name=name
#     def met_1(self):
#         print("my name is",self.name,"my school name is",self.school)
# s1=student("rajkumar")
# s1.met_1()
# print(s1.name)
# print(s1.school)

# class student:
#     def __init__(self,name,age,rollno):
#         self.name=name
#         self._age=age
#         self.__rollno=rollno
#     def met_1(self):
#         print("my name is",self.name)
#         print("my age is",self._age)
# s1=student("rajkumar",14,22)
# s1.met_1()
# print(s1.name)
# print(s1._age)
# print(s1._student__rollno)

# class student1(student):
#     def met_1(self):
#         print("my name is",self._age)
# s1=student1("rajkumar",13,22)
# print(s1._age)

# class student():
#     def __init__(self):
#         print("parent constructor")
#     def met_1(self):
#         print("parent method")
# class student1(student):
#     def __init__(self):
#         print("child constructor")
#         super().__init__()
#     def met_2(self):
#         print("child method")
#         super().met_1()
# s1=student1()
# s1.met_2()


# class student():
#     def __init__(self,name):
#         self.name=name
#     def met_1(self):
#         print("my name is ",self.name)
# s1=student("rajkumar")
# s1.met_1()


# class student():
#     school="ABC school"
#     @classmethod
#     def met_1(cls):
#         print("my school name is",cls.school)
# student.met_1()

# class student:
#     @staticmethod
#     def add(a,b):
#         print(a+b)
# student.add(1,2)

# #single inheritance
# class student():
#     def met_1(self):
#         print("this is method 1")
# class student1(student):
#     def met_2(self):
#         print("this is method 2")
# obj=student1()
# obj.met_2()
# obj.met_1()

# #multilevel inheritance
# class student():
#     def met_1(self):
#         print("this is method 1")
# class student1(student):
#     def met_2(self):
#         print("this is method 2")
# class student2(student1):
#     def met_3(self):
#         print("this is method 3")
# obj=student2()
# obj.met_3()
# obj.met_2()
# obj.met_1()

# #multiple inheritance
# class student():
#     def met_1(self):
#         print("this is method 1")
# class student1():
#     def met_2(self):
#         print("this is method 2")
# class student2(student,student1):
#     def met_3(self):
#         print("this is method 3")
# obj=student2()
# obj.met_3()
# obj.met_2()
# obj.met_1()


# #hierarchical inheritance
# class student():
#     def met_1(self):
#         print("this is method 1")
# class student1(student):
#     def met_2(self):
#         print("this is method 2")
# class student2(student):
#     def met_3(self):
#         print("this is method 3")
# obj=student2()
# obj.met_3()
# obj.met_1()
# obj=student1()
# obj.met_2()
# obj.met_1()

# # hierarchical inertance
# class student():
#     def met_1(self):
#         print("this is method 1")
# class student1(student):
#     def met_2(self):
#         print("this is method 2")
# class student2(student):
#     def met_3(self):
#         print("this is method 3")
# class student3(student1,student2):
#     def met_4(self):
#         print("this is method 4")
# obj=student3()
# obj.met_1()
# obj.met_2()


# #polymorphism
# class student():
#     def met_1(self):
#         print('Method1')
# class student1(student):
#     def met_1(self):
#         print("Method2")
# obj=student1()
# obj.met_1()
# obj=student()
# # obj.met_1()

# print(10+20)
# print("hello"+"warangal")

# from abc import ABC,abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class car(vehicle):
#     def start(self):
#         print("car starts with key")
# c=car()
# c.start()

# class Account():
#     def __init__(self):
#         self.__balance=0
#     def deposit(self,amount):
#         self.__balance+=amount
#     def show_balance(self):
#         return self.__balance
# obj=Account()
# obj.deposit(100)
# print(obj.show_balance())

#method overloading
# from multipledispatch import dispatch
# class student():
#     @dispatch()
#     def met_1(self):
#         print("this is method 1")
#     @dispatch(object)
#     def met_1(self,a):
#         print("This is method 2")
#         print(a)
#     @dispatch(object,object)
#     def met_1(self,a,b):
#         print("This is method 3")
#         print(a)
#         print(b)
# obj=student()
# obj.met_1()
# obj.met_1(10)
# obj.met_1(20,30)

#method overriding
class c1():
    # def met_1(self):
    #     print("this is class 1 method 1")
    pass
class c2():
    def met_1(self):
        print("this is class 2 method 1")
class c3(c1,c2):
    # def met_1(self):
    #     print("this is class 3 method 1")
    pass
obj=c3()
obj.met_1()
