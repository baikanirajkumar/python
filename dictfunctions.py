a={"name":"rajkumar","rollno":14}
a["rollno"]=12
# print(a)
# a.setdefault("name","mnbvc")   #if it have the key it doesnot take doesnot have it will be taken
# print(a)
# a.setdefault("classname","mnbvc")   # this item is not present in above so it will be added
# print(a)
# print(a.pop("name"))     # pop the specific key
# print(a)
# print(a.popitem())   #item will be poped
# print(a)

# del a["name"]    #del the specific key
# print(a)


# print(a.get("name","ssss")) #if the key is present in a it will return the value if not return the default value("ssss")
# print(a.keys())
# print(a.values())
# print(a.items())

# a={"name":"rajkumar","age":"thirty"}
# b={"name":"ramesh","age":25}
# print(a.update(b))
# print(a)

# print(sorted(a,reverse=True))
# print(a)
# print(max(a))   #compare with keys and return max key 
# print(max(a,key=a.get))  #compare with values and return max key
# print(a)
# print(min(a,key=a.get)) ##compare with values and return min key



a={"name":"rajkumar","rollno":14}
# print(a)
# print(a.get("name"))
# print(a.keys())
# print(a.values())
# print(a.items())
# a.update({"rollno":15})
# print(a)
# # a.pop("rollno")
# # print(a)
# a.popitem()
# print(a)
# a.clear()
# print(a)
b=a.copy()
print(b)
# print(id(b))
# print(id(a))
a.setdefault("city","chennai")
print(a)