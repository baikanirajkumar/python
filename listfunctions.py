#append function
# x=[1,2,3,4]
# x.append(5)
# print(x)

# #insert function
# x=[1,2,3,4]
# x.insert(0,9)
# print(x)

#extend function
# x.extend([6,7])
# print(x)

#remove function
# y=[1,2,3,4]
# y.remove(1)
# print(y)

# #pop function
# y=[1,2,3,4.5]
# y.pop()
# print(y.pop())
# print(y)

# # delete function
# y=[1,2,3,4]
# del y[1]  #used to remove the element in particular index
# print(y)

# #clear function
# z=[1,2,3,4,5,6,7,8,9]
# z.clear()
# print(z)

# #slicing
# #list slicing :-retreviwing sub list from the current list
# a=[1,2,3,4,5,6,7,8,9]
# m=a[2:6:1]
# print(m)

# n=a[-9:-1:1]
# print(n)

# o=a[0:5]
# print(o)

# p=a[:6:1]
# print(p)

# q=a[1::1]
# print(q)

# r=a[::1]
# print(r)

# s=a[::-1]
# print(s)


# x=["a","b","c","d","e"]
# print(x)
# del x[1:4:2]
# print(x)


# x=[1,2,3,4,5]
# x.append(6)
# print(x)
# x.insert(0,1)
# print(x)
# x.extend([2,3])
# print(x)


# x=["a","b","c","b","a","e"]
# x.sort()
# print(x)
# print(len(x))
# print(x.count("a"))
# print(x.index("a"))
# print(max(x))
# print(min(x))

# x=[1,2,3,4,5]
# print(sum(x))

# #replacing the element
# x=["a","b","b","d"]
# x[2]="c"
# print(x)

# #copy function
# x=["a","b","c","d"]
# y=x.copy()
# print(id(x))
# print(id(y))

# #sort
# x=["a","b","a","d","e"]
# x.sort()#reverse=False(default)
# print(x)

# x.sort(reverse=True)
# print(x)

# # #sorted
# x=["a","b","c","d","e"]
# print(sorted("hello",reverse=False))
# print(x)

# x=["a","b","c","d","e","a"]
# print(sorted(x))
# print(x)


# x=["a","b","c",1,"e"]
# print(any(x)) #if any one true return true if all false return false
# print(all(x)) #if all true return true else return false


# y=["a","b","c"]
# b=list(enumerate(y))
# c=tuple(enumerate(y))
# print(b)
# print(c)

# #enumerate
# x=["a","b","c"]
# y=dict(enumerate(x))#we can take list ,tuple,set,dictionary
# print(y)

# #reverse
# a=["a","b","c"]
# a.reverse()
# print(a)