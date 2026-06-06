# a="raj"
# b="kumar"
# h=10
# c=len(a)
# d=len(b)
# e=c+d
# print(c)
# print(d)
# print(e)


# num=int(input("enter the number:"))
# num=num-2
# a=0
# b=1
# print(a)
# print(b)
# for i in range(num):
#     c=a+b
#     print(c)
#     a=b
#     b=c


# a="codegnan"
# b=a[0:8:1]
# c=a[ :8:1]
# d=a[1: :2]
# e=a[1:8: ]
# f=a[ : :3]
# g=a[ : :-1]
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)



# a=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(a,"*",i,"=",a*i)
#     i+=1

# a=int(input("enter the number:"))
# for i in range(1,11):
#     print(a,"*",i,"=",a*i)
#     i+=1


# a=int(input("enter the number:"))
# b=0
# c=1
# print(b,end="")
# print(c,end="")
# for i in range(a):
#     d=b+c
#     print(d,end="")
#     b=c
#     c=d 

# a=["rajkumar","armu","raj","raju","raju","raj"]
# z=0
# y=len(a)
# x=[]
# while z<y:
#     if a[z]=="raj":
#         x.append("raj")
#         z+=1
#     else:
#         z+=1
# print(x)

# #if we get raj in list then we can add it to the empty list 
# a=["ramu","raju","rakesh","rajesh","raj","ramesh","raj","ramu","raj"]
# x=0
# y=len(a)
# z=[]
# while x<y:
#     if a[x]=="raj":
#         z.append("raj")
#         x+=1
#     else:
#         x+=1
# print(z)
# print(z[1])
# print(len(z))

# a=["ram","kumar","raju","raj","raj"]
# b=a.index("raj")
# print(b)


# a=["raj","ramu","rakesh","ramu"]
# b=[i for i in a if i=="ramu"]
# print(b)
# print(len(b))
# print(b[1])


#converting python script to json script
# import json
# x=[10,20,30,40]
# print(x,type(x),x[1])
# y=json.dumps(x)
# print(y,type(y),y[1])

# z=json.loads(y)
# print(z,type(z),z[1])
# x=[10,20,30,40]
# import json
# with open("abcd.json","w")as xyz:
#     json.dump(x,xyz)

# with open("abcd.json") as xyz:
#     d=json.load(xyz)
# print(d)

# dict={"name":"rajkumar","rollno":45,"course":"Btech","name":"ram"}
# print(dict["name"])
# print(dict.get("name"))
# b=dict.setdefault("specialization","csm")
# print(b)
# print(dict)
# c=dict.pop("name")
# print(dict)
# d=dict.popitem()
# print(dict)
# e=dict.popitem()
# print(dict)
# del dict["name"]
# print(dict)

# a={"name":"rajkumar","rollno":24,"couse":"BTECH"}
# b={"name":"chandu","rollno":20}
# c=a.update(b)
# print(a)
# print(max(a))
# print(min(a))
# print(a.keys())
# print(a.values())
# print(a.items())



# #dictionary functions
# a={"name":"rajkumar","rollno":20,"course":"btech"}
# print(a)
# b=a["name"]
# print(b)
# c=a.setdefault("goodboy","chandu")
# print(a)
# d=a.pop("rollno")
# print(a)
# e=a.popitem()
# print(a)
# del a
# print(a)
# print(a.keys())
# print(a.values())
# print(a.items())

# del a["name"]
# print(a)
# rajkumar={"name":"raju","rollno":23,"couse":"btech","name":"chandu"}
# chandu={"name":"chandram","rollno":20,"couse":"pharmacy"}
# c=rajkumar.update(chandu)
# print(rajkumar)
# a=rajkumar.get("name")
# print(a)
# b=rajkumar["name"]
# print(b)

# a=10
# a+=10 #a=a+10
# print(a)

# a=int(input("enter the number"))
# for i in range(10,0,-1):
#     print(a,"*",i,"=",a*i)
#     i-=1



# a=int(input("eneter the number:"))
# i=1
# while a<=10:
#     if i<=10:
#         print(a,"*",i,"=",a*i)
#         i+=1
#     else:
#         i+=1



# a=int(input("eneter the number:"))
# i=10
# while a<=10:
#     if i<=10 and i>=1:
#         print(a,"*",i,"=",a*i)
#         i-=1
#     else:
#         i-=1

#dict
# x={"username1":{"password":"1234","wins":10,"lost":0,"score":0}}
# y={"username2":{"password":"1234","wins":10,"lost":0,"score":0}}


x={"name":"bharath","rollno":20}
y={"name":"rajkumar","rollno":14}
# a=x["name"]
# print(a)
# print(x.keys())
# print(x.values())
# c=x.setdefault("abc","rajkumar")
# print(x)
# d=x.pop("name")
# print(x)
# e=x.popitem()
# print(x)

# b=x.update(y)
# print(x)

# a=int(input("enter the value"))
# b=int(input("enter the number"))
# c=a+b
# print(c)


# def fun_1(x,y):
#     z=x+y
#     print(z)
# fun_1(400,500)

# x=100
# class classname():
#     x=100 #class variable
#     def fun_1(self,a,b):

# import random
# print(random.randint(1,3))

# c=int(input('enter the number:'))
# while c>50:
#     print(c)
#     c-=1


# a=[1,2,3,4,1,2,3,4]
# # b=[]
# # c=a.count(1)
# # b.append(c)
# # d=a.count(2)
# # b.append(d)
# # e=a.count(3)
# # b.append(e)
# # f=a.count(4)
# # b.append(f)
# # print(b)

# s1="abcf"
# s2="abf"
# s3=""
# for i in s1:
    
#     if i in s2:
#         continue
#     else:
#         s3+=i
# print(s3)


# a=[1,2,3,5,4,1,2,3]
# for i in a:
#     d=a.count(i)
#     if d==1:
#         print(i)

# a="rajkumar"
# print(a)
# del a
# print(a)

x=[1,2,3,4,5]
# x.append(5)
# print(x)

# x.insert(0,9)
# print(x)

# x.extend([1,2])
# print(x)
# x.remove(2)
# print(x)

# print(x)
# x.pop()
# print(x)

# del x[1]
# print(x)

# x.clear()
# print(x)

x=["a","b","c","d",5]
# b=x[2:4:1]
# print(b)
# b=x[2:4:]
# print(b)
# b=x[:5:1]
# print(b)
# b=x[0::1]
# print(b)
# b=x[::1]
# print(b)
# b=x[::-1]
# # print(b)
# del x[1:5:1]
# print(x)

# x=["a","b","c","d","a"]
# del x[4]
# print(x)


# #print second repeated index number
# x=["a","b","c","a","e"]
# y=[]
# count=0
# for i in x:
#     count+=1
#     if i not in y or i!="a":
#             y+=i
#     elif i in y and i=="a":
#           y+=i
#           break
          
# index=count-1
# print(index)

# #reverse a list using for loop
# a=["a","b","c","d","e"]
# b=[]
# for i in a:
#     b.insert(0,i)
# print(b)    

# x=["a","b","c","a","c","a"]
# y=len(x)
# z=y-1
# for i in range(z,0,-1):
#     print(i)


# a="rajkumar"
# b=a[7:8:1]
# print(b)


# a="ajay"
# for i in a:
#     print(i)

# a,b=input("enter the names:").split(",")
# print("hello my name is {0} and my rollno is {1}".format(a,b) )


