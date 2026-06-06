#why generators are needed:1) without genertors stores all numbers in memory
#           2) Uses more memory

#generators: 1) generates numbers one by one
#            2) Uses less memory
def raj():
    print("start")
    yield 1
    yield 2
    yield 3
    yield 4
    print("end")
b=raj()
print(next(b))
print(next(b))
print(next(b))
print(next(b))

  
