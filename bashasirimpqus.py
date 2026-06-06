# #find smallest number in an array
# a=list(map(int,input("enter the list:").split(",")))
# smallest=a[0]
# for num in a:
#     if num<smallest:
#         smallest=num
# print(smallest)

# #find largest number in an array
# a=list(map(int,input("enter the number:").split(",")))
# largest=a[0]
# for num in a:
#     if num>largest:
#         largest=num
# print(largest)


# #print common characters in both strings
# a=input("enter s1:")
# b=input("enter s2:")
# for i in a:
#     if i in b:
#         print(i,end="")
#     else:
#         continue

# #count vowels and consonents in a string
# a=input("enter the string:")
# vowels=0
# consonents=0
# for i in a:
#       if i.isalpha():
#         if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#             vowels+=1
#         else:
#             consonents+=1
# print(vowels)
# print(consonents)

# #separate even and odd number from list
# a=list(map(int,input("enter the list:").split(",")))
# even=[]
# odd=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# #reverse each word in a string
# a="I love python"
# b=a.split()
# for i in b:
#     c=i[::-1]
#     print(c,end=" ")

# #reverse a string without slicing
# a=input("enter the string:")
# b=""
# for i in range(len(a),0):
#     b.append(i)
# print(b)