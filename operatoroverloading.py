# class c_1():
#     def __init__(self,rollno,age):
#         self.rollno=rollno
#         self.age=age
#     def __add__(self,q):
#         return c_1(self.rollno+q.rollno,self.age+q.age)
#     def __sub__(self,p):
#         return c_1(self.rollno-p.rollno,self.age-p.age)
#     def __mul__(self,r):
#         return c_1(self.rollno*r.rollno,self.age*r.age)
#     def __truediv__(self,r):
#         return c_1(self.rollno/r.rollno,self.age/r.age)
#     def __eq__(self,r):
#         return c_1(self.rollno==r.rollno,self.age==r.age)
#     def __lt__(self,r):
#         return c_1(self.rollno<r.rollno,self.age<r.age)
#     def met_1(self):
#         print(self.rollno)
#         print(self.age)
# c=c_1(24,23)
# c.met_1()
# d=c_1(45,34)
# d.met_1()
# total=c+d
# total.met_1()
# difference=c-d
# difference.met_1()
# multiplication=c*d
# multiplication.met_1()
# truedivision=c/d
# truedivision.met_1()
# lessthan=c<d
# lessthan.met_1()
# equalsequals=c==d
# equalsequals.met_1()


# #for str method  
# class c_2():
#     def __init__(self,s):
#         self.name=s
#     def __str__(self):  #it is called when the object is typecasted into str
#         return f"the object is typecasted into str object {self.name}"
#     def m_1(self):
#         print(self.name)
# obj=c_2("rajkumar")
# print(str(obj))
# obj.m_1()

