# x=lambda n,a=1,b=2:a+b+n
# print(x(10))     #here 10 is taken as n value

# x=lambda a=10:print(a)  # print statement
# print(x())

# if else in lambda function
# y=lambda a,b:a+b if a<b else a-b
# print(y(10,20))
# print(y(5,2))

# y=[1,2,3,4,5]
# z=tuple(map(lambda a:a//2 if a%2==0 else a*2 ,y))
# print(z)
# z=tuple(map(lambda a:a<2,y))
# m=tuple(filter(lambda a:a<2,y)) # it will return true value(1)....filter(function, iterable)
# print(z,"map")
# print(m,"filter")

# from functools import reduce
# x=reduce(lambda a,b:a+b,[1,2,3,4])
# print(x)


