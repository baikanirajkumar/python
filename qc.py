# a=input()
# b=a[::-1]
# print("reversed string",b)

# a=input()
# b=a[::-1]
# if a==b:
#     print("palindrome")
# else:
#     print("not palindrome")


# a=int(input())
# if a<=1:
#     print("not prime number")
# else:
#     for i in range(2,a):
#         if a%i==0:
#             print("not prime number")
#             break
#     else:
#         print("prime")

# n=int(input())
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# print(a,end=" ")
# print(b,end=" ")
# for i in range(2,n):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c



# a=int(input())
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)


# a=list(map(int,input("enter the number:").split(",")))
# duplicates=[]
# for i in a:
#     if a.count(i)>1 and i not in duplicates:
#         duplicates.append(i)
#     else:
#         continue
# print(duplicates)

# a=list(map(int,input("enter the list:").split(",")))
# b=list(set(a))
# print(b)

# a=list(map(int,input().split(",")))
# unique=[]
# for i in a:
#     if i not in unique:
#         unique.append(i)
#     else:
#         continue
# print(unique)


# a=list(map(int,input("enter the list:").split(",")))
# a.sort(reverse=True)
# print(a[1])


# a=input()
# count=0
# for i in a:
#     if i.lower() in "aeiou":
#         count+=1
# print(count)


# lst=[10,20,23,1,3,45]
# largest=lst[0]
# for i in lst:
#     if i>largest:
#         largest=i
# print(largest)

# a=int(input())
# temp=a
# length=len(str(a))
# sum=0
# while temp>0:
#     rem=temp%10
#     sum+=rem**length
#     temp=temp//10
# if sum==a:
#     print("amsnum")
# else:
#     print("not arm")


a=input()
freq={}
for ch in a:
    freq[ch]=freq.get(ch,0)+1
print(freq)



