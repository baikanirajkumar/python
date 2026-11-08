"""regex(regular expression):regular expression is the sequence of characters used to 
    search,match,validate and manipulate the text patterns"""
#group():it is method that returns text matched by the regular expression

# import re
# text="my phone number is 6305517955"
# result=re.search(r"\d{10}",text)
# print(result.group())




# # re.search():Searches for the first occurrence of a pattern in a string.
# import re
# text="my name is raj kumar"
# result=re.search("rajkumar",text)
# if True:
#     print("found")


# re.findall():returns all matched as a list
# import re
# text="my 10 and 20 of 30"
# result=re.findall(r"\d+",text)
# print(result)

#re.split():splits the string based on pattern
# import re
# text="this,is,rajkumar"
# result=re.split(",",text)
# print(result)

# #re.sub():replaces matched text
# import re
# text="i love java"
# result=re.sub("java","python",text)
# print(result)

# ---------------------------

# re.search()      → Searches for a pattern anywhere in the string.
# re.match()       → check beginning
# re.fullmatch()   → match entire string
# re.findall()     → find all matching values  (no group method)
# re.sub()         → replace/substitute (no group method)

# import re
# text="My phone number is 63055178955"
# result=re.search(r"\d+",text)
# print(result.group())


import re
text="python pragramming"
result=re.match("python",text)
print(result.group())

# import re
# text="1234"
# result=re.fullmatch(r"\d+",text)
# print(result.group())

# import re
# text="the values are 10  and 20"
# result=re.findall(r"\d+",text)
# print(result)


# import re
# text="python programming"
# result=re.sub("python","Java",text)
# print(result)


# import re
# email=input().strip()
# pattern=r"\w+@\w+\.\w+"
# if re.fullmatch(pattern,email):
#     print("Valid mail")
# else:
#     print("Invalid mail")


# import re
# phone=input().strip()
# pattern=r"\d{10}"
# if re.fullmatch(pattern,phone):
#     print("valid phone number")
# else:
#     print("invalid phone number")

# import re
# bikenum=input().strip()
# pattern=r"[A-Z]{2}\d{2}[A-Z]{2}\d{4}"
# if re.fullmatch(pattern,bikenum):
#     print("valid bike number")
# else:
#     print("invalid bike number")



r'''Regex	Meaning
\d	Digit
\D	Not digit
\w	Word character
\W	Not word character
\s	Whitespace
\S	Not whitespace
.	Any character
[]	Character set
^	Beginning
$	End
+	One or more
*	Zero or more
?	Zero or one
{n}	Exactly n times
{n,m}	n to m times'''


import re 
text="my phone number is 6305517955"
result=re.search(r"\d+",text)
print(result.group())


text="python programming"
result=re.match("python",text)
print(result.group())

text="1234"
result=re.fullmatch(r"\d+",text)
print(result.group())


text="my numbers are 10 and 20"
result=re.findall(r"\d+",text)
print(result)

text="python programming"
result=re.sub("python","java",text)
print(result)

# a=input().strip()
# pattern=r"\w+@\w+\.\w+"
# if re.fullmatch(pattern,a):
#     print("valid mail")
# else:
#     print("invalid mail")

# a=input("enter the number:").strip()
# pattern=r"\d+"
# if re.fullmatch(pattern,a):
#     print("valid phone number")
# else:
#     print("invalid phone number")

# a=input().strip()
# pattern=r"[6-9]{1}\d{9}"
# if re.fullmatch(pattern,a):
#     print("valid num")
# else:
#     print("invalid number")

# a=input().strip()
# pattern=r"[A-Z]{2}\d{2}[A-Z]{2}\d{4}"
# if re.fullmatch(pattern,a):
#     print("valid bike num")
# else:
#     print("invalid bike num")

# bike number pattern:r"[A-Z]{2}\d{2}[A-Z]{2}\d{4}"
# phone number pattern :r"\d{10}"
# phone number = r"\+[0-9]{2}[6-9]\d{9}"
# email :r"\w+@\w+.\w+" 
# emial: r"[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z0-9]+"

