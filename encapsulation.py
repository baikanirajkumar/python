class cl_1():
    def __init__(self,p_name,price):
        self.p_name=p_name  #public access
        self.__price=price   #private access...within the same class
        self._quantity=10  #protected access...

    def method_1(self,new_price):
        self.__price=new_price
    def method_show(self):
        print(f"the product is {self.p_name} and its price is {self.__price}")
obj=cl_1("car",200000)
obj.method_show()
# obj.price=1000  #updating the price value
# obj.method_show()
# print(obj.p_name)
## print(obj.__price)
# print(obj._quantity)
obj.method_1(30000)
obj.method_show()


class class_2():
    def method_2(self):
        print(f"the product name is {obj.p_name} and quantity is {obj._quantity}") #and price is {obj.__price}  it shows error because it is private 
c1=class_2()
c1.method_2()

# #to overcome above problem for private below code is updated
# class class_2():
#     def method_2(self):
#         print(f"the product name is {obj.p_name} and quantity is {obj._quantity} and price is {obj._cl_1__price} ") #_cl_1 (_classname)...use that to access private..it is called name mangling
# c1=class_2()
# c1.method_2()
