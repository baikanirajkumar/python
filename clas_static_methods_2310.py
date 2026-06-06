class cl_1():
    x="class variable"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def cl_mthd(cls):
        cl_1.x="updated class varible"
        k="class method local variable"
        print("this is class method")
        return k
    
    @classmethod
    def cl_mthd_2(cls,name,age):
        return cls(name,age)
        

    
    def m_1(Self):
        print("x=",cl_1.x)
        print(f"his name={Self.name}")
        print(f"with age of {Self.age}")
    @staticmethod
    def fn_1(d):
        print("function statement ",cl_1.x)
        print("name=",d.name,"age=",d.age)

c=cl_1('xyz',25)
# # c.fn_1(c)
print(c.cl_mthd())
# c.m_1()
# print("out of class",cl_1.x)

e=cl_1.cl_mthd_2("abc",30)
c.m_1()
c.fn_1(e)


f=cl_1.cl_mthd_2("klm",40)
f.m_1()