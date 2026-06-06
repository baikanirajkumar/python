# # task is to get the data who scored more than 59 marks
# x=[("ram",80),("raj",60),("kumar",45)]
# y=[]
# for name,marks in x:
#     if marks>59:
#         y.append((name,marks))
# print(y)
# to overcome writing more code in above example we using below concept

# #list comprehension
# z=[(name,marks) for name,marks in x if marks>59]
# print(z)

# #tuple comprehension
# z=tuple((name,marks) for name,marks in x if marks>59)
# print(z)

# #set comprehension
# z=set((name,marks) for name,marks in x if marks>59)
# print(z)


# # sir given example
# x=[10,20]
# z=[i+1 for i in x if i>2]
# print(z)


# #pdf examples
#squares example
# z=[x*x for x in range(6)]
# print(z)

# #even numbers example
# numbers=[9,20,30,40]
# even=[i for i in numbers if i%2==0]
# print(even)

# #odd numbers example
# numbers=[1,2,3,4,5,7]
# odd=[i for i in numbers if i%2!=0]
# print(odd)

# #uppercase a list of strings
# list=["raj","kumar","baikani"]
# upper=[name.upper() for name in list]
# print(upper)

# #lowercase a list of strings
# list=["RAJ","KUMAR","BAIKANI"]
# lower=[name.lower() for name in list]
# print(lower)

# #uppercase
# a=["laptop","mouse","pendrive"]
# upper=[name.upper() for name in a]
# print(upper)

# #prices
# prices=[1000,2000,3000]
# discount=[price*0.9 for price in prices]
# print(discount)

# #doubt
# boolean=[True,False,True,False]
# indexes=[i for i,stock in enumerate(boolean) if stock]
# print(indexes)


# #product info as tuples

# product_info=[("laptop",10000),("bike",20000),("car",25000),("watch",30000)]
# price=[name for name,price in product_info if price>10000]
# print(price)









