# try:
#     x=int(input("enter a value"))
#     print(x)

# except ValueError:
#     print("you have given non-numerics plz give only integers")
#     x=int(input("enter anumber"))
#     print(x)

# else:
#     print("this is else block ")

# finally:
#     print("this is finally block ")





# try:
#     a=int(input("enter a value for a "))
#     b=int(input("enter a value for b "))
#     c=a/b 
#     if c>10:
#          print("the c value is more than 10")
#          print("c=",c)
#     elif c<10:
#          print("the c value is less than 10")
#          print("c=",c)      

#     elif c==10:
#          print("c is equals to 10")
#          print(d)

# except NameError:
#      print("name error")
#      d=c
#      print(d)
          
# except ValueError:
#      a=100
#      b=200
#      c=a/b 
#      print("value error")
#      print("c=",c)

# except ZeroDivisionError:
#      b=20
#      print("zero division error")
#      c=a/b
#      print("c=",c)


try:
    a=int(input("enter a value for a "))
    b=int(input("enter a value for b "))
    c=a/b 
    if c>10:
         print("the c value is more than 10")
         print("c=",c)
    elif c<10:
         print("the c value is less than 10")
         print("c=",c)      

    elif c==10:
         print("c is equals to 10")
         print(d)

except Exception as x:

    a=100
    b=20
    print("c=",a/b)
    print(x)