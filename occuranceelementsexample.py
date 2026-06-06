a=[1,2,3,4,1,2,3,4]
b=[]
count=[]
for i in a:
    if i not in b:
        b.append(i)
        count.append(1)
    else:
        index=b.index(i)
        count[index]+=1
print(count)


s1="abcf"
s2="abf"
s3=""
for i in s1:
    for j in s2:
        if i==j:
            continue
        else:
            j+=1
            s3+=j
print(s3)
            
        



