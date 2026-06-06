a={"name":"rajkumar","rollno":14}
# a["rollno"]=12
# print(a)
# a.setdefault("name","mnbvc")   #if it have the key it doesnot take doesnot have it will be taken
# print(a)
# a.setdefault("classname","mnbvc")   # this item is not present in above so it will be added
# print(a)
# print(a.pop("name"))     # pop the specific key
# print(a)
# print(a.popitem())   #item will be poped
# print(a)

# del a["name"]    #del the specific key
# print(a)


# print(a.get("name","ssss")) #if the key is present in a it will return the value if not return the default value("ssss")
# print(a.keys())
# print(a.values())
# print(a.items())

# a={"name":"rajkumar","age":"thirty"}
# b={"name":"ramesh","age":25}
# print(a.update(b))
# print(a)

# print(sorted(a,reverse=True))
# print(a)
# print(max(a))   #compare with keys and return max key 
# print(max(a,key=a.get))  #compare with values and return max key
# print(a)
# print(min(a,key=a.get)) ##compare with values and return min key

# #dictionary coding exam  here print the most repeated value in the dictionary
# a = {1:20, 2:20, 3:30, 4:10}
# b = a.values()
# c = max(b, key = list(b).count)
# print(c)

# a=64
# b=round((a)**(1/3))
# c=b*b*b
# if a==c:
#     print("it is perfect cube")

# a=4
# b=(a)**(1/2)
# c=b*b
# if a==c:
#     print("it is perfect square")


# a=10
# b=20
# c=a%b
# print(c)
# d=a/b
# e=a//b
# print(d)
# print(e)

# a=90
# a+=10
# print(a)
# a=2
# b=2**3
# print(b)


# a=10
# b=20
# c=30
# d=40
# e=50
# f=60
# g=70
# a+=10
# b-=10
# c*=10
# d/=10
# e%=10
# f//=10
# h=g**10
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(h)


# a=10
# b=20
# c=a==b
# d=a!=b
# e=a>b
# f=a<b
# g=a>=b
# h=a<=b
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)

# print(ord("z"))
# print(chr(97))

# a="hello"
# b="hl"
# print(b in a)
# print(b not in a)

# x = [1, 2, 3]
# y = x
# z = [1, 2, 3]

# print(x is y)       # True — both refer to the same object
# print(x is z)       # False — different objects with same values
# print(x is not z)   # True — x and z are not the same object


# a=100
# b=200
# c=900
# print(a>b or c>b and c>a)
# print(c>a and c>b and c>a)
# print(not a>b) #here actually the condition is false(100>900) but we use not operator so it return True
# print( not True)
# print(not 0)

# print(ord("h"))
# print(ord("i"))
# print(ord("A"))


# a=10
# b=20
# print(a&b)
# print(a|b)
# print(~a)
# print(a^b)
# print(a<<2)
# print(a>>2)

