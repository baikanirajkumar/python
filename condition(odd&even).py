result=int(input("enter the number:"))
if (result%2==0):
    print("it is even number")
    if result<7:
        print("the given number is",result,"which is less than 7")
        result*=5
        print("the updated value after result*5 is:",result)
    elif result>7 and result<25:
        print("the given number is",result,"which is greater than 7 and less than 25")
        result*=10
        print("the updated value after result*10 is :",result)
    elif result>25:
        print("the given number is",result,"which is greater than 25")
        result*=4
        print("the updated value after result*4 is:",result)

else :
    print("it is odd number")
    if result<7:
        print("the given number is",result,"which is less than 7")
        result*=5
        print("the updated value after result*5 is:",result)
    elif result>7 and result<25:
        print("the given number is",result,"which is greater than 7 and less than 25")
        result*=10
        print("the updated value after result*10 is :",result)
    elif result>25:
        print("the given number is",result,"which is greater than 25")
        result*=4
        print("the updated value after result*4 is:",result)