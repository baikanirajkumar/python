# import math
# x=1
# print(math.pi)
# print(math.e)
# print(math.exp(5))
# print(math.copysign(10,20))
# print(math.fsum([10,20,30,40]))
# print(math.fmod(12,3))
# print(math.fabs(-10))
# print(math.factorial(5))
# print(math.sqrt(16))
# print(math.pow(2,3))
# print(math.floor(10.9))
# print(math.ceil(10.9))
# print(math.hypot(10,20))
# print(math.log(5,2))
# print(math.log2(5))
# print(math.log10(5))
# print(math.tan(x))
# print(math.cos(x/2))
# print(math.sin(x))
# print(math.degrees(1))    #converts radians to degrees...One radian is approximately 57.3 degrees.
# print(math.radians(1))    #converts degrees to radians...

# instead of writing all these code we are using fabs function
# a="-10"
# b=a[1::]
# print(b)
# y=[1,2,3,5]
# x=tuple(filter(lambda a:a<2,y))
# print(x)



# import platform 
# print(platform.system())
# print(platform.processor())
# print(platform.version())
# print(platform.release())


# #combinations contain only unique elements
# import itertools
# x=list(itertools.combinations("abcd",2))
# print(x)

#permutations contain only duplicate elements
# y=set(itertools.permutations("abcd",2))
# print(y)

import sys
print(sys.argv)
print(sys.version)
print(sys.version_info)
print(sys.path)
print("hello world")
print("hello codegnan")
sys.exit()
print("hello world")
print("hello codegnan")

# from random import *
# print(randint(10,20))
# print(randrange(1,10,3))
# print(random()) # it will return floating point between 0 and 1

# x=randint(1000,9999)
# print(x)

# y=int(input("enter the otp:"))
# if x==y:
#     print("OTP is valid")
# else:
#     print("OTP is not valid")


# import random
# print(random.uniform(1,10))  # return float value from 1 to 10
# x=["a","b","c","d"]
# print(random.choice(x)) #return single element from list
# print(random.choices(x,k=2)) #return multiple elements from list
# print("before shuffle",x)
# random.shuffle(x)
# print("after shuffle",x)



# import random
# random.seed(1)
# x=[1,2,3,4,5]
# dice=random.choices(x,k=2)
# output=sum(dice)
# if output>7:
#     print(dice)
#     print("+7 you won the game")
# elif output<7:
#     print(dice)
#     print("-7 you won the game")
# elif output==7:
#     print(dice)
#     print("7 you won the game")

# #converting python script to json script
# import json
# x=[10,20,30,40]
# print(x,type(x),x[1])
# y=json.dumps(x)
# print(y,type(y),y[1])


# z=json.loads(y)
# print(z,type(z),z[1])

# import json
# with open("asdfg.json","w") as xyz:
#     json.dump(x,xyz)

# with open("asdfg.json") as abc:
#     g=json.load(abc)
# print("load function",g)


# import collections
# x=[10,20,30,40,50,60]
# y=collections.deque(x)
# print(y)

# x.append(100)
# print(x)

# y.extend(("a","b","c"))
# y.extendleft(("a","b","c"))
# print(y)
# print(y[2])
# y.pop()  # it is used to remove first element and last element
# print(y)
# y.popleft()
# print(y)

# y.rotate(-3) #deque([40, 50, 60, 10, 20, 30])
# print(y)
# y.rotate(3) #deque([10, 20, 30, 40, 50, 60])
# print(y)

#namedtuple is collection of tuple and dictionary
# In dictionaries manipulation is not easy so we use namedtuple 
# import collections
# frame=collections.namedtuple("std_name",["name","age","no"])
# data1=frame("abc",67,6667)
# # data2=frame("bac",78,4544)
# # data3=frame(input("enter the name"),input("enetr the age"),input("enter the no"))
# print(data1)
# # # print(data2)
# # # print(data3)
# # print(data1[0])  # return value using indexing
# # print(list(data1))
# # print(data1._fields) #return keys
# # z=data1._asdict()
# # print(z)   #return dictionary
# n=frame._make([1000,2000,300])
# print("n=",n)
# b=data1._replace(name="cba") #replace name
# print(b)






