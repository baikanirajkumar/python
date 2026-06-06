# #encapsulation

# class bankaccount():
#     def __init__(self):
#         self.__balance=0
#     def deposit(self,amount):
#         self.__balance+=amount
#     def show_balance(self):
#         return self.__balance
# c=bankaccount()
# c.deposit(100)
# print(c.show_balance())



# class parent():
#     def met_1(self):
#         print("met_1")
# class child(parent):       
#     def met_2(self):
#         print("met_2")
# c=child()
# c.met_2()
# c.met_1()




# class parent1():
#     def met_1(self):
#         print("met_1")
# class parent2:       
#     def met_2(self):
#         print("met_2")
# class child(parent1,parent2):
#     def met_3(self):
#         print("met_3")
# c=child()
# c.met_3()
# c.met_2()
# c.met_1()


class parent1():
    def met_1(self):
        print("met_1")
class parent2(parent1):       
    def met_2(self):
        print("met_2")
class child(parent2):
    def met_3(self):
        print("met_3")
c=child()
c.met_3()
c.met_2()
c.met_1()