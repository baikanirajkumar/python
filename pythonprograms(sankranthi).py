# #In python arrays are replaced with lists
# a=[1,2,3,4,5,6,7,8,10]  #(using formula)
# b=sum(a)
# c=10*(11)//2  #(formula:n*(n+1)//2)
# d=c-b
# print(d)

#output:9

# #without formula
# a=[1,2,4,5,6,7,9]
# b=0
# c=1
# for i in a:
#     if a[b]==c:
#         b+=1
#         c+=1
#     else:
#         print(c)
#         b+=1
#         c+=2

"""output:3
        8"""


# #find the duplicate in an array(list)
# a=list(map(int,input("enter the list:").split(",")))
# # a=[1, 3, 4, 2, 5, 3]
# b=[]
# c=0
# for i in a:
#     if a[c] not in b:
#         b.append(a[c])
#         c+=1
#     elif a[c] in b:
#         print(a[c])
#         c+=1


#max and min element in unsorted array
# #using max and min functions
# a=[1,3,7,2,3,1,5,6]
# print(max(a))
# print(min(a))

# #using loop
# a=[1,4,2,3,5,8,45]
# max_element=a[0]
# min_element=a[0]
# for i in a:
#     if i>max_element:
#         max_element=i
#     if i<min_element:
#         min_element=i
# print("maximum element:",max_element)
# print("minimum element:",min_element)



# a=[2, 4, 3, 5, 6, -1]
# b=[{},{}]
# target=5
# for i in a:
#     if a[0]+i==5:
        
# a=int(input("enter the number:"))
# for i in range(a):
#     if i==0:
#         continue
#     else:
#         b="#"
#         c=7-i
#         d=" "
#         print(c*d,b*i)

a=int(input("enter the number:"))
b="*"
c=" "
d=4
for i in range(a):
        if i>=0:
        # elif i>1:
                e=d-i
                print(e*c," ",b*i," ")
