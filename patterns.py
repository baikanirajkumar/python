# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()

# x=1
# for i in range(5):
#     for j in range(5):
#         print(x,end=" ")
#         x+=1
#     print()


# x=1
# for i in range(5):
#     for j in range(5):
#         print(x,end=" ")
#     x+=1
#     print()



# for i in range(5):
#     for j in range(1,6):
#             print(j,end=" ")
#     print()


# x=97
# for i in range(5):
#     for j in range(5):
#         y=chr(x)
#         print(y,end=" ")
#         x+=1
#     print()


# x=97
# for i in range(5):
#     for j in range(5):
#         y=chr(x)
#         print(y,end=" ")
#     x+=1
#     print()



# for i in range(5):
#     x=97
#     for j in range(1,6):
#         y=chr(x)
#         print(y,end=" ")
#         x+=1
#     print()

# for i in range(1,6):
#     for j in range(i,i+5):
#         if j<=5:
#             print(j,end=" ")
#         else:
#             print(j-5,end=" ")
#     print()

# k=1
# for i in range(5):
#     for j in range(0,k):
#         print("*",end=" ")
#     k+=2
#     print()


# k=1
# for i in range(5):
#     for j in range(0,k):
#         print(k,"*",end=" ")
#     k+=1
#     print()


# maybe for exam
# for i in range(1,6):
#     print(" "*(i-1)*2,end="")
#     y=""
#     for j in range(i,6):
#         y=y+str(j)+"*"
#     print(y.rstrip("*"))

# x=["a","b","c","c","d","e","f","g","a","b","c","d"]
# y=set(x)
# a=x.count("a")
# b=x.count("b")
# c=x.count("c")
# d=x.count("d")
# e=x.count("e")
# f=x.count("f")
# g=x.count("g")
# print(max(a,b,c,d,e,f,g))
# print()



# for i in range(1,6):
#     print(" "*(i-1)*2,end="")
#     y=""
#     for j in range(i,6):
#         y=y+str(j)+"*"
#     print(y.rstrip("*"))

# #empty code
# x=["a","b","c","d","e","f","g","h","i","j","k","a"]
# y=set()
# z=tuple(y)
# data=dict.fromkeys(z)
# print(data)
# for i in z:
#     data[i]=x.count(i)
# print(data)
# highest_value=max(data,key=data.get)
# print(highest_value)
# required=[]

# for i in range(1,6):
#     print(" "*(i-1)*2,end="")
#     y=""
#     for j in range(i,6):
#         y=y+str(j)+"*"
#     print(y.rstrip("*"))
# for i in range(1,6):
#     print(" "*(i-1)*2,end="")
#     y=""
#     for j in range(i,6):
#        y=y+str(j)+"*"
#        print(y.rstrip("*")) 


# x=97
# for i in range(5):
#     for j in range(5):
#         y=chr(x)
#         print(y,end=" ")
#         x+=1
#     print()


# a=65
# print(ord("z"))



'''a a a a a 
b b b b b
c c c c c
d d d d d
e e e e e'''

# x=97
# for i in range(5):
#     for j in range(5):
#         y=chr(x)
#         print(y,end=" ")
#     print()
#     x+=1


# for i in range(5):
#     x=97
#     for j in range(5):
#         y=chr(x)
#         print(y,end=" ")
#         x+=1
#     print()

# for i in range(1,6):
#     for j in range(i,i+5):
#         if j<=5:
#             print(j,end=" ")
#         else:
#             print(j-5,end=" ")
#     print()
      

# x=97
# for i in range(1,6): 
#     for j in range(1,6):
#         if x<=102:
#             y=chr(x)
#             print(y,end=" ")
#             x+=1
#         else:
#             print(y-5,end=" ")
#     print()


# for i in range(1,6):
#     for j in range(i,i+5):
#         if j<=5:
#             print(j,end=" ")
#         else:
#             print(j-5,end=" ")
#     print()
    

#error
# x=65
# for i in range(x,x+5):
#     for j in range(i,i+5):
#         y=chr(x)
#         if j<=69:
#             print(y,end=" ")
#             x+=1
#         else:
#             print(j,end=" ")
#             x+=1
#     print()



# for i in range(5):
#     x=65
#     for j in range(5):
#         y=chr(x)
#         print(y,end=" ")
#         x+=1
#     print()


x=65
for i in range(x,x+5):
    for j in range(i,i+5):
        y=chr(x)
        if j<=69:
            print(j,end=" ")
            x+=1
        else:
            print(j-5,end=" ")
            x+=1
    print()

        