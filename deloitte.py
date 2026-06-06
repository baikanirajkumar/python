# class c1():
#     school="abc school"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def met_1(self,a,b):
#         print("my name is",self.name)
#         print(a+b)
#     def met_2(self):
#         print("my school name is",c1.school)
# obj=c1("rajkumar",20)
# obj.met_1(10,20)
# obj.met_2()
# print(obj.name,obj.age,obj.school)
# print(isinstance(obj,c1))

# class c1():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def met_1(self):
#         print("this is",self.name)
#         print("my age is",self.age)
#         print(f"my name is {self.name},and my age is {self.age}")
# obj=c1("rajkumar",20)
# obj.met_1()


# class c1():
#     school="abc school"
#     @classmethod
#     def met_1(cls):
#         print("this is",cls.school)
# obj=c1()
# obj.met_1()
# c1.met_1()

# class c1():
#     @staticmethod
#     def met_1(a,b):
#         print("add",a+b)
# c1.met_1(10,20)



# class c1():
#     def met_1(self):
#         print("this is method1")
# class c2(c1):
#     def met_2(self,a,b):
#         print("this is method 2")
#         return a+b
# obj=c2()
# print(obj.met_2(10,20))
# obj.met_1()

# class c1():
#     def met_1(self):
#         print("this is method1")
# class c2():
#     def met_2(self,a,b):
#         print("this is method 2")
#         return a+b
# class c3(c1,c2):
#     def met_3(self):
#         print("this is method 3")
# obj=c3()
# print(obj.met_2(2,2))
# obj.met_3()
# obj.met_1()
# # print(obj.met_2(10,2))
# print(c3.mro())
# print(c3.__mro__)



# class c1():
#     def met_1(self):
#         print("this is method1")
# class c2(c1):
#     def met_2(self,a,b):
#         print("this is method 2")
#         return a+b
# class c3(c2):
#     def met_3(self):
#         print("this is method 3")
# obj=c3()
# obj.met_3()
# print(obj.met_2(2,2))
# obj.met_1()



# class c1():
#     def met_1(self):
#         print("this is method1")
# class c2():
#     def met_1(self):
#         print("this is method 2")
# obj=c1()
# obj.met_1()
# obj1=c2()
# obj1.met_1()


# from abc import ABC,abstractmethod
# class c1(ABC):
#     @abstractmethod
#     def met_1(self):
#         pass
# class c2(c1):
#     def met_1(self):
#         print("this is method 2")
# obj=c2()
# obj.met_1()



# class c1():
#     def __init__(self):
#         self.__balance=0
#     def deposit(self,amount):
#         self.__balance+=amount
#     def show_balance(self):
#         return self.__balance
# obj=c1()
# obj.deposit(1000)
# print(obj.show_balance())


# class c1():
#     def __init__(self,name,age,rollno):
#         self.name=name
#         self._age=age
#         self.__rollno=rollno
# obj=c1("rajkumar",20,1)
# print(obj.name,obj._age)
# print(obj._c1__rollno)


# class parent():
#     def __init__(self):
#         print("parent constructor")
#     def met_1(self):
#         print("this method1")
# class child(parent):
#     def __init__(self):
#         print("this is child constructor")
#         super().__init__()
#     def met_2(self):
#         print("this is method2")
#         super().met_1()
# c=child()
# c.met_2()



# from multipledispatch import dispatch
# class c1():
#     @dispatch()
#     def met_1(self):
#         print("this is method1")
#     @dispatch(int)
#     def met_1(self,a):
#         print(a)
#     @dispatch(int,float)
#     def met_1(self,a,b):
#         print(a)
#         print(b)
# obj=c1()
# obj.met_1()
# obj.met_1(10)
# obj.met_1(10,23.3)


# print("hello world",end="")
# print("hello hyd","happy homes","hyderanad",sep="/")

# a=input("enter the string:")
# print(a,20)

# b=input("enter the numbers").split(",")
# print(b)

# a=list(map(int,input("enter the numbers:").split(",")))
# print(a)

# a=eval(input("enter data:"))
# print(a)

# a="rajkumar"
# b="ramu"
# print(f"this is {a} and my friend {b}")


# a=100
# b="raj"
# c=10.8
# print("a=%d,b=%s,c=%f" %(a,b,c))


# a=10
# b=29
# print("number1 is {} and num2 is {}".format(a,b))

# a=int(input("enter the number:"))
# if a>10:
#     print(f"{a} is greater than 10")
# elif a<10:
#     print(f"{a} is less than 10")


# a=int(input("enter the number:"))
# if a>10:
#     if a%2==0:
#         print(f"{a} is gretaer than 10 and even number")
#     else:
#         print("odd number but greater than 10")
# elif a<10:
#     if a%2==0:
#         print(f"{a} is less than 10 and even number")
#     else:
#         print("odd number but less than 10")

# for i in range(1,11):
#     print(i)

# a=1
# while a<=10:
#     print(a)
#     a+=1



# a=int(input("enter the number:"))
# if a%2==0:
#     print("even")
# else:
#     print("odd")

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# if a>b:
#     print(f"{a} is largest")
# else:
#     print(f"{b} is largest")


# a=int(input("enter the number:"))
# if a<=1:
#     print("it is not prime number")
# else:
#     for i in range(2,a):
#         if a%i==0:
#             print("it is not aprime number")
#             break
#     else:
#         print("it is a prime number")


# a=input("enter the string:")
# b=a[::-1]
# print(b)

# a=input("enter the string")
# b=a[::-1]
# if a==b:
#     print("it is palindrome")
# else:
#     print("it is not plaindrome")

# a=int(input("enter the number:"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# x=int(input("enter thye number:"))
# a=0
# b=1
# print(a,end=" ")
# print(b,end=" ")
# for i in range(x-2):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c

# n=int(input())

# a=0
# b=1

# for i in range(n):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c

# a=list(map(int,input("enter the list:").split(",")))
# print(max(a))

# a=input("enter the string:")
# count=0
# for i in a:
#     if i in "aeiouAEIOU":
#         count+=1
# print(count)

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# a,b=b,a
# print(a)
# print(b)

# a=[1,1,2,3,4,2]
# print(list(set(a)))

# a=input()
# sum=0
# for i in a:
#     sum=sum+int(i)
# print(sum)

# a=int(input())
# temp=a
# sum=0
# count=0
# for i in str(a):
#     count+=1
# while a>0:
#     rem=a%10
#     sum=sum+rem**count
#     a=a//10
# if temp==sum:
#     print("armstrong number")
# else:
#     print("not armstrong number")


# a=int(input())
# count=0
# while a>0:
#     a=a//10


# a=input("enter the number:")
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev=rev+a[i]
# print(rev)

#sort the list
# a=[1,5,2,4]
# a.sort()
# print(a)

# a=input()
# sum=0
# for i in a:
#     sum=sum+int(i)
# print(sum)

# a=int(input("enter the number:"))
# b=a**(1/2)
# c=b*b
# if a==c:
#     print("perfect square")
# else:
#     print("not perfect square")


# x=lambda n,e=100,f=20:n+e+f
# print(x)

# def fun_1(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fun_1(n-1)
# print(fun_1(5))

# a=[1,2,3,4]
# def fun_1(a):
#     a*=2
#     print("inner:",a)
# fun_1(a)
# print("outer:",a)


a=[1,2,3]
a.append([5,3])
print(a)
a.extend([3,3])
print(a)