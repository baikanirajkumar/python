# a="rajkumar"
# b=a[::-1]
# print(b)

# a=input()
# b=a[::-1]
# if a==b:
#     print("palindrome")
# else:
#     print("not palindrome")

# a=int(input())
# if a<=1:
#     print("it is not prime number")
# else:
#     for i in range(2,a):
#         if a%i==0:
#             print("it is not prime number")
#             break
#     else:
#         print("it is prime number")

# n=int(input())
# a=int(input())
# b=int(input())
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

# a=list(map(int,input().split(",")))
# duplicates=[]
# for i in a:
#     if a.count(i)>1 and i not in duplicates:
#         duplicates.append(i)
# print(duplicates)

# a="rajkumar"
# b=a.count("j")
# print(b)

# a=list(map(int,input().split(",")))
# unique=[]
# for i in a:
#     if i not in unique :
#         unique.append(i)
# print(unique)

# a=list(map(int,input().split(",")))
# a.sort(reverse=True)
# print(a[1])

# a=list(map(int,input().split(",")))
# largest=a[0]
# for i in a:
#     if i>largest:
#         largest=i
# a.remove(largest)
# second_largest=a[0]
# for i in a:
#     if i>second_largest:
#         second_largest=i
# print(second_largest)

# a=list(map(int,input().split(",")))
# b=a.copy()
# largest=b[0]
# for i in b:
#     if i>largest:
#         largest=i
# b.remove(largest)
# second_largest=b[0]
# for i in b:
#     if i>second_largest:
#         second_largest=i
# print(second_largest)
# print(a)
# print(b)

# a=input()
# b=a.lower()
# count=0
# for i in b:
#     if i in "aeiou":
#         count+=1
# print(count)


# a="rajkumar"
# freq={}
# for i in a:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)

# a=input()
# b=input()
# if sorted(a)==sorted(b):
#     print("anagram")
# else:
#     print("not anagram")

# a=input()
# b=a.split()
# for i in b:
#     b.reverse(i)
# print(b)


# a=input()
# count=0
# for i in a:
#     if i.lower() in "aeiou":
#         count+=1
# print(count)

# a=input()
# b=a.split()
# result=[]
# for i in range(len(b)-1,-1,-1):
#     result.append(b[i])
# print(" ".join(result))

# a=int(input())
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
#     print("not armstrong number")

# a=int(input())
# if a%2==0:
#     print("even")
# else:
#     print("odd")



