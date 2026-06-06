# #for loop
# for i in range(5):
#     print(i)

# li=["rajkumar","ramesh","prashanth","rajkumar"]
# count=0
# for i in li:
#     if i=="ramesh":
#         count+=1
# print(count)


# #print 1 and its index from a list
# a=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,1,2,2,3,3]
# count=0
# index=0
# for i in a:
#     if i==1:
#         count+=1
#         print(i,index)
#     index+=1
# print(count)



# #reverse a string
# a=str(input("enter the string:"))
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev=rev+a[i]
# print(rev)

# b=str(input("enter the string:"))
# c=b[::-1]
# print(c)

# #reverse a number
# a=int(input("enter the number:"))
# b=str(a)
# c=b[::-1]
# d=int(c)
# print(d,type(d))

# # check wheather the given string is palindrome or not
# a=str(input("enter the string:"))
# b=a[::-1]
# if a==b:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

#reverse a string without slicing and checking whaeather it is palindrome or not
# a=str(input("enter the string:"))
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev=rev+a[i]
# if a==rev:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")


# #part-8
# #find the max element from the list
# a=list(map(int,input("enter the list:").split(",")))
# max=a[0]
# for i in a:
#     if i>max:
#         max=i
# print(max)

# print(max(1,3,2))
# print(min(5,7,2))

#print  how many words present in the sentence
a=list(map(str,input("enter the strings:").split(",")))
count=[]
for i in a:
    b=i.split()
    x=0
    for j in b:
        x+=1
    count.append(x)
print(max(count))


