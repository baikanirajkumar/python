# x=list(map(int,input("enter the numbers:").split(",")))
x=[1,2,3,4,5,6]
for i in x:
    if i%2==0:
        x.remove(i)
        i+=1
    else:
        print(i)
    i+=1
        
