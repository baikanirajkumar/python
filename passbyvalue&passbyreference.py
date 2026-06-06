#pass by value:changes made inside the function doesnot affect original variable
#pass by refernce: changes made inside the function affect the orginal variable


# #pass by value
# x=100
# def fun_1(a):
#     a*=2
#     print(a)
# fun_1(x)
# print(x)

# #own example 
# x=1000
# def fun_1(x):
#     x+=2
#     print(x)
# fun_1(x)
# print(x)

#passby reference
x=[10,20,30]
print("x",x)
def fun_1(a):
    # a=a.copy()
    a=a[::1]
    a*=2
    print("inner",a)
fun_1(x)
fun_1(["a","b","c"])
print("x",x)



# #own example
# x=(20,30,40)
# def fun_1(a):
#     a=a[::1]
#     a*=2
#     print(a)
# fun_1(x)
# print(x)
# fun_1((50,60,70))


# #not working on sets and dictionary
# x={"name":"rajkumar","rollno":24}
# def fun_1(a):
#     a=a.copy()
#     a*=2
#     print(a)
# fun_1(x)
# print(x)
# fun_1((40,50,60)


# #pass by value and pass by reference
a=10
print("a=",a)
def fun_1(x):
    x=100
    print("x=",x)
fun_1(a)
print(a)

#pass by refernce
a=[10,20,30]
def fun_1(x):
    x*=2
    print("inner",x)
fun_1(a)
print("outer",a)

#pass by value:int,float,string,tuple
#pass by reference:list,set,tuple

#pass by value
x=100
def fun_1(a):
    a*=2
    print(a)
fun_1(x)
print(x)

#pass by value
x=(10,20,30,40)
def fun_1(a):
    a*=2
    print("inner:",a)
fun_1(x)
print("outer:",x)

#pass by value
x="rajkumar"
def fun_1(a):
    a*=2
    print("inner:",a)
fun_1(x)
print("outer:",x)


#pass by value
x=10.9
def fun_1(x):
    x*=2
    print("inner:",x)
fun_1(x)
print("outer:",x)


#pass by reference:list
a=[1,2,3,4]
def fun_1(a):
    a*=2
    print("inner:",a)
fun_1(a)
print("outer:",a)


# #pass by reference:set
# a={1,2,3,4}
# def fun_1(a):
#     a.add(10)
#     print("inner:",a)
# fun_1(a)
# print("outer:",a)


# #pass by reference:dictionary
# a={"name":"rajkumar","age":24,"college":"jits"}
# def fun_1(a):
#     a["name"]="kiran"
#     print("inner:",a)
# fun_1(a)
# print("outer:",a)

