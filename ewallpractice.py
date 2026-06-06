# class classname():
#     x="hello codegnan"
#     def method1(self,a,b):
#         print("hello world")
#         print("price is",a)
#         return "discount",b
# c=classname()
# print(c.method1(1000,10)) 
# print(c.x)
# print(classname.x)


# def fun_1(a):
#     print("hello")
#     return a
# print(fun_1(10))




# class Student:
    
#     # class variable
#     school = "ABC School"

#     def __init__(self, name, age):
#         # instance variables
#         self.name = name
#         self.age = age


# # creating objects
# s1 = Student("Raj", 20)
# s2 = Student("Kumar", 21)

# # accessing variables
# print(s1.name, s1.age, s1.school)
# print(s2.name, s2.age, s2.school)



# class bankaccount():
#     def __init__(self):
#         self.__balance=0
#     def deposit(self,amount):
#         self.__balance+=amount
#     def show_balance(self):
#         return self.__balance
# b=bankaccount()
# b.deposit(1000)
# print(b.show_balance())
# print(b._bankaccount__balance)#name mangling


# #single inheritance
# class parent():
#     def met_1(self):
#         print("this is method 1")
# class child(parent):
#     def met_2(self):
#         print("this is method2")

# p=child()
# p.met_2()
# p.met_1()


# #multilevel inheritance
# class parent1():
#     def met_1(self):
#         print("this is method 1")
# class parent2():
#     def met_2(self):
#         print("this is method2")
# class child(parent1,parent2):
#     def met_3(self,a,b):
#         return a,b,a+b
# p=child()
# p.met_1()
# p.met_2()
# print(p.met_3(10,20))


# #multilevel inheritance
# class parent():
#     def met_1(self):
#         print("this is method1")
# class child(parent):
#     def met_2(self):
#         print("this is method2")
# class subchild(child):
#     def met_3(self):
#         print("this is method3")
# p=subchild()
# p.met_3()
# p.met_2()
# p.met_1()


# #hierachical inheritance
# class parent():
#     def met_1(self):
#         print("this is method1")
# class child(parent):
#     def met_2(self):
#         print("this is method2")
# class subchild(parent):
#     def met_3(self):
#         print("this is method3")
# p=subchild()
# p.met_3()
# p.met_1()
# d=child()
# d.met_2()
# d.met_1()


# a=list(map(int,input("enter the values:").split(",")))
# print(type(a))
# print(a)

# a=tuple(map(float,input("enter the tuple values").split(",")))
# print(type(a))
# print(a)


# a=set(map(int,input("enter the values:").split(",")))
# print(type(a))
# print(a)


# a=eval(input("enter mutiple data:"))
# print(a)


# a,b=input("enter the multiple names:").split(",")
# print("hello this is {1} and iam from {0}".format(a,b))


# a,b=input("enter the multiple names:").split(",")
# print(f"this is {a} and my village is {b}")

# a=100
# b=10.9
# c="rajkumar"
# print("a=%d,b=%f,c=%s" %(a,b,c))

# a=int(input("enter the number:"))
# while a<=50 and a>=1:
#     print(a)
#     a-=1


# #jumping statements
# for i in range(1,11):
#     if i==8:
#         continue
#     print(i)
# a="abcdzabcd"
# for i in a:
#     if i=="z":
#         print("this particular iteration skips",i)
#         continue
#     print(i)


# for i in range(5):
#     pass
# print("hello world")


# match case
# name=input("enter the name:")
# match name:
#     case "allu arjun":
#         print("icon star")
#     case "pawan kalyan":
#         print("power star")
#     case _:
#         print("the given name is",name)

# x="avcf"
# assert type(x) is not str,"the given value not string 12345" 


# for i in range(5):
#     print(i)

# x=lambda a,b=200,c=500:a+b+c
# print(x(10))

# y=lambda a=10:print(a)
# y()


# x=lambda a,b:a+b if a>b else a-b
# print(x(10,20))


# def fun_1(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fun_1(n-1)
# print(fun_1(5))

# --------------------

# class classname():
#     a="class variable"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def met_1(self):
#         print("this is met_1")
#         print(f"my name is {self.name} and my age is {self.age}")
# d=classname("raqjkumar",12)
# print(classname.a)
# print(d.a)
# d.met_1()
# print(d.name,d.age)


# class classname():
#     def __init__(self):
#         self.__balance=0
#     def deposit(self,amount):
#         self.__balance+=amount
#     def showbalance(self):
#         return self.__balance
# obj=classname()
# obj.deposit(100)
# print(obj.showbalance())


# class animal():
#     def sound(self):
#         print("this is animal sound")
# class human(animal):
#     def sound(self):
#         print("this is humans sound")
# h=human()
# h.sound()
# a=animal()
# a.sound()


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


from multipledispatch import dispatch
class classname():
    @dispatch()
    def met_1(self):
        print("this is met_1")
    @dispatch(str)
    def met_1(self,a):
        print(a)
    @dispatch(int,float)
    def met_1(self,a,b):
        print(a)
        print(b)
obj=classname()
obj.met_1()
obj.met_1("rajkumar")
obj.met_1(10,20.0)