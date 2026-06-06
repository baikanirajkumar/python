# x=int(input("enter the number:")) #print the numbers from 1 to 10
# while x<=10 and x>=1:
#     print("the x value is:",x)
#     x+=1
# print("the end of loop")


# age=int(input("enter the age:")) #checking eligibility for voting
# if age>=18:
#     print("he is eligible for voting")
# else:
#     print("he is not eligible for voting")


# a=int(input("enter the number:"))
# while a<=10 and a>=1:
#     print("the value of a:",a)
#     a-=1
# print("end of loop")


# a=int(input("enter the number:"))
# if a%2==0:
#     a+=2
#     print("the value is:",a)  
# else:
#     print("enter the even number")

a=["apple","banana","apple","pomagranate"]
y=len(a)
z=0
c=[]
while z<y:
    if a[z]=="apple":
        a.append(z)
        if len(c)>1:
            print(c[1])     
    z+=1
    

# a=["abc","def","apple","yyy","pineapple","grapes","yyy","farmer"]
# x=len(a)
# z=0
# m=[]
# while z<x:
#     if a[z]=="yyy":
#         m.append(z)
#         if len(m)>1:
#             print(m[1])
#     z+=1
