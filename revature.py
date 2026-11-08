# #reverse a string
# a=input("enter the string:")
# b=a[::-1]
# print(b)

# #palindrome
# a=input("enter the string:")
# b=a[::-1]
# if a==b:
#     print("palindrome")
# else:
#     print("not palindrome")

# #prime number
# a=int(input("enter the number:"))
# if a<=1:
#     print("it is not prime number")
# else:
#     for i in range(2,a):
#         if a%i==0:
#             print("it is not prime number")
#             break
#     else:
#         print("it is prime number")

# #fibonacci series
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# print(a,end=" ")
# print(b,end=" ")
# for i in range(2,5):
#     c=a+b
#     print(c,end=" ")
#     a=b 
#     b=c


# #factorial
# a=int(input("enter the number:"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# #find duplicates in a list
# a=list(map(int,input("enter the number:").split(",")))
# duplicates=[]
# for i in a:
#     if a.count(i)>1 and i not in duplicates:
#         duplicates.append(i)
# print(duplicates)

#remove duplicates from the list
# a=list(map(int,input("enter the list").split(",")))
# b=list(set(a))
# print(b)

# a=list(map(int,input("enter the list").split(",")))
# unique=[]
# for i in a:
#     if i not in unique:
#         unique.append(i)
# print(unique)

#second largest element
# a=list(map(int,input("enter the list").split(",")))
# a.sort()
# print("second largest",a[-2])

# #count the vowels
# a=input("enter the string:")
# b=a.lower()
# count=0
# for i in b:
#     if i in "aeiou":
#         count+=1
# print(count)


# #frequency of the characters //go through revature file in chatgpt 
a=input("enter the string:")
freq={}
for i in a:
    freq[i]=freq.get(i,0)+1
print(freq)

#largest element in the list
# a=list(map(int,input("enter the list:").split(",")))
# a.sort()
# print(a[-1])


# list=list(map(int,input("enter the list").split(",")))#[10,20,60,30,70]
# largest=list[0]
# for i in list:
#     if i>largest:
#         largest=i
# print(largest)

#swap two numbers
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# a,b=b,a
# print(a)
# print(b)


# #even or odd
# a=int(input("enter the number:"))
# if a%2==0:
#     print("even")
# else:
#     print("odd")

# a=int(input("enter the number"))
# temp=a
# digit=len(str(a))
# sum=0
# while temp>0:
#     rem=temp%10
#     sum+=rem**digit
#     temp=temp//10
# if a==sum:
#     print("Armstrong number")
# else:
#     print("Not armtrong number")


