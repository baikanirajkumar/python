"""stringfunctions:string functions are built in functions used to perform operations on strings
common string functions(len(),max(),min(),sorted())"""
#len()

# a="python"
# print(len(a))

# b="rajkumar"
# print(max(b)) #u

# c="codegnan"
# print(min(c)) #a

# d="raju"
# print(sorted(d)) #op:['a', 'j', 'r', 'u']

"""string methods: string methods are used with the dot notatation(string.method())"""

# x="rajkumar"
# y="yadav"
# print(x+y)  # concatination of strings(adding of two strings)
# print(x*3)   # replication

# x="raj"
# y=12        # we cannot add integer and string
# print(x+y)   #error

# print("abc">"z")  # based on ascii value


# x="codegnan"  #delete the data
# del x
# print(x)

# x="raj"   # string is immutable to covert it into upper case use another variable
# y=x.upper()
# print(y)
# print(x)

# z="RAJ"
# a=z.lower()
# print(a)


# z="rAJkumar"
# y=z.upper()
# print(y)


# print("hello world".capitalize()) # only at index 0 it will be capitlaize
# print("hello world".title())  #at index 0 and after every white space first letter will become capital
# print("hello world.iam rajkumar".title())  #after full stop
# a="this is string"
# print(a.capitalize())
# print(a.title())


# y="jhggGVVGVU"   # it will convert uppercase to lowercase and lowercase to uppercase
# print(y.swapcase())


# x="rajkumar"  # if we have multiple a's then it will give first index value
# print(x.index("a"))
# # print(x.index("ee"))  #error because it should match the sequence...it is not matching the sequence
# print(x.index("aj"))  #matching the sequence


# # to overcome above error there is find function it will wont show error it will return -1 if the sequence is not available
x="rajkumar"
print(x.find("aaj"))
print(x.rfind("r"))  # take index from right....if the character is not there it will -1
print(x.rindex("ku")) ## take "       "   "......."                                   "show value error


"""⚠️ Important Difference
Function	If substring not found
find()	     returns -1
rfind()    	 returns -1 checks from right side and last occurance
index()	     Error
rindex()	 Error    checks from right side and last occurance"""

x="rajkumar"
y="ramu"
print(x.startswith("r"))
print(x.startswith("a"))
print(x.endswith("r"))
print(x.endswith("b"))
print(x.endswith("rjk")) # return false because it check sequence


# print(x.endswith("a",0,7)) #string.endswith(substring, start, end), it will take three parameters...slicing format

# print(x.startswith("ra",0,7)) #string.startswith(substring, start, end)



# x="rajkumar"
# print(x.rjust(15,"*"))    #rjust=rightjust....here the number(15) should be greater than string size to perform well(adjustment)
# print(x.ljust(10,"*"))    #ljust=leftjust

# print(x.center(15,"*"))   #the string will be in center remaing places will be replaced with ***...once take odd number and check

# x="rajkumar"
# print(x.zfill(10))   # here remaining empty places will be filled with 0's ...same as rjust(empty spaces replace with *)


# x="88888raj88888"   #strip means cutting frontside and backside
# print(x.strip("8"))
# print(x.lstrip("8"))  #lstrip=leftstrip 
# print(x.rstrip("8"))  #rstrip=rightstrip
# x="rajkumar"
# print(x.lstrip("raj"))
# print(x.rstrip("kumar"))


# x="raj kumar"
# print(x.replace(" ","-")) # at white space we are replaceing with -
# print(x.join(["x","y","z"])) #xraj kumar yraj kumar z (output)


# x="123"      # only single digit returns true..if you give float return false(100.4)
# print(x.isdigit())

# print("120.4".isdigit())


# print("hello".isalpha())

# x="rajkumar123"     # returns true if it contains all characters and all numbers but return false if it contains special characters
# x="112231"
# x="hedhjedej12"
# x="hdwhbd 1241567779"  #here it contains special characters return false
# print(x.isalnum())


x="  "  # return true when string contains only white space
# x="rajkumar" #return false because it contains characters within the double quotes
# print(x.isspace())

#unpacking of strings
# a,b,c,*d="[rajkumar]" # for *d remaining elements will be assigned if we print remaining all elemnets will be printed
# print(a)
# print(b)
# print(c)
# print(d)
# ouput for above code
#  [
# r
# a
# ['j', 'k', 'u', 'm', 'a', 'r', ']']


# # unpacking of lists

# a,(b,c),*d=[100,(200,300),400,500,600,700]
# print(a)
# print((b,c))
# print(b)
# print(c)
# print(d)


# #format function it is used in python output formatting
# a="rajkumar"
# b="ilaiah"
# print("hi my name is {} ,my father name is {}".format(a,b))
# print("name is {name},age is {age}".format_map({"name":"rajkumar","age":22})) #dictionary format placing keys in placeholders




