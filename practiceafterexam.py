# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=a+b
# print(c)

# a=int(input("enter the number"))
# if a>0:
#     print(f"{a} is positive number")
# else:
#     print(f"{a} is not positive number")

# #check if the given string is empty or not
# a=str(input("enter the string"))
# if len(a)==0:
#     print("the string is empty")
# else:
#     print("the given string is not empty")


# a=str(input("enter the string:"))
# if a=="":
#     print("the string is empty")
# else:
#     print("the string is not empty")

# a=str(input("enter the string"))
# if not a:
#     print("empty")
# else:
#     print(a)

# a=int(input("enter the number:"))
# if a>0:
#     print("the number is positive")
# elif a<0:
#     print("the number is negative number")
# else:
#     print("the number is zero")


# a=int(input("enter the number:"))
# if a%3==0 and a%5==0:
#     print(f"{a} is multiple of both 3 and 5")


# a=int(input("enter the number:"))
# a1=(a)**(1/2)
# a2=a1*a1
# if a==a2:
#     print("it is perfect square")
# else:
#     print("it is not perfect square")


# #end parameter and seperator parameter
# print("rajkumar baikani",end="&")
# print("codegnan",end="&")
# print("hyderabad")

# print("rajkumar","baikani","from","kondaparthy",sep="/")

# x="this"
# y="is"
# z="rajkumar"
# print(x,y,z,sep="/")


# #python input functions
# a=int(input("enter the value:"))
# b=int(input("enter the value:"))
# b=float(b)
# c=a+b
# print(c)
# print(type(c))


# a,b=input("enter the mutiple valuees").split("and")
# print(a)
# print(b)

# a=input("enter multiple values:").split("and")
# print(a)

# a=list(map(int,input("enter the values:").split(",")))
# print(a)
# b=tuple(map(int,input("enter the mutiple values:").split(",")))
# print(b)
# c=set(map(int,input("enter multiple values").split(",")))
# print(c)

# #creating dictionary using evalutionary function
# a=eval(input("enter data:"))
# print(a)

# #python output formatting
# a,b=input("enter the names").split(",")
# print(a)
# print(b)


# #longest word in string
# a="this is python"
# b=a[0:4:1]
# c=a[5:7:1]
# d=a[8:13:1]
# e=len(b)
# f=len(c)
# g=len(d)
# if e>f and e>g:
#     print("this")
# elif f>e and f>g:
#     print("is")
# else:
#     print("python")


# #check palindrome
# a=str(input("enter the string"))
# b=a[::-1]
# if a==b:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

# #reverse each word in string
# a="this is rajkumar"
# b=a[0:4:1]
# b1=b[::-1]
# c=a[5:7:1]
# c1=c[::-1]
# d=a[8:17:1]
# d1=d[::-1]
# print(b1)
# print(c1)
# print(d1)

# #count number of words in sentence
# a="rajkumar"
# print(len(a))

# #count character frequency
# a=["a","b","c","d","a","c","d","e"]
# print(a.count("a"))
# print(a.count("b"))


# #python output formatting
# a,b=input("enter the names:").split(",")
# print("hello {} Your rollno is {}".format(a,b))
# a,b=input("enter the names:").split(",")
# print("hello {1} your roll no is {0}".format(a,b))


# # another method for python output formatting
# a="rajkumar"
# b="14"
# print(f"my name is {a} and my roll no is {b}")

#python output formatting using modulary operator
# a=100
# b=190.8
# c='rajkumar'
# print("a=%d,b=%f,c=%s"%(a,b,c))


# #looping
# x=int(input("enter the number:"))
# while x<50 and x>=1:
#     print(x)
#     x-=1
# print("end of loop")

# x=int(input("enter the number"))
# for i in range(x):
#     print(x)
#     x-=1

# a=int(input("enter the number:"))
# if a%2==0:
#     a+=2
#     print(f"the a value is {a}")
# else:
#     print("enter the even number")

# a=["raj","kumar","raj","chandu"]
# b=0
# count=0
# while b<len(a):
#     if a[b]=="raj":
#         count+=1
#         if count==2:
#             print(b)
#     b+=1

# a="rajkumar"
# b=0
# c=len(a)
# d=[]
# while b<c:
#     if a[b]=="r":
#         d.append("*")
#         b+=1
#     else:
#         d.append(a[b])
#         b+=1
# print(d.strip())


# #program to print the table
# a=1
# for i in range(1,11,1):
#     print(a,"*",i,"=",a*i)
#     i+=1


# a=1
# b=1
# c=11
# while a<c and b<=10:
#     print(a,"*",b,"=",a*b)
#     b+=1 

# for i in range(5):
#     pass

# a="rajkumar"
# for i in a:
#     if i=="j":
#         print('the loop jumps here')
#         continue
#     print(i)


#assert keyword
# a="rajkumar"
# assert type(a) is not str
# for i in a:
#     if i=="a":
#         print("*",end="")
#         continue
#     print(i,end="")


#list functions
# a=[1,23,"a","apple",True,False]
# b=a.pop(1)
# print(a)
# print(a.pop(1))
# print(a)
# a.remove("apple")
# print(a)
# a.extend(["banana","mango"])
# print(a)
# a.append(["e","f"])
# print(a)
# a.insert(4,"z")
# print(a)
# del a[2]
# print(a)
# del a
# print(a)
# a.clear()
# print(a)

# a=["a","b","c","d","e"]
# b=a[1:4:2]
# print(b)
# c=a[:5:1]
# print(c)
# d=a[0::1]
# print(d)
# e=a[0:5:]
# print(e)
# f=a[::2]
# print(f)
# g=a[::-1]
# print(g)
# f=a[::-2]
# print(f)

# a=["a","b","c","d","e"]
# del a[0:3:1]
# print(a)

# a=["a","b","c","d"]
# a[2]="b"
# print(a)

# #copy functions
# a=["a","b",'c',"d","e","b"]
# b=a.copy()
# print(id(a))
# print(id(b))
# print(a.index("b"))
# c=a.index("b")
# print(c)
# print(a.count("b"))
# print(max(a))
# print(min(a))
# a=[1,2,3,4,5,6]
# print(max(a))
# print(min(a))

# a=[1,2,3,45,33]
# print(sum(a))


# a=["a","b","c"]
# b=list(enumerate(a))
# print(b)
# c=tuple(enumerate(a))
# print(c)

# a=[("name","rajkumar"),("rollno",14)]
# b=dict(a)
# print(b)

# x=["a","b","c"]
# x.reverse()
# print(x)

# a=[1,5,2,5,6,2,5,8]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# print(sorted(a))
# print(a)
# b=sorted(a)
# print(b)
# print(a)
# print(len(a))
# print(any(a))
# print(all(a))

# #empty functions or 0 argumented functions
# def fun_1():
#     a=100
#     b=200
#     c=a+b
#     print(c)
# fun_1()


# #argumented functions(required argumented functions)
# a="rajkumar"
# b="baikani"
# def fun(x,y):
#     a1=x
#     a2=a1+y
#     print("a=",a)
#     print("b=",b)
#     print(a+b)
#     print(a2)
# fun(10,20)
# fun(20,40)

# #default argumented functions
# a="rajkumar baiknai"
# def fun_1(x,y,a=100,b=200):
#     c=a+b+x+y
#     print(c)
# fun_1(200,300)

# def fun_1(*x):
#     print(x)
# fun_1(10,20,30,40,50)
# fun_1(10)
# fun_1()

# def fun_1(a,b,c="raj",d="kumar",*e):
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
#     print("d=",d)
#     print("e=",e)
# fun_1(10,20,30,40,50,60,39)


# def fun_1(**x):
#     print(x)
# fun_1(name="raju",age=24,rollno=14)

# def fun_1(a,b,*c,**d):
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
#     print("d=",d)
# fun_1(10,20,30,40,50,name="rajkumar",rollno=14)

# #return statement
# def fun_1(x=10,y=20):
#     print("this is return statement example")
#     return x+y,x-y,x/y
# print(fun_1())
# a=fun_1()
# print(a)

# def fun_1(x,y):
#     a=x+y
#     print('a=',a)
#     print("x=",x)
#     print("y=",y)
# fun_1(10,20)


# a=lambda a,b:a+b
# print(a(10,20))
# x=lambda a,b:a+b if a>b else a-b
# print(x(10,20))
# a=list(map(int,input("enter multiple values").split("/")))
# print(a)
# print(type(a))


# y=(10,20,30,40)
# x=tuple(map(lambda a:a//2 if a%2==0 else a*2,y))
# print(x)
# print(type(x))

# y=[10,20,30,40]
# x=[1,2,3,4]
# a=list(map(lambda a,b:a+b if a>b else a-b,y,x))
# print(a)
# print(type(a))

# #pass by value and pass by reference
# a=10
# a=10.8
#a="rajkumar"
# a=(10,20,30,40)
# a={10,20,30}
# a={"name":"rajkumar","rollno":14}
# print("a=",a)
# def fun_1(x):
#     x=100
#     print("x=",x)
# fun_1(a)
# print(a)

# #pass by refernce
# a=[10,20,30]
# a={10,20,30}
# # a={"name":"rajkumar","rollno":14,"branch":"csm"}
# def fun_1(x):
#     # x[0]=12
#     x.add(2)
#     print("inner",x)
# fun_1(a)
# print("outer",a)

# #genarators 
# def fun_1():
#     print("hello")
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     print("end")
# b=fun_1()
# for i in b:
#     print(i)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))


# import modules 
# modules.fun_1(10,20)

# import modules as mno
# mno.fun_1(10,20)
 
# from modules import fun_1
# fun_1(20,20)

# from modules import *
# fun_1(30,30)

#built in modules
# import math
# print(math.pi)
# print(math.e)
# print(math.exp(5))
# print(math.fabs(-10))
# print(math.sqrt(16))
# print(math.copysign(10,-29))
# print(math.ceil(10.001))
# print(math.floor(10.002))
# print(math.radians(5))
# print(math.degrees(10))
# print(math.fsum([10,20,30]))
# print(math.factorial(5))
# print(math.fmod(10,3))
# print(math.pow(2,3))
# print(math.hypot(10,20))
# print(math.log2(5))
# print(math.log10(4))
# print(math.log(5,4))
# x=10
# print(math.tan(x))
# print(math.cos(x/2))
# print(math.sin(x))
# print(math.radians(60))
# print(math.degrees(1))


# #platform module
# import platform
# print(platform.system())
# print(platform.version())
# print(platform.release())
# print(platform.processor())

# import itertools
# x=list(itertools.combinations("abcd",2))
# print(x)
# y=list(itertools.permutations("abcd",2))
# print(y)

# import sys
# print(sys.argv)
# print(sys.version)
# print(sys.version_info)
# print(sys.path)
# sys.exit()
# print("hello world")

# x="yugendra sai"
# for i in x:
#     if i=="a":
#         print("*",end="")
#         continue
#     else:
#         print(i,end="")

# from random import *
# # print(random())
# # print(randint(1,10))
# b=randint(1000,2000)
# print(b)
# a=int(input("enter the otp:"))
# if a==b:
#     print("the otp is matched successfully")
# else:
# #     print("the otp is not correct,please enter the correct otp")
# print(randrange(1,10,3))

# class classname():
#     x="class variable"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def met_1(self):
#         return f"this is first method,my name is {self.name}"
#     def met_2(self):
#         return f"this is second method,my age is {self.age}"
# c1=classname("rajkumar",23)
# print(c1.met_1())
# print(c1.met_2())


# #method overloading
# from multipledispatch import dispatch 
# class cl_1():
#     a="this is class variable"
#     def __init__(self):
#         self.a="rajkumar"
#         self.b="baikani"
#     @dispatch(int)
#     def met_1(self,x):
#         print("this is method 1")
#         print("x=",x)
#     @dispatch(int,str)
#     def met_1(self,x,y):
#         print("this is method 2")
#         print("x=",x)
#         print("y=",y) 
#     @dispatch(int,int,float)   
#     def met_1(self,x,y,z):
#         print("this is method 3")
#         print("x=",x)
#         print("y=",y)
#         print("z=",z)
# c1=cl_1()
# c1.met_1(10)
# c1.met_1(10,"codegnan")
# c1.met_1(10,20,30.9)


# from multipledispatch import dispatch 
# class cl_1():
#     a="this is class variable"
#     def __init__(self):
#         self.a="rajkumar"
#         self.b="baikani"
#     @dispatch(object)
#     def met_1(self,x):
#         print("this is method 1")
#         print("x=",x)
#     @dispatch(object,object)
#     def met_1(self,x,y):
#         print("this is method 2")
#         print("x=",x)
#         print("y=",y) 
#     @dispatch(object,object,object)   
#     def met_1(self,x,y,z):
#         print("this is method 3")
#         print("x=",x)
#         print("y=",y)
#         print("z=",z)
# c1=cl_1()
# c1.met_1(10)
# c1.met_1(10,10)
# c1.met_1(10,20,30)

# #methos overriding
# class c_1():
#     # def met_1(self):
#     #     print("this is c_1 method")
#     pass
# class c_2():
#     def met_1(self):
#         print("this is c_2 method")
# class c_3(c_1,c_2):
#     # def met_1(self):
#     #     print("this is c_3 method")
#     pass
# obj=c_3()
# obj.met_1()
# print(c_3.mro())

#exam answer for pfs-45 batch
# a=int(input("enter the number of ages:"))
# total=0
# for i in range(a):
#     age=int(input("enetr the ages"))
#     if age<5:
#         total+=0
#     elif age>5 and age<18:
#         total+=100
#     elif age>19 and age<60:
#         total+=150
#     else:
#         total+=120
# print("total movie ticket price =",total)


# a=float(input("enter the amount:"))
# tax=0
# if a<=250000:
#     tax+=0
# elif a>250001 or a<500000:
#     tax+=a*0.05
# elif a>500001 or a<1000000:
#     tax+=a*0.2
# elif a>1000000:
#     tax+=a*0.3
# print(tax)


# class classname():
#     x="rajkumar"
#     y="baikani"
#     def met_1(self):
#         print("this is method 1")
#         print(classname.x)
#     def met_2(self):
#         print("this is method 2")
#         print(classname.y)
#         return classname.x,classname.y
# obj=classname()
# obj.met_1()
# print(obj.met_2())

# def fun_1():
#     a=100
#     b=200
#     c=a+b
#     print(c)
# fun_1()

# def fun_2(x,y):
#     x+=10
#     y+=20
#     z=x+y
#     print(z)
# fun_2(10,20)

# def fun_3(x=10,y=30):
#     z=x+y
#     print(z)
# fun_3(60)

# #pass by value
# x=100
# def fun_1(a):
#     a*=2
#     print(a)
# fun_1(x)
# print(x)

# #pass by value
# x=(10,20,30,40)
# def fun_1(a):
#     a*=2
#     print("inner:",a)
# fun_1(x)
# print("outer:",x)

# #pass by value
# x="rajkumar"
# def fun_1(a):
#     a*=2
#     print("inner:",a)
# fun_1(x)
# print("outer:",x)


# #pass by value
# x=10.9
# def fun_1(x):
#     x*=2
#     print("inner:",x)
# fun_1(x)
# print("outer:",x)


# #pass by reference
# a=[1,2,3,4]
# def fun_1(a):
#     a*=2
#     print("inner:",a)
# fun_1(a)
# print("outer:",a)


# #pass by reference
# a={1,2,3,4}
# def fun_1(a):
#     a.add(10)
#     print("inner:",a)
# fun_1(a)
# print("outer:",a)


# #pass by reference
# a={"name":"rajkumar","age":24,"college":"jits"}
# def fun_1(a):
#     a["name"]="kiran"
#     print("inner:",a)
# fun_1(a)
# print("outer:",a)

#generators
def fun_1():
    print("start")
    yield "rajkumar"
    yield "chandu"
    yield "kiran"
    yield "kamal"
    yield "kishore"
# c=fun_1()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# a=1
# b=0
# c=[1,2,3,4,5,6,7,8,10]
# for i in c:
#     if c[b]==a:
#         a+=1
#         b+=1
#     else:
#         print(a)


# a=[1,2,3,4,5,6,7,8,10]
# n=10
# c=n*(n+1)//2
# d=sum(a)
# e=c-d
# print(e)


# a=[1,2,3,4,5,6,7,9]
# b=0
# c=1
# for i in a:
#     if a[b]==c:
#         b+=1
#         c+=1
#     else:
#         print(c)

# a=[1,2,3,4,5,6,7,8,10]
# b=sum(a)
# c=10*(11)/2  #(formula:n*(n+1)/2)
# d=c-b
# print(d)


