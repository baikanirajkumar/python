#method overriding....it is used in devops
import threading
def fn_1(): #global interpretor lock.. this is the reason it will executes line by line...it wont perform multithreading in python..if we want to perform we use threading module that will unlock the GIL
    for i in range(10):
        print("A")
def fn_2():
    for i in range(10):
        print("B")
def fn_3():
    for i in range(10):
        print("C")
        
x=threading.Thread(target=fn_1)
y=threading.Thread(target=fn_2)
z=threading.Thread(target=fn_3)

x.start()
y.start()
z.start()

x.join()
y.join()
z.join()
