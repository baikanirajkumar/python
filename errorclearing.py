a=["apple","banana","apple","pomagranate"]
y=len(a)
z=0
c=[]
while z<y:
    if a[z]=="apple":
        a.append(z)
        if len(c)>1:
            print(c[1])     
    z+=1
    
