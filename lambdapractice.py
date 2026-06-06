# y=lambda a,b,c=30,d=20:a+b+c+d
# print(y(10,20))

# y=lambda a,b:a+b if a<b else a-b
# print(y(10,20))
# print(y(30,20))

# #map(),filter(),reduce() functions
# y=[1,2,3,4,5]
# z=tuple(map(lambda a:a//2 if a%2==0 else a*2 ,y))
# print(z)
# z=tuple(map(lambda a:a<2,y))
# m=tuple(filter(lambda a:a<2,y)) # it will return true value(1)
# print(z,"map")
# print(m,"filter")
# from functools import reduce
# a=reduce(lambda a,b:a+b,[1,3,3,4,6])
# print(a)

x={"name":"rajkumar","rollno":22,"branch":"csm"}
print(x.items())
y=dict(sorted(x.items(),key=lambda x:x[1],reverse=True))
print(y)
