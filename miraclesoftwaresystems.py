#arrays
#.Move all negative numbers to one side of the array. 
# a=list(map(int,input("enter the list:").split(",")))
# negative=[]
# positive=[]
# for i in a:
#     if i<0:
#         negative.append(i)
#     else:
#         positive.append(i)
# result=negative+positive
# print(result)

# #find maximum element in an array
# a=list(map(int,input("enter the list").split(",")))
# max_num=a[0]
# for i in a:
#     if i>max_num:
#         max_num=i
# print(max_num)

# a=list(map(int,input("enter the list").split(",")))
# a.sort()
# print(a)

#strings
# #1.check if two strings are anagram
# a=input("enter the string:")
# b=input("enter the string:")
# c=a.lower()
# d=b.lower()
# if sorted(c)==sorted(d):
#     print("anagram")
# else:
#     print("not anangram")

# #reverse a string without using built in functions
# a=input("enter the string:")
# b=""
# for i in range(len(a)-1,-1,-1):
#     b+=a[i]
# print(b)

# #find the first non-repating character in the string
# a="rajkumar"
# b=[]
# for i in a:
#     c=a.count(i)
#     b.append(c)
# d=b.index(1)
# print(a[d])

# #count the number of vowels and consonents
# a=input("enter the string:")
# vowels=0
# consonents=0
# b=a.lower()
# for i in b:
#     if i.isalpha():
#         if i in "aeiou":
#             vowels+=1
#         else:
#             consonents+=1
# print(vowels)
# print(consonents)

# #remove duplicate characters from the string
# a=input("enter the string:")
# b=""
# for i in a:
#     if i not in b:
#         b+=i
# print(b)

# #count the frequency of each character
# a=input("enter the string:")
# b=""
# for i in a:
#     if i not in b:
#         print(i,":",a.count(i))
#         b+=i

# #check a string is palindrome
# a=input("enter the string:")
# b=a[::-1]
# if a==b:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")

# #convert the string into uppercase letters without using built in functions
# a=input("enter the string:")
# b=""
# for i in a:
#     if i>="a" and i<="z":
#         b+=chr(ord(i)-32)
#     else:
#         b+=i
# print(b)

a=input("enter the string:")
b=""
for i in a:
    if i>="A" and i<="Z":
        b+=chr(ord(i)+32)
    else:
        b+=i
print(b)