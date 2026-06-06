# creates the new sets
x={"a","b","c","d","a"}  #removes duplicates  and return combination elements of x and y
y={"e","f","g","h","a"}    
# print(x.union(y))

# print(x.intersection(y))   #returns common elements
# z=x&y                 # &(ampersand is used as intersection symbol)
# print(z)


# z=x-y      #difference
# print(z)

# print(x.symmetric_difference(y))
# z=x^y
# print(z)

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# result = A.symmetric_difference(B)
# print(result)
#output
# {1, 2, 5, 6}


# x.difference_update(y) # removes common elements from x and y and it will be updated
# print(x)

# y.symmetric_difference_update(x)
# print(y)
# x.add("z")
# print(x)

# x.remove("b")
# print(x)

# print(x.pop())
# print(x)

# del x   #deletes entire set
# print(x)

# print(x.clear())  # clears the data in the set
# print(x)



# x={"a","b","c"}  #if the element is not in set doesnot return value error
# x.discard("a")
# print(x)

a={"a","b","c","d"}
b={"a","b","c"}
print(b.issubset(a)) #returns true because  b is subset of a
print(a.issuperset(b))  # return true because a is superset of b

a={"x","y","z"}   # return true if no common elements present in both sets
b={"a","b","c"}
print(a.isdisjoint(b))


# a={100,200,300,400}  # max and min function will work only on homogenous data
# print(max(a))
# print(min(a))
# print(len(a))
# print(sum(a))       #sum function             "                       "


# c={"x","y","z"}
# print(c)            #{'z', 'x', 'y'}
# d=c
# d.remove("z")
# print(c)            #{'x', 'y'}
# print(id(c))        #2307000703616
# print(id(d))        #2307000703616


# d=c.copy()
# print(d)