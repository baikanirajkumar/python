
# def add(a,b):
#     c=a+b
#     return c
# print(add(5,6))

# # print(add(5,6))

# d=2
# # val=add(5,6)
# print(add(5,6)*d)



#functions with def keyword
#zero argumented functions
# def fun_1():
#     a=100
#     b="rajkumar"
#     c="btech"
#     print(a,"age")
#     print(b,"name")
#     print(c,"course")
# fun_1()


# #argumented functions
# #required arguments
# a=100
# b=90
# def fun_2(x,y):
#     z=x+y
#     print("hello world")
#     print(z)
# fun_2(30,40)
# fun_2(a,b)

# #default arguments
# def fun_3(x=100,y=300):
#     z=x+y
#     print(z)
#     print("hello codegnan")
# fun_3()
# fun_3("hello","world")
# fun_3(23,34)


# #orbitary arguments
# def fun_1(a,b,*x,c=100,d=400):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(x)
# fun_1(10,20,30,40)


#keyword argumented functions

# def fun_1(x,y,**kw):
#     print(x)
#     print(y)
#     print(kw)
# fun_1(10,20,name="rajkumar",age=20)


# #overall example
# def fun_1(a,b,*x,c="raj",**y):
#     a=10
#     b=20
#     print(a)
#     print(b)
#     print(x)
#     # print(c)
#     print(y)
# fun_1(10,20,30,40,50,name="rajkumar",age=40)



##lambda functions
# x=lambda x,y:x+y+10
# print(x(10,20))

# #lambda function with if else
# y=lambda a,b:a+b if a>b else a-b
# print(y(10,20))
# print(y(20,10))


# # # map function
# y=[1,2,4,5,6,7]
# # x=tuple(map(lambda a:a//2 if a%2==0 else a/2,y))
# # print(x)
# x=tuple(filter(lambda a:a<2,y))
# print(x)

# import functools
# x=functools.reduce(lambda a,b:a+b,[1,2,3,4])
# print(x)

# from functools import reduce
# x=reduce(lambda a,b:a+b,[1,2,3,4])
# print(x)



# import functools as fc
# x=fc.reduce(lambda a,b:a+b,[1,2,3,4])
# print(x)

# #call by value
# x=100
# def fun_1(b):
#      b*=2
#      print(b)
# fun_1(x)
# fun_1(200)


# x=[10,20,30.40]
# def fun_1(a):
#      a=a[::1]
#      b=a*2
#      print(b)
# fun_1(x)


# class classname():
#     game="kabaddi"
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def meth_1(self):
#         print(f"my name is {self.name} and my roll no is {self.rollno}")
#     def meth_2(self):
#         print("hello world")
# c1=classname("raj","24")
# c1.meth_1()

# class classname2():
#     def __init__(self,x,y,des):
#         classname.__init__(self,x,y)
#         self.x=x
#         self.y=y
#         self.des=des
#     def meth_3(self):
#         classname.meth_1(self)
#         print(f"hello codegnan, this is {self.x} and my age is {self.y} and my des is {self.des}")
#         classname.meth_2(self)
#     def meth_4(self):
#         print("i prefer IT job")
# c2=classname2("raj","25","software employee")
# c2.meth_3()
# c2.meth_4()


#daily exam coding question

# #print the greeting message
# a=str(input("enter the name:"))
# print("hello",a)

#take list as user input and print max element from the list
# a=list(map(int,input("enter the values:").split(",")))
# print(max(a))




# class c1_1():
#     a="class variable"
#     def __init__(self,a,b):
#         self.a="rajkumar"
#         self.b="btech"
#     def met_1(self):
#         print(f"this is {self.a} and my course is {self.b}")
#     def met_2(self):
#         self.met_1()
#         print("hello world")
#         print("hello codegnan")
# # c=c1_1("rajkumar","btech")
# # c.met_1()
# # c.met_2()

# class c2_2():
#     b="this is raj kumar"
#     def __init__(self,x,y,z):
#         c1_1.__init__(self,x,y)
#         self.x=x
#         self.y=y
#         self.z=z
#     def met_3(self):
#         c1_1.met_1(self)
#         print("this is method 3")
#         print(f"currently i ws taking coaching in {self.x} at {self.y} and my roll no is {self.z}")
#     def met_4(self):
#         print("this is method 4")
#     @classmethod
#     def fun_2(cls):
#         c2_2.b="this is chandu"
#         k="hello hyderabad"
#         return k
#     @classmethod
#     def fun_3(cls,name,age,rollno):
#         return cls(name,age,rollno)
#     @staticmethod
#     def fun_1(e):
#         print("this is function",e.x)
#         print(f"{e.x} and {e.y} ")
#     # fun_1()
# e=c2_2("codegnan","hyd","20")
# # e.met_3()
# # c2_2.fun_1()
# # e.fun_1(e)
# # print(e.fun_2())
# # print(e.fun_3())
# d=c2_2.fun_3("pawan",30,40)
# print(d.fun_3("pawan",30,40))


# #single inheritance
# class c1():
#     def met_1(self):
#         print("this is method 1")
#     def met_2(self,a,b):
#         return a,b,a+b
# # c10=c1()
# # c10.met_1()
# # print(c10.met_2(100,200))

# class c2(c1):
#     def met_3(self):
#         print("this is method 3")
#     def met_4(self,c,d):
#         return c,d,c+d
# c20=c2()
# # c20.met_3()
# # print(c20.met_4(20,30))
# # c20.met_1()
# # print(c20.met_2(10,20))

# #Multilevelinheritance
# class c3(c2):
#     def met_5(self):
#         print("this is method 5")
#     def met_6(self,e,f):
#         return e,f,e+f
# c30=c3()
# c30.met_5()
# print(c30.met_6(2,4))
# c30.met_1()
# print(c30.met_2(4,5))
# c30.met_3()
# print(c30.met_4(10,20))


# class a():
#     def met_7(self):
#         print("this is method 7 of class a")
#     def met_8(self):
#         print("this is method 8 of class a")
# class b():
#     def met_9(self):
#         print("this is method 9 of class b")
#     def met_10(self):
#         print("this is method 10 of class b")
# class c():
#     def met_11(self):
#         print("this is method 11 of class c")
#     def met_12(self):
#         print("this is method 12 of class c")
# class d(a,b,c):
#     def met_13(self):
#         print("this is method 13 of class d")
#     # def met_7(self):
#     #     print("this is method 7 of class d")
# obj=d()
# obj.met_13()
# obj.met_7()
# obj.met_7()
# obj.met_8()
# obj.met_9()
# obj.met_10()
# obj.met_11()
# obj.met_12()
# obj.met_13()

# #print the factorial of numbers
# def fun_1(n):
#     print("recursuion",n)
#     if n==0 and n==1:
#         return 1
#     else:
#         return n*fun_1(n-1)
# print(fun_1(5))


# #print the fibonacci series
# def fun_1(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fun_1(n-2)+fun_1(n-1)
# print(fun_1(10))

# def sum(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return n+sum(n-1)
# print(sum(5))    




# #single inheritance
# class parent():
#     def met_1(self):
#         print("met_1")
# class child(parent):
#     def met_2(self):
#         print("met_2")
# # c=child()
# # c.met_2()
# # c.met_1()

# #multiple inheitance
# class childchild(child):
#     def met_3(self):
#         print("met_3")
# d=childchild()
# d.met_3()
# d.met_2()
# d.met_1()


# #multiple inheritance
# class parent1():
#     def met_1(self):
#         print("met_1")
# class parent2():
#     def met_2(self):
#         print("met_2")
# class parent3():
#     def met_3(self):
#         print("met_3")
# class child(parent1,parent2,parent3):
#     def met_4(self):
#         print("met_4")
# e=child()
# e.met_1()
# e.met_2()
# e.met_3()
# e.met_4()

##hierarchical inheritance
# class parent():
#     def met_1(self):
#         print("met_1")
# class child1(parent):
#     def met_2(self):
#         print("met_2")
# class child2(parent):
#     def met_3(self):
#         print("met_3")
# class child3(parent):
#     def met_4(self):
#         print("met_4")
# a=child3()
# a.met_1()
# a.met_4()
# b=child2()
# b.met_1()
# b.met_3()
# c=child1()
# c.met_1()
# c.met_2()

#hybrid inheritance

# class grandfather():
#     def met_1(self):
#         print("met_1")
# class father(grandfather):
#     def met_2(self):
#         print("met_2")
# class child(grandfather):
#     def met_3(self):
#         print("met_3")
# class child2(father,child):
#     def met_4(self):
#         print("met_4")
# obj=child2()
# obj.met_4()
# obj.met_3()
# obj.met_2()
# obj.met_1()




# class Grandfather:
#     def met_1(self):
#         print("met_1")

# class Father(Grandfather):
#     def met_2(self):
#         print("met_2")

# class Child(Grandfather):
#     def met_3(self):
#         print("met_3")

# # Inherit from the subclasses (Father and Child) — not from Grandfather again
# class Child2(Father, Child):
#     def met_4(self):
#         print("met_4")

# # instantiate!
# obj = Child2()
# obj.met_4()   # from Child2
# obj.met_3()   # from Child
# obj.met_2()   # from Father
# obj.met_1()   # from Grandfather (inherited)


##method overloading
# from multipledispatch import dispatch
# class c_1():
#     @dispatch()
#     def met_1(self):
#         print("this is met_1")
#     @dispatch(int)
#     def met_1(self,a):
#         print("a:",a)
#         print("this is met_2")
#     @dispatch(int,float)
#     def met_1(self,a,b):
#         print("a:",a)
#         print("b:",b)
#         print("this is met_3")
# obj=c_1()
# obj.met_1(10,20.0)
# obj.met_1(12)
# obj.met_1()

# from multipledispatch import dispatch
# class c_1():
#     @dispatch()
#     def met_1(self):
#         print("this is met_1")
#     @dispatch(object)
#     def met_1(self,a):
#         print("a:",a)
#         print("this is met_2")
#     @dispatch(object,object)
#     def met_1(self,a,b):
#         print("a:",a)
#         print("b:",b)
#         print("this is met_3")
# obj=c_1()
# obj.met_1("raj","kumar")
# obj.met_1(12)
# obj.met_1()

# print(isinstance(obj,c_1))

# x=100
# print(isinstance(x,int))

# x="rajkumar"
# print(isinstance(x,str))

# x={"name":"rajkumar","rollno":14,"cousre":"Btech"}
# print(isinstance(x,dict))
# x={"name","rajkumar","name",13,12} #if we print the set it will return unique elements
# print(isinstance(x,set))
# print(x)

# class c_1():
#     def met_1(self,a,b):
#         if type(a) is int and type(b) is str:
#             print("a is int type of data and b is string type of data")
#         elif type(a) is float and type(b) is float:
#             print("a is float type of data and b is float type of data")
#         elif type(a) is str and type(b) is int:
#             print("a is str type of data and b is int type of data")
#         elif type(a) is str and type(b) is str:
#             print("a is str type of data and b is str type of data")
# obj=c_1()
# obj.met_1(10,"raj")
# obj.met_1(10.9,34.5)
# obj.met_1("rajkumar",23)
# obj.met_1("kumar","chandu")


# print("hello","warangal",sep="&",end="/")
# print("hello codegnan")

# #patterns
# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()


# for i in range(5):
#     for j in range(5):
#         if i==0 or j==0 or i==4 or j==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# a=1
# b=2
# c=3
# d=4
# for i in range(4):
#     for j in range(4):
#         if i==0:
#             print(a)
#             break
#         elif i==1:
#             print(a,b)
#             break
#         elif i==2:
#             print(a,b,c)
#             break
#         elif i==3:
#             print(a,b,c,d)
#             break
#         print()
# a=1
# b=2
# c=3
# d=4
# for i in range(4):
#     for j in range(4):
#         if i==0:
#             print("    ",a,"   ")
#             break
#         elif i==1:
#             print("  ",b," ",b,"  ")
#             break
#         elif i==2:
#             print(" ",c," ",c," ",c," ")
#             break
#         elif i==3:
#             print(d," ",d," ",d," ",d)
#             break
#     print()
        


# a=int(input("enter the number:"))
# b=2
# while b<=a//2:
#     if a%b==0:
#         print("it is not a prime number")
#         break
#     b+=1
# else:
#     print("it is prime number")

# a=int(input("enter the number:"))
# b=2
# c=a//2
# if b<=c:
#     if a%b==0:
#         print("it is not a prime number")
#     else:
#         print("it is prime number")
# else:
#     print("it is prime number")

# a=int(input("enter the number:"))
# if a in [2,3,5,7,11,13,17,19]:
#     print("it is prime number")
# else:
#     print("it is not prime number")


# #to check wheather it is leap year or not
# year=int(input("enter the number:"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("it is leap year")
# else:
#     print("it is not leap year")


# #method overriding
# class c_1():
#     # def met_1(self):
#     #     print("thid is method 1 of class 1")
#     pass
# class c_2():
#     def met_1(self):
#         print("this is method 1 of class 2")
# class c_3(c_1,c_2):
#     # def met_1(self):
#     #     print("this is method 1 of class 3")
#     pass
# obj=c_3()
# obj.met_1()

# #method overloading
# from multipledispatch import dispatch
# class c_1():
#     @dispatch()
#     def met_1(self):
#         print("hi")
#     @dispatch(object,object)
#     def met_1(self,a,b):
#         print("a:",a)
#         print("b:",b)
# obj=c_1()
# obj.met_1(10,20)
# obj.met_1()
# obj.met_1(23.34,34.56)

# import threading
# def fun_1():
#     print("this is rajkumar")
#     print("hello world")
#     print("hello codegnan")
# def fun_2():
#     a=10
#     b=20
#     c=a+b
#     print(c)
# def fun_3(c=100,d=200):
#     print(c+d)
# x=threading.Thread(target=fun_1)
# y=threading.Thread(target=fun_2)
# z=threading.Thread(target=fun_3)

# x.start()
# y.start()
# z.start()

# x.join()
# y.join()
# z.join()


# from abc import ABC,abstractmethod
# class c_1():
#     @abstractmethod
#     def met_1(self):
#         pass
#     @abstractmethod
#     def met_2(self):
#         pass
#     def met_3(self,a,b):
#         print("a",a)
#         print("b",b)
#         print("hi")
# class execution(c_1):
#     def met_1(self):
#         print("hello world")
# class execution2(execution):
#     def met_2(self):
#         print("hello codegnan")
# obj=execution2()
# obj.met_1()
# obj.met_2()
# obj.met_3(10,20)

# #check it is prime number or not under 20
# a=int(input("enter the number"))
# if a in [2,3,5,7,11,13,17,19]:
#     print("it is prime number")
# else:
#     print("it is not prime number")


# #print unique elements from the list
# a=[1,2,3,4,5,2,3,4,6,7]
# unique_list=[]
# for i in a:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)



# class c_1():
#     def met_1(self,a,b):
#         print("a:",a)
#         print("b:",b)
#         print("this is method 1 of class1")
# class c_2(c_1):
#     # def met_1(self,a,b):
#     #     print("a:",a)
#     #     print("b:",b)
#     #     print("this is method 1 of class 2")
#     pass
# obj=c_2()
# obj.met_1(10,20)

# from multipledispatch import dispatch
# class c_1():
#     @dispatch(object,object)
#     def met_1(self,a,b):
#         print("a:",a)
#         print("b:",b)
#         print(a+b)
#     @dispatch(object)
#     def met_1(self,c):
#         print("c:",c)
#         print("hello world")
# obj=c_1()
# obj.met_1(10)
# obj.met_1("rajkumar","chandu")




# c=0
# for i in range(1,10):
#     if i%2==0 and i<10:
#         c+=i
#         i+=1
#     else:
#         i+=1

# print(c)

# unique_list=[]
# for i in [1,2,3,42,3,4]:
#     if i in unique_list:
#         pass
#     else:
#         if i not in unique_list:
#             unique_list.append(i)
# print(unique_list)

# try:
#     x=int(input("enter the number:"))
#     print(x)
# except:
#     x=int(input("enter the number:"))
#     print(x)
# else:
#     print("this is else block")
# finally:
#     print("this is finally block")

# a={}
# print(type(a))
# # output:<class 'dict'>


# b=set()
# print(type(b))
# #output <class 'set'>

# c={"rajkumar",23,True,False}
# print(type(c))
# #output <class 'set'>

# d={"name":"rajkumar","rollno":14,"course":"Btech"}
# print(type(d))
# # output:<class 'dict'>


# class classname1():
#     x="hello world"
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def met_1(self):
#         print("this is method 1")
#     def met_2(self):
#         print("this is method 2")
#     def met_3(self):
#         self.met_1()
#         self.met_2()
#         print("this is method 3")
# # obj=classname1("chandu",35)
# # obj.met_1()
# # obj.met_2()
# # obj.met_3()
# # print(obj.x)
# # print(obj.y)

# class classname2():
#     a="hello codegnan"
#     def __init__(self,name,age,x,y):
#         classname1.__init__(self,x,y)
#         self.name=name
#         self.age=age
#     def met_4(self):
#         classname1.met_1(self)
#         print("this is method 4")
#         print("my name is",self.name)
#         print("my age is",self.age)
#     def met_5(self):
#         print("this is method 5")
# c1=classname2("vishnu",43,"rajkumar",34)
# c1.met_4()
# c1.met_5()
# c1.met_1()
# c1.met_2()



# for i in range(2,10,2):
#     print(i)


# for i in range(1,10,2):
#     print(i)



# class class1():
#     x="hello world"
#     def __init__(self,name,age,branch):
#         self.name=name
#         self.__age=age
#         self._branch=branch
#     def met_1(self):
#         print(f"my name is {self.name} and my age is {self.__age} and my branch is {self._branch}")
# obj=class1("rajkumar",24,"btech")
# # obj.met_1()
# # print(obj.name)
# # print(obj._branch)
# # print(obj.__age)
# class c_2():
#     def met_2(self):
#         print(f"my branch is {obj._branch} and my name is {obj.name} and my age is {obj._class1__age}")
# ob=c_2()
# ob.met_2()

# a="string"
# b=["rajkumar","ramesh",True,False,23.34,23]
# c=("rajkumar","rajkumar","ramesh",90,True,False)
# d={"happy","happy","birthday",True,True,False}
# e={"name":"rajkumar","rollno":"14","age":22,"course":"Btech"}
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# #arthimetic operators(+,-,*,/,//,%,**)
# a=100
# b=20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

# #assignment operators(=,+=,-=,*=,/=,//=,%=,**=) ..instead of taking third variable we can update easily
# a=10
# b=10
# a+=b #20
# a-=b #10
# a*=b #100
# a/=b #10
# a//=b #1.0
# a%=b  #1.0
# a**=b #1.0
# print(a)

#relational operators(==,!=,>,<,>=,<=)
# a=10
# b=20
# # print(a>b)
# # print(a<b)
# # print(a==b)
# # print(a!=b)
# # print(a>=b)
# # print(a<=b)
# print(ord("A"))
# print(chr(97))

#membership operators(in,not in)
# a="this is raj kumar"
# b="raj kumar"
# print(b in a) #true
# print(b not in a) #false
# a="rajkumar"
# b="rj"
# print(b in a) #false
# print(b not in a)  #True

# #identity operators(is,is not)
# a=10
# b=10
# print(a is b)
# print(a is not b)

#logical operators(and,or,not)
# a=100
# b=200
# c=300
# print(a>b and b>c)
# print(c>b or b>a)
# print(not a>b)


# #bitwise operators(&,|,^,~,<<,>>)
# a=10
# b=20
# print(a&b)
# print(a|b)
# print(a^b)
# print(~a)
# print(a<<b)
# print(a>>b)


# #typecasting
# #int to others
# a=10
# print(type(a))
# print(float(a))
# print(complex(a))
# print(bool(a))
# print(str(a))
# print(list(a))  
# print(tuple(a)) 
# print(set(a))
# print(dict(a))

# #float to others
# a=10.0
# print(type(a))
# print(int(a))
# print(complex(a))
# print(bool(a))
# print(str(a))
# print(list(a))  
# print(tuple(a)) 
# print(set(a))
# print(dict(a))

# #str to others
# a="rajkumar"
# print(type(a))
# # print(int(a))
# # print(complex(a))
# print(bool(a))
# # print(float(a))
# print(list(a))  
# print(tuple(a)) 
# print(set(a))
# # print(dict(a))

# #list to others
# a=["rajkumar","kumar",True,False]
# print(type(a))
# # print(int(a))
# # print(complex(a))
# print(bool(a))
# print(str(a))
# # print(float(a))  
# print(tuple(a)) 
# print(set(a))
# # print(dict(a))

# #tuple to others
# a=("raj","kumar",True,False,29)
# print(type(a))
# # print(int(a))
# # print(float(a))
# # print(complex(a))
# print(bool(a))
# print(str(a))
# print(list(a))  
# print(set(a))
# # print(dict(a))


#set to others
# a={"raj","kumar",True,False,34.5}
# print(type(a))
# # print(int(a))
# # print(float(a))
# # print(complex(a))
# print(bool(a))
# print(str(a))
# print(list(a))  
# print(tuple(a)) 
# # print(dict(a))

# #dict to others
# a={"name":"rajkumar","rollno":24,"branch":"csm"}
# print(type(a))
# # print(int(a))
# # print(float(a))
# # print(complex(a))
# print(bool(a))
# print(str(a))
# print(list(a))  
# print(tuple(a)) 
# print(set(a))

# #bool to others
# a=False
# print(type(a))
# print(int(a))
# print(complex(a))
# print(float(a))
# print(str(a))
# print(list(a))  
# print(tuple(a)) 
# print(set(a))
# print(dict(a))

# d=[("name","rajkumar"),("batch","14"),("subject","python")]
# print(dict(d))

a=list(map(int,input().split(",")))
b=[]
for i in a:
    for j in a:
        if i>j and i not in b:
            b.append(i)
print(b)
print(b[1])
       

