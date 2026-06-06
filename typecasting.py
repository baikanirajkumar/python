# a=10
# print(type(a))
# print(float(a))
# print(complex(a))
# print(bool(a))
# print(str(a))
# #print(list(a))     we cannot convert int to list
# #print(set(a))      we cannot convert int to set
# #print(dict(a))     we cannot convert int to dict
# #print(tuple(a))    we cannot convert int to tuple
# print(str(a))

# # here we going to convert float into different types
# b=25.0
# print(type(b))
# print(int(b))
# print(complex(b))
# print(bool(b))
# print(str(b))
# print(list(b))     #we cannot convert float to list
# print(set(b))      #we cannot convert float to set
# print(tuple(b))    #we cannot convert float to tuple
# print(dict(b))     #we cannoy convert float to dict



#Now we are going to discuss about string typecasting
# c="10"
# print(int(c))
# print(float(c))
# print(bool(c))
# print(complex(c))
# print(list(c))
# print(set(c))
# print(tuple(c))
# print(dict(c))          #we cannot convert string to dictionary

# c="apple" #"apple" is not a number, it is a text string, so Python cannot convert it to an integer.
# # print(int(c))      #we cannot convert string into int 
# # #but whenever we are writing numbers in place of string then it will be executed ....we already did above once check it
# # #print(float(c))   # we cannot convert string to float
# print(bool(c))
# # #print(complex(c))  #we cannot convert string to complex
# print(list(c))
# print(set(c))
# print(tuple(c))
# # print(dict(c))      #we cannot convert string to dictionary

# c="10.9"
# # print(int(c))     # error
# print(float(c))
# print(bool(c))
# print(complex(c))
# print(list(c))
# print(set(c))
# print(tuple(c))
# #print(dict(c))     #we cannot convert string to dictionary



# # Now we are going to discuss about list typecasting
# list=["apple",True,100,10+30j]
# print(list)
# print(type(list))
# #print(int(list))           not allowed
# #print(float(list))         not allowed
# #print(complex(list))       not allowed
# print(str(list))
# print(set(list))
# print(tuple(list))
# print(bool(list))
# # print(dict(list))          #need list of key value pairs
  


# #now we are going to discuss about tuple typecsting
# tuple=(True,False,10+20j,"Apple")
# #print(int(tuple))                we cannot convert tuple to int
# #print(float(tuple))              we cannot convert tuple to float
# #print(complex(tuple))            we cannot convert tuple to complex
# print(bool(tuple))
# print(list(tuple))
# print(set(tuple))
# #print(dict(tuple))               we cannot convert tuple to dictionary


#now we are  going to discuss about set typecasting

# set={"apple",True,"banana",10+20j,100}
# #print(int(set))                  we cannot convert set into int
# #print(float(set))                we cannot convert set into float
# #print(complex(set))              we cannot convert set into complex
# print(str(set))
# print(bool(set))
# print(list(set))
# print(type(set))
# print(tuple(set))
# #print(dict(set))                 we cannot convert set into dict



#now we are going to discuss about dictionary typecasting
# dict={'name': 'rajkumar','rollno':'22c41a6614','branch':'csm'}
# print(type(dict))
#print(int(dict))           we cannot convert dict to int
#print(float(dict))         we cannot convert dict to float
#print(complex(dict))       we cannot convert dict to complex
# print(bool(dict))
# print(list(dict))
# print(set(dict))
# print(str(dict))
# print(tuple(dict))


#now we are going to discuss about boolean typecasting

# bool=True
# print(type(bool))
# print(int(bool))
# print(float(bool))
# print(complex(bool))
# print(str(bool))
# print(list(bool))           we cannot convert bool to list
# print(tuple(bool))          we cannot convert bool to tuple
# print(set(bool))            we cannot convert bool to set
# print(dict(bool))           we cannot convert bool to dict


#now we are going to discuss about conversion of list to dictionary
a={('name','rajkumar'),('roll no','22c41a6614'),('branch','csm')}
c=dict(a)
print(c)

