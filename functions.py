# def rajkumar():
#     print(100)
#     x="raj"
#     print(x)
#     print("hello",x)
# rajkumar()
# rajkumar()

# print("welcome to hyderabad")
# rajkumar()


# def fn_1():
#     print("hello world")

# for i in range(10):     # here default stsrt value is 0 
#     print("iteration no",i)
#     fn_1()

#empty functions or zero argumented functions
# x="100" # global variable because out of function
# def fn_2():   # zero argumented functions
#     a=100 # local variable because it is within the function
#     b=200
#     x="global"
#     c=a+b
#     print("c=",c)
#     print("a=",a)
#     print("b=",b)
#     print("x=",x)
# print("hello world")
# fn_2()
# fn_2()

# argumented function....required argumented functions
# m=str(input("enter the name:"))
# n="kumar"
# def fn_2(x,y):
#     a=x
#     b=y
#     print("a=",a)
#     print("b=",b)
#     print("n=",n)
# fn_2(10,20)
# fn_2(100,300)
# fn_2(y=30,x=38)
# fn_2(m,n)

# def fn_2(x=100,y=200):
#     a=x
#     b=x+y
#     print("a=",a)
#     print("b=",b)
# fn_2()
# # fn_2(10,20)
# fn_2(10)   # here we given only one value it will take as x value and y will be taken as default(200)


# # return keyword
# def fn_1(x,y):
#     print("This is raj kumar")
#     return x,y,x+y,x*y,"return function"
# print(fn_1(100,300))
# z=fn_1(10,20)
# print(z)

#orbitary arguments
# def fun_1(x,y,*z):
#     print(x)
#     print(y)
#     print(z)
# fun_1(10,20,30,40,50,60)

# #keyword arguments
# def fun_1(x,y,**z):
#     print(x)
#     print(y)
#     print(z)
# fun_1(10,20,name="rajkumar",age=25,branch="csm",course="btech")
x=0
b=int(input("enter the number:"))
for i in range(b):
    a=b*(b-1)
    x+=a   
    b-=1
print(x)
    
