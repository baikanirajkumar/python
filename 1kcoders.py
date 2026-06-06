""" Question: Write a program to print numbers from 1 to n. Explanation:
 Use a loop starting from 1 to n and print each number.
Input: n = 5 - Output: 1 2 3 4 5"""
# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     print(i,end=" ")


"""2. Print Numbers from m to n
Question: Write a program to print numbers from m to n. 
Explanation: Loop from m to n and print values. - 
Input: m = 3, n = 7 - Output: 3 4 5 6 7"""

# m=int(input("enter the number:"))
# n=int(input("enter the number:"))
# for i in range(m,n+1):
#     print(i,end=" ")


"""3. Print Numbers from n to 1 in Reverse
Question: Write a program to print numbers in reverse from n to 1.
Explanation: Use a loop starting from n and decrement to 1. - 
Input: n = 5 - Output: 5 4 3 2 1"""

# a=int(input("enter the number:"))
# for i in range(a,0,-1):
#     print(i,end=" ")



"""4. Print Numbers from n to m in Reverse
Question: Write a program to print numbers from n to m in reverse.
Explanation: Start from n and go down to m. - 
Input: n = 10, m = 6 - Output: 10 9 8 7 6"""


# n=int(input("enter the number:"))
# m=int(input("enter the number:"))
# for i in range(n,m-1,-1):
#     print(i,end=" ")

"""5. Sum of n Natural Numbers
Question: Write a program to calculate the sum of first n natural numbers. 
Explanation: Use formula or loop to sum from 1 to n. -
Input: n = 5 - Output: 15"""

# n=int(input("enter the number:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)


"""6. Factorial of a Number
Question: Write a program to find the factorial of a number.
Explanation: Multiply all numbers from 1 to n. - 
Input: n = 5 - Output: 120"""

# a=int(input("enter the number:"))
# fact=1
# for i in range(1,a+1):
#     fact*=i
# print(fact)


"""7. Sum of m to n Numbers
Question: Write a program to find the sum of all numbers from m to n. 
Explanation: Loop from m to n and add values. - 
Input: m = 3, n = 6 - Output: 18"""

# m=int(input("enter the number:"))
# n=int(input("enter the number:"))
# z=0
# for i in range(m,n+1):
#     z+=i
# print(z)


"""8. Product of m to n Numbers
Question: Write a program to find the product of numbers from m to n. 
Explanation: Loop from m to n and multiply values. - 
Input: m = 2, n = 4 - Output: 24"""

# m=int(input("enter the number:"))
# n=int(input("enter the number:"))
# z=1
# for i in range(m,n+1):
#     z*=i
# print(z)


"""9. Print Factors of a Number
Question: Write a program to print all factors of a given number. 
Explanation: Check divisibility of number from 1 to n. -
Input: n = 6 - Output: 1 2 3 6"""

# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")
#     else:
#         continue

"""10. Count of Factors
Question: Write a program to count how many factors a number has.
Explanation: Increment count when divisible. - 
Input: n = 6 - Output: 4"""
# n=int(input("enter the number:"))
# z=0
# for i in range(1,n+1):
#     if n%i==0:
#         z+=1
#     else:
#         continue
# print(z)

"""11. Prime Number Check
Question: Check if a number is prime. 
Explanation: A number is prime if it has exactly 2 factors. -
Input: n = 7 - Output: Prime"""

a=int(input("enter the number:"))
if a<=1:
    print("it is not a prime number")
else:
    for i in range(2,a):
        if a%i==0:
            print("it is not a prime number")
            break
    else:
        print("it is prime number")

