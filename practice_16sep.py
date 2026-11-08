a=lambda x:x*x
print(a(5))

a=lambda x,y:x if x>y else y
print(a(10,20))

even_odd=lambda x:"even" if x%2==0 else "odd"
print(even_odd(10))


numbers=[1,2,3,4]
a=list(map(lambda x:x*x,numbers))
print(a)

names=["rajkumar","rajesh"]
upper_names=list(map(lambda x:x.upper(),names))
print(upper_names)


a=[1,2,3]
b=[4,5,6]
x=list(map(lambda x,y:x+y,a,b))
print(x)

numbers=[1,2,3]
filtered=list(filter(lambda x:x>1,numbers))
print(filtered)

names=["ramesh","kunal"]
filtered=list(filter(lambda x:x.startswith("r"),names))
print(filtered)


numbers=[1,2,3]
filtered=list(filter(lambda x:x%2==0,numbers))
print(filtered)