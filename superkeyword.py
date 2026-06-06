# #super() keyword is used to call the constructors or methods of a parent class from the child class
# class parent():
#     def __init__(self):
#         print("this is parent constructor")
# class child(parent):
#     def __init__(self):
#         super().__init__() #calling the parent class constructor
#         print("this is child constructor")
# c=child()


#calling the parent class method
class parent():
    def __init__(self):
        print("this is parent constructor")
    def met_1(self):
        print("this is parent class met1")
class child(parent):
    def __init__(self):
        print("this is child class constructor")
    def met_2(self):
        super().met_1()
        print("this is child class met2")
c=child()
c.met_2()