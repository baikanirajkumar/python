a=input("enter the number:")
s=sum(int(i)**3 for i in a)
print("armstrong" if s==int(a) else "Not armstrong")