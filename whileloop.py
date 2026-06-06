# a=["abc","def","apple","banana","pineapple","grapes","yyy","farmer"]
# x=len(a)
# z=0
# while z<x:
#     print("the string in loop:",a[z-1])
#     if a[z]="yyy":
#         x=0
#     z+=1


a=["abc","def","apple","yyy","pineapple","grapes","yyy","farmer"]
x=len(a)
z=0
m=[]
while z<x:
    if a[z]=="yyy":
        m.append(z)
        if len(m)>1:
            print(m[1])
    z+=1


# string_r=str(input("enter the string:"))
# length=len(string_r)
# z=0
# output=""
# while z<length:
#     i=string_r[z]
#     if string_r[z]==string_r[2]:
#         i="*"
#         output+=i
#     else:
#         output+=i
#     z+=1
# print(output)



# string_r=str(input("enter the string:"))
# length=len(string_r)
# z=0
# output=""
# while z<length:
#     i=string_r[z]
#     if string_r[z]==string_r[2]:
#         i="*"
#         output+=i
#     else:
#         output+=i
#     z+=1
# print(output)



# n=input()
# replaced=n.replace(n[2],"*")
# print(replaced)




