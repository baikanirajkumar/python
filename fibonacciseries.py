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

x=int(input("enter the number:"))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(x-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c



