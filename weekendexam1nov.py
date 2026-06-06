# print("create acoount")
# print("Login")
# print("Edit profile")
# print("OTP Verification")
# a=int(input("choose the correct option:"))
# dict={}
# if a==1:
#     print("you selected create account")
#     userid=input("enter the user id:")
#     name=input("enter the name:")
#     email=input("enter the email:")
#     phonenumber=int(input("enter the phone number:"))
#     password=input("enter the password:")
#     bio=input("enter the bio:")
#     dict.setdefault["userid":]


# userdata={}
# def create_account():
#     userid=input("enter the user id:")
#     name=input("enter the name:")
#     email=input("enter the email:")
#     phonenumber=int(input("enter the phone number:"))
#     password=input("enter the password:")
#     bio=input("enter the bio:")
#     def login():
#         userid=input("enter the user id:")
#         password=int(input("enter the password:"))
# import json
import random
c=random.randint(111111,999999)
userdata = {}

def create_account():
    userid = input("Enter the user ID: ")
    name = input("Enter the name: ")
    email = input("Enter the email: ")
    phonenumber = int(input("Enter the phone number: "))
    password = input("Enter the password: ")
    bio = input("Enter the bio: ")

    userdata[userid] = {"name": name,"email": email,"phonenumber": phonenumber,"password": password,"bio": bio}
    a=userdata[userid]
    print(a)
    print("Account created successfully!")
    # ab=create_account()
    # bc=json.dumps(ab)
    # with open("asdfg.json","w") as xyz:
    #     json.dump(bc,xyz)

    def login():
        login_userid = input("Enter the user ID to login: ")
        login_password = input("Enter the password: ")

        if login_userid in userdata and userdata[userid]["password"] == login_password:
            print("Successfully registered and logged in!")
        else:
            print("Invalid user ID or password!")
    
    def edit_profile():
        # otp=int(input("enter the otp"))
        # if c==otp
        userid = input("Enter the user ID: ")
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        phonenumber = int(input("Enter the phone number: "))
        password = input("Enter the password: ")
        bio = input("Enter the bio: ")
        userdata[userid] = {"name": name,"email": email,"phonenumber": phonenumber,"password": password,"bio": bio}
        b=userdata[userid]
        a.update(b)
        print(a)
    login()
    edit_profile()
create_account()


# import random
# print(random.randint(111111,999999))


