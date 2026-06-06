# #fibonacci series
# num=int(input("enter the number:"))
# a=0
# b=1
# print(a,end="")
# print(b,end="")
# for i in range(2,num+1):
#     c=a+b
#     print(c,end="")
#     a=b
#     b=c

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


# #find missing number in an array
# a=list(map(int,input("enter the list:").split(",")))
# n=max(a)
# expected_sum=n*(n+1)//2
# actual_sum=sum(a)
# difference=expected_sum-actual_sum
# print(difference)


# #convert two lists into dict/tuple
# a=list(map(int,input("enter the list:").split(",")))
# b=list(map(int,input("enter the list:").split(",")))
# c=dict(zip(a,b))
# print(c)

# #find the sum of digits in a string
# a=input("enter the string")
# sum=0
# for i in a:
#     if i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0":
#         i=int(i)
#         sum+=i
#     else:
#         continue
# print(sum)

# #alternate code
# a=input("enter the string:")
# total=0
# for i in a:
#     if i.isdigit():
#         i=int(i)
#         total+=i
# print(total)

# #reverse each word in a string
# a=input("enter the string:")
# b=a.split()
# for i in b:
#     i=i[::-1]
#     print(i,end=" ")

# #sum of two numbers equal to target
# a=list(map(int,input("enter the number:").split(",")))
# target=9
# result=[]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==target:
#             result.append([a[i],a[j]])
# print(result)


# #reverse a number
# a=int(input("enter the number:"))
# reverse=0
# while a>0:
#     lastdigit=a%10
#     reverse=reverse*10+lastdigit
#     a=a//10
# print(reverse) 



# a=int(input("enter the number:"))
# temp=a
# b=len(str(a))
# am=0
# while temp>0:
#     lastdigit=temp%10
#     value=lastdigit**b
#     am+=value
#     temp=temp//10
# if a==am:
#     print("armstrong number")
# else:
#     print("not armstrong number")

# #separate even and odd numbers from list
# a=list(map(int,input("enter the list").split(",")))
# even=[]
# odd=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("even numbers",even)
# print("odd numbers",odd)

# #count how many even and odd numbers present in list
# a=list(map(int,input("enter the list:").split(",")))
# evencount=0
# oddcount=0
# for i in a:
#     if i%2==0:
#         evencount+=1
#     else:
#         oddcount+=1
# print("evencount:",evencount)
# print("oddcount:",oddcount)

# #print second largest number from the list
# a=list(map(int,input("enter the number:").split(",")))
# b=a[0]

# #print abbrevation
# a=input("enter the string:")
# b=a.split()
# for i in b:
#     print(i[0],end="")


# a=(10)   #int
# print(type(a))



#find the second largest number in a list
a=list(map(int,input("enter the number:").split(",")))
a.sort(reverse=True)
print(a[1])

