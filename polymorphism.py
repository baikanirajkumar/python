class c_1():
    def __init__(self,a,b):
        self.name=a
        self.age=b
    def met_1(self):
        print("my name is",self.name)
        print("my age is",self.age)
    @staticmethod
    def met_2(p):
        print("name",p.name)
        print("age",p.age)
x=c_1("rajkumar",25)
y=c_1("raj",26)
# x.met_2(x)  # it is usedin past classes to call static method


#instead of calling the static method directly we are calling differently..i.e:polymorphism
# def fun_x(k):
#     k.met_1()
#     k.met_2(k)
# for i in [x,y]:
#     fun_x(i)



# #example from  pdf
# #polymorphism with functions and objects
# class tomato():
#     def type(self):
#         print("type")
#     def color(self):
#         print("color")
# class fruit():
#     def type(self):
#         print("apple")
#     def color(self):
#         print("red")
# def fun(obj):
#     obj.type()
#     obj.color()
# t=tomato()
# f=fruit()
# fun(t)
# fun(f)


# #polymorphism
# class c_1():
#     def met_1(self):
#         print("this is method 1")
#     def met_2(self):
#         print("this is method 2")
# class c_2():
#     def met_1(self):
#         print("this is method 3")
#     def met_2(self):
#         print("this is method 4")
# c=c_1()
# d=c_2()
# for i in (c,d):
#     i.met_1()
#     i.met_2()

